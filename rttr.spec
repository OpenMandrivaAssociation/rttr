%define major 1
%define libname %mklibname rttr %{major}
%define devname %mklibname rttr -d

Summary:	Run Time Type Reflection library for C++
Name:		rttr
Version:	0.9.6
Release:	3
Url:		https://rttr.org/
Source0:	https://www.rttr.org/releases/rttr-%{version}-src.tar.gz
Patch0:		rttr-0.9.6-clang10.patch
Patch1:		rttr-0.9.6-docdir.patch
License:	MIT
Group:		System/Libraries
BuildRequires:	cmake ninja
BuildRequires:	doxygen graphviz

%description
RTTR stands for Run Time Type Reflection. It describes the ability of a
computer program to introspect and modify an object at runtime.
It is also the name of the library itself, which is written in C++
and released as open source library.

The goal of this project is to provide an easy and intuitive way to use
reflection in C++.

%package -n %{libname}
Summary:	Run Time Type Reflection library for C++
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
RTTR stands for Run Time Type Reflection. It describes the ability of a
computer program to introspect and modify an object at runtime.
It is also the name of the library itself, which is written in C++
and released as open source library.

The goal of this project is to provide an easy and intuitive way to use
reflection in C++.

%package -n %{devname}
Summary:	Development files for the Run Time Type Reflection library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	rttr-devel = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

RTTR stands for Run Time Type Reflection. It describes the ability of a
computer program to introspect and modify an object at runtime.
It is also the name of the library itself, which is written in C++
and released as open source library.

The goal of this project is to provide an easy and intuitive way to use
reflection in C++.

%prep
%autosetup -p1
# FIXME unit tests are disabled because they cause a build failure
%cmake \
	-DBUILD_UNIT_TESTS:BOOL=OFF \
	-DDOXYGEN_DOC_INSTALL_DIR=share/doc \
	-G Ninja

%build
export LD_LIBRARY_PATH=$(pwd)/build/lib:${LD_LIBRARY_PATH}
%ninja_build -C build

%install
%ninja_install -C build
rm -f %{buildroot}%{_docdir}/index.html %{buildroot}%{_datadir}/rttr/*.{txt,md}
# Fix up permissions
find %{buildroot} -type d |xargs chmod 0755
find %{buildroot} -type f |xargs chmod 0644
chmod 0755 %{buildroot}%{_libdir}/lib*.so*

%files

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%doc %{_docdir}/rttr-%(echo %{version} |sed -e 's,\.,-,g')
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/rttr/cmake
