%undefine __cmake_in_source_build
%global intname scn
%global upname %{intname}lib

Name: libscn
Version: 0.4
Release: 1%{?dist}

License: ASL 2.0
Summary: Library for replacing scanf and std::istream
URL: https://github.com/eliaskosunen/%{upname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: google-benchmark-devel
BuildRequires: doctest-devel
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

%description
%{upname} is a modern C++ library for replacing scanf and std::istream.

This library attempts to move us ever so closer to replacing iostreams
and C stdio altogether. It's faster than iostream (see Benchmarks) and
type-safe, unlike scanf. Think {fmt} but in the other direction.

This library is the reference implementation of the ISO C++ standards
proposal P1729 "Text Parsing".

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{upname}-%{version} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSCN_TESTS:BOOL=ON \
    -DSCN_EXAMPLES:BOOL=OFF \
    -DSCN_BENCHMARKS:BOOL=ON \
    -DSCN_DOCS:BOOL=OFF \
    -DSCN_INSTALL:BOOL=ON \
    -DSCN_PEDANTIC:BOOL=OFF
%cmake_build

%check
%ctest

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/%{intname}

%files
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{intname}/
%{_libdir}/cmake/%{intname}/
%{_libdir}/%{name}.so

%changelog
* Sun Jan 31 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4-1
- Updated to version 0.4.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3-2
- Added patch with library destination fixes.

* Tue Aug 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3-1
- Initial SPEC release.
