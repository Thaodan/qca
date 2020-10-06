Name:       qca-qt5
Summary:    Qt Cryptographic Architecture
Version:    2.3.1
Release:    1
License:    LGPLv2+
URL:        https://invent.kde.org/libraries/qc
Source0:    %{name}-%{version}.tar.gz
Source100:  qca-qt5.yaml
Requires:   ca-certificates
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  ca-certificates
BuildRequires:  cmake

%description
The Qt Cryptographic Architecture (QCA) provides a straightforward and cross-
platform API for a range of cryptographic features, including SSL/TLS,
X.509 certificates, SASL, OpenPGP, S/MIME CMS, and smart cards.


%package devel
Summary:    Qt Cryptographic Architecture - development files
Requires:   %{name} = %{version}-%{release}

%description devel
The Qt Cryptographic Architecture (QCA) provides a straightforward and cross-
platform API for a range of cryptographic features, including SSL/TLS,
X.509 certificates, SASL, OpenPGP, S/MIME CMS, and smart cards.

This package contains development files for building software that uses the
Qt Cryptographic Architecture.


%prep
%autosetup -n %{name}-%{version}/qca

%build

%cmake -D BUILD_TESTS:BOOL=OFF \
       -DQCA_INSTALL_IN_QT_PREFIX:BOOL=ON\
       .

%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%doc README TODO
%{_libdir}/qt5/bin/qcatool-qt5
%{_libdir}/qt5/bin/mozcerts-qt5
%{_libdir}/libqca-qt5.so.*
%{_libdir}/qt5/plugins/crypto/*
%{_datadir}/qt5/man/*/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qca-qt5/QtCrypto
%{_libdir}/libqca-qt5.so
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_datadir}/qt5/mkspecs/features/crypto.prf
%{_libdir}/cmake/Qca-qt5/*
