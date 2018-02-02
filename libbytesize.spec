#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libbytesize
Version  : 1.2
Release  : 6
URL      : https://github.com/storaged-project/libbytesize/archive/1.2.tar.gz
Source0  : https://github.com/storaged-project/libbytesize/archive/1.2.tar.gz
Summary  : Library for working with sizes in bytes
Group    : Development/Tools
License  : LGPL-2.1
Requires: libbytesize-legacypython
Requires: libbytesize-python3
Requires: libbytesize-lib
Requires: libbytesize-python
BuildRequires : gmp-dev
BuildRequires : mpfr-dev
BuildRequires : pkgconfig(libpcre)
BuildRequires : python-pocketlint
BuildRequires : python-polib
BuildRequires : six
BuildRequires : six-python

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


%package legacypython
Summary: legacypython components for the libbytesize package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the libbytesize package.


%package lib
Summary: lib components for the libbytesize package.
Group: Libraries

%description lib
lib components for the libbytesize package.


%package python
Summary: python components for the libbytesize package.
Group: Default
Requires: libbytesize-legacypython
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
export SOURCE_DATE_EPOCH=1512067610
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1512067610
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/bytesize/bs_size.h
/usr/lib64/libbytesize.so
/usr/lib64/pkgconfig/bytesize.pc

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbytesize.so.1
/usr/lib64/libbytesize.so.1.0.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
