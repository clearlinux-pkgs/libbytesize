#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libbytesize
Version  : 1.2
Release  : 13
URL      : https://github.com/storaged-project/libbytesize/archive/1.2.tar.gz
Source0  : https://github.com/storaged-project/libbytesize/archive/1.2.tar.gz
Summary  : Library for working with sizes in bytes
Group    : Development/Tools
License  : LGPL-2.1
Requires: libbytesize-python3
Requires: libbytesize-lib
Requires: libbytesize-doc
Requires: libbytesize-python
BuildRequires : docbook-xml
BuildRequires : gmp-dev
BuildRequires : gtk-doc
BuildRequires : libxslt-dev
BuildRequires : mpfr-dev
BuildRequires : pkgconfig(libpcre)
BuildRequires : python-pocketlint
BuildRequires : python-polib

%description
### CI status
<img alt="CI status" src="https://fedorapeople.org/groups/storage_apis/statuses/libbytesize-master.svg" width="100%" height="275ex" />

%package dev
Summary: dev components for the libbytesize package.
Group: Development
Requires: libbytesize-lib
Provides: libbytesize-devel

%description dev
dev components for the libbytesize package.


%package doc
Summary: doc components for the libbytesize package.
Group: Documentation

%description doc
doc components for the libbytesize package.


%package lib
Summary: lib components for the libbytesize package.
Group: Libraries

%description lib
lib components for the libbytesize package.


%package python
Summary: python components for the libbytesize package.
Group: Default
Requires: libbytesize-python3

%description python
python components for the libbytesize package.


%package python3
Summary: python3 components for the libbytesize package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libbytesize package.


%prep
%setup -q -n libbytesize-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517697961
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517697961
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/bytesize/bs_size.h
/usr/lib64/libbytesize.so
/usr/lib64/pkgconfig/bytesize.pc

%files doc
%defattr(-,root,root,-)
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
