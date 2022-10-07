#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5CC908FDB71E12C2 (daniel@haxx.se)
#
Name     : curl-mini
Version  : 7.85.0
Release  : 133
URL      : https://github.com/curl/curl/releases/download/curl-7_85_0/curl-7.85.0.tar.xz
Source0  : https://github.com/curl/curl/releases/download/curl-7_85_0/curl-7.85.0.tar.xz
Source1  : https://github.com/curl/curl/releases/download/curl-7_85_0/curl-7.85.0.tar.xz.asc
Summary  : Command line tool and library for transferring data with URLs
Group    : Development/Tools
License  : MIT
Requires: curl-mini-lib = %{version}-%{release}
Requires: curl-mini-license = %{version}-%{release}
Requires: ca-certs
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cmake
BuildRequires : ca-certs
BuildRequires : dbus-dev
BuildRequires : e2fsprogs-dev
BuildRequires : gettext-bin
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : groff
BuildRequires : libc6
BuildRequires : libidn-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : zstd-dev
Patch1: 0001-Remove-use-of-DES.patch
Patch2: 0004-Avoid-stripping-the-g-option.patch
Patch3: 0005-Open-library-file-descriptors-with-O_CLOEXEC.patch
Patch4: libcurlmini.patch

%description
curl is used in command lines or scripts to transfer data. It is also used in
cars, television sets, routers, printers, audio equipment, mobile phones,
tablets, settop boxes, media players and is the internet transfer backbone for
thousands of software applications affecting billions of humans daily.

%package dev
Summary: dev components for the curl-mini package.
Group: Development
Requires: curl-mini-lib = %{version}-%{release}
Provides: curl-mini-devel = %{version}-%{release}
Requires: curl-mini = %{version}-%{release}

%description dev
dev components for the curl-mini package.


%package lib
Summary: lib components for the curl-mini package.
Group: Libraries
Requires: curl-mini-license = %{version}-%{release}

%description lib
lib components for the curl-mini package.


%package license
Summary: license components for the curl-mini package.
Group: Default

%description license
license components for the curl-mini package.


%prep
%setup -q -n curl-7.85.0
cd %{_builddir}/curl-7.85.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665153459
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
%reconfigure --disable-static --with-ssl=/usr \
--disable-ldap \
--without-winidn \
--without-libidn \
--enable-threaded-resolver \
--without-zlib \
--enable-symbol-hiding \
--with-ca-path=/var/cache/ca-certs/anchors \
--disable-ntlm-wb \
--disable-smb \
--disable-proxy \
--without-nghttp2 \
--enable-ipv6 \
--disable-telnet \
--disable-tftp \
--disable-pop3 \
--disable-gopher \
--enable-negotiate \
--without-libproxy \
--enable-rtsp \
--disable-imap \
--disable-smtp \
--disable-mqtt \
--without-zstd --with-gssapi=/usr
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1665153459
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/curl-mini
cp %{_builddir}/curl-%{version}/COPYING %{buildroot}/usr/share/package-licenses/curl-mini/a1b6d897dd52289ab03cb1350b152e68f44bc130 || :
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/share/man/man3/*
rm -f %{buildroot}*/usr/share/man/man1/*
rm -f %{buildroot}*/usr/include/curl/curl.h
rm -f %{buildroot}*/usr/include/curl/curlver.h
rm -f %{buildroot}*/usr/include/curl/easy.h
rm -f %{buildroot}*/usr/include/curl/header.h
rm -f %{buildroot}*/usr/include/curl/mprintf.h
rm -f %{buildroot}*/usr/include/curl/multi.h
rm -f %{buildroot}*/usr/include/curl/options.h
rm -f %{buildroot}*/usr/include/curl/stdcheaders.h
rm -f %{buildroot}*/usr/include/curl/system.h
rm -f %{buildroot}*/usr/include/curl/typecheck-gcc.h
rm -f %{buildroot}*/usr/include/curl/urlapi.h
rm -f %{buildroot}*/usr/lib64/pkgconfig/libcurl.pc
rm -f %{buildroot}*/usr/share/aclocal/*.m4
rm -f %{buildroot}*/usr/bin/curl
rm -f %{buildroot}*/usr/bin/curl-config

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/libcurlmini.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcurlmini.so.4
/usr/lib64/libcurlmini.so.4.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/curl-mini/a1b6d897dd52289ab03cb1350b152e68f44bc130
