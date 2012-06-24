Summary:	Library for interaction with smartcard readers
Summary(pl.UTF-8):	Biblioteka do współpracy z czytnikami kart procesorowych
Name:		libtlp
Version:	1.0.5
Release:	2
License:	BSD-like + restricted vendor's name usage (see copyright file)
Group:		Libraries
Source0:	http://www.gemplus.com/techno/tlp_drivers/download/%{name}_%{version}.tar.gz
# Source0-md5:	36b83fb77dc6872240e4b340ec441914
URL:		http://www.gemplus.com/techno/tlp_drivers/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The TLP224 protocol is used to encode commands send to the smartcard
reader. The command can be for the reader itself (Power on, reset,
etc.) or can contain a ISO 7616-4 APDU.

TLP224(R) is a registered trademark of Bull Corporation.

%description -l pl.UTF-8
Protokół TLP224 jest używany do kodowania poleceń wysyłanych do
czytników kart procesorowych. Komendy mogą być skierowane do samego
czytnika (włączenie, reset itp.) lub zawierać APDU wg ISO 7616-4.

TLP224(R) jest zastrzeżonym znakiem Bull Corporation.

%package devel
Summary:	libtlp header files
Summary(pl.UTF-8):	Pliki nagłówkowe libtlp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libtlp header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libtlp.

%package tools
Summary:	Simple libtlp tools
Summary(pl.UTF-8):	Proste narzędzia do libtlp
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description tools
Simple libtlp tools:
- reset_tlp to reset smartcard reader
- scsend to send command to the reader.

%description tools -l pl.UTF-8
Proste narzędzia do libtlp:
- reset_tlp do resetowania czytnika kart
- scsend do wysyłania poleceń do czytnika.

%prep
%setup -qn libtlp

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I."

rm -rf src/samples/CVS

%{__make} -C src/tools \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I.."

%install
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,3},%{_examplesdir}/%{name}-%{version}}

%{__make} -C src install install-dev \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB=$RPM_BUILD_ROOT%{_libdir}

install src/man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install src/samples/*  $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *txt README.tlp README.unix copyright
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
