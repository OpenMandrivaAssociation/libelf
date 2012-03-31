%define libname libelf

Name:		libelfg0
Version:	0.8.13
Release:	1
Summary:	An ELF object file access library
Group:		Development/C
License:	LGPLv2
URL:		http://www.mr511.de/software/english.html
Source0:	http://www.mr511.de/software/%{libname}-%{version}.tar.gz
Suggests:	%{libname}-locales

%description
libelf provides routines to access and manipulate ELF object files. It
is still not complete, but is required for a number of programs, such as
Eli (a state of the art compiler generation system), and Elk (the
Extension Language Kit - an implementation of the Scheme programming
language.)

This shared library may be needed by pre-packaged programs. To compile
programs with this library, you will need to install the libelfg0-dev
package as well.

%files
%{_libdir}/%{libname}.so.0*

%package locales
Summary:	An ELF object file access library: locales

%description locales
libelf provides routines to access and manipulate ELF object files. It
is still not complete, but is required for a number of programs, such as
Eli (a state of the art compiler generation system), and Elk (the
Extension Language Kit - an implementation of the Scheme programming
language.)

This package contains locales-only data.

%files locales
%lang(de) %{_localedir}/de/

%package devel
Summary:	An ELF object file access library: development files
Requires:	%{name} = %{version}

%description devel
libelf provides routines to access and manipulate ELF object files. It
is still not complete, but is required for a number of programs, such as
Eli (a state of the art compiler generation system), and Elk (the
Extension Language Kit - an implementation of the Scheme programming
language.)

This development library is only needed if you intend to compile, or
write, your own programs with this library. It holds the static linking
library (.a), and the required .so link to libelf0.so.0. To run programs
linked with this library, install the libelfg0 package. 

%files devel
%{_libdir}/%{libname}.so
%{_libdir}/%{libname}.a
%{_includedir}/%{libname}/
%{_libdir}/pkgconfig/%{libname}.pc

%prep
%setup -q -n %{libname}-%{version}

%build
%configure
%make

%install
%makeinstall
