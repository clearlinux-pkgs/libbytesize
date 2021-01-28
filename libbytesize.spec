#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libbytesize
Version  : 2.5
Release  : 30
URL      : https://github.com/storaged-project/libbytesize/releases/download/2.5/libbytesize-2.5.tar.gz
Source0  : https://github.com/storaged-project/libbytesize/releases/download/2.5/libbytesize-2.5.tar.gz
Summary  : A library for working with sizes in bytes
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: libbytesize-bin = %{version}-%{release}
Requires: libbytesize-lib = %{version}-%{release}
Requires: libbytesize-license = %{version}-%{release}
Requires: libbytesize-locales = %{version}-%{release}
Requires: libbytesize-man = %{version}-%{release}
Requires: libbytesize-python = %{version}-%{release}
Requires: libbytesize-python3 = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gmp-dev
BuildRequires : gtk-doc
BuildRequires : libxslt-dev
BuildRequires : mpfr-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libpcre2-8)
BuildRequires : python-pocketlint
BuildRequires : python-polib

%description
The libbytesize is a C library that facilitates work with sizes in
bytes. Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package bin
Summary: bin components for the libbytesize package.
Group: Binaries
Requires: libbytesize-license = %{version}-%{release}

%description bin
bin components for the libbytesize package.


%package dev
Summary: dev components for the libbytesize package.
Group: Development
Requires: libbytesize-lib = %{version}-%{release}
Requires: libbytesize-bin = %{version}-%{release}
Provides: libbytesize-devel = %{version}-%{release}
Requires: libbytesize = %{version}-%{release}

%description dev
dev components for the libbytesize package.


%package doc
Summary: doc components for the libbytesize package.
Group: Documentation
Requires: libbytesize-man = %{version}-%{release}

%description doc
doc components for the libbytesize package.


%package lib
Summary: lib components for the libbytesize package.
Group: Libraries
Requires: libbytesize-license = %{version}-%{release}

%description lib
lib components for the libbytesize package.


%package license
Summary: license components for the libbytesize package.
Group: Default

%description license
license components for the libbytesize package.


%package locales
Summary: locales components for the libbytesize package.
Group: Default

%description locales
locales components for the libbytesize package.


%package man
Summary: man components for the libbytesize package.
Group: Default

%description man
man components for the libbytesize package.


%package python
Summary: python components for the libbytesize package.
Group: Default
Requires: libbytesize-python3 = %{version}-%{release}

%description python
python components for the libbytesize package.


%package python3
Summary: python3 components for the libbytesize package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libbytesize package.


%prep
%setup -q -n libbytesize-2.5
cd %{_builddir}/libbytesize-2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611859991
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1611859991
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libbytesize
cp %{_builddir}/libbytesize-2.5/LICENSE %{buildroot}/usr/share/package-licenses/libbytesize/507ba5f4949dedff9e01b4d5b64b365fdc7d4d04
%make_install
%find_lang libbytesize

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bscalc

%files dev
%defattr(-,root,root,-)
/usr/include/bytesize/bs_size.h
/usr/lib64/libbytesize.so
/usr/lib64/pkgconfig/bytesize.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libbytesize/annotation-glossary.html
/usr/share/gtk-doc/html/libbytesize/api-index-full.html
/usr/share/gtk-doc/html/libbytesize/ch01.html
/usr/share/gtk-doc/html/libbytesize/ch02.html
/usr/share/gtk-doc/html/libbytesize/deprecated-api-index.html
/usr/share/gtk-doc/html/libbytesize/home.png
/usr/share/gtk-doc/html/libbytesize/index.html
/usr/share/gtk-doc/html/libbytesize/left-insensitive.png
/usr/share/gtk-doc/html/libbytesize/left.png
/usr/share/gtk-doc/html/libbytesize/libbytesize-BSSize.html
/usr/share/gtk-doc/html/libbytesize/libbytesize.devhelp2
/usr/share/gtk-doc/html/libbytesize/right-insensitive.png
/usr/share/gtk-doc/html/libbytesize/right.png
/usr/share/gtk-doc/html/libbytesize/style.css
/usr/share/gtk-doc/html/libbytesize/up-insensitive.png
/usr/share/gtk-doc/html/libbytesize/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbytesize.so.1
/usr/lib64/libbytesize.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libbytesize/507ba5f4949dedff9e01b4d5b64b365fdc7d4d04

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bscalc.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f libbytesize.lang
%defattr(-,root,root,-)

