Name:		libelf
Version:	0.8.13
Release:	5
Summary:	An ELF object file access library
Group:		Development/C
License:	LGPLv2
URL:		http://www.mr511.de/software/english.html
Source0:	http://www.mr511.de/software/%{name}-%{version}.tar.gz
Suggests:	%{name}-locales

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
%{_libdir}/%{name}.so.0*

%package locales
Summary:	An ELF object file access library: locales
BuildArch:	noarch

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
Requires:	%{name} = %{version}-%{release}
Conflicts:	elfutils-devel

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
%{_libdir}/%{name}.so
%{_libdir}/%{name}.a
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%prep
%setup -q -n %{name}-%{version}

%build
%configure \
		--enable-lto

#fedya 
#dirty hack for cross-compilation
sed -i 's/CC = gcc/CC = %{__cc}/g' Makefile
sed -i 's/CC = gcc/CC = %{__cc}/g' lib/Makefile
%make

%install
%makeinstall
