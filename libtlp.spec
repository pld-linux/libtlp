Summary:	Library for interaction with smartcard readers
Summary(pl):	Biblioteka do wspó³pracy z czytnikami kart chipowych
Name:		libtlp
Version:	1.0.5
Release:	1
License:	Consult w/ www.gemplus.com and file 'copyright'
Group:		Libraries
Source0:	%{name}_%{version}.tar.gz
Source1:	%{name}-perl_1.0.0.tar.gz
#Source2:	%{name}-dev-1.0.5-2.tgz
URL:		http://www.gemplus.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The TLP224 protocol is used to encode commands send to the smartcard
reader. The command can be for the reader itself (Power on, reset,
etc.) or can contain a ISO 7616-4 APDU.

This is implementation of this protocol made by GemPlus(R). TLP224(R)
is a registered trademark of Bull Corporation. See attached copyright
file!

%description -l pl
Protokó³ TLP224 jest u¿ywany do kodowania poleceñ wysy³anych do
czytników kart chipowych. Komendy mog± byæ skierowane do samego
czytnika (w³±czenie, reset itp.) lub zawieraæ ISO 7616-4 APDU.

Ta bibloteka jest implementacj± protoko³u, napisan± przez GemPlus(R).
TLP224(R) jest zastrze¿onym znakiem Bull Corporation. Nale¿y zapoznaæ
siê z do³±czonym pliku copyright!

%package devel
Summary:	libtlp header files
Summary(pl):	Pliki nag³ówkowe libtlp
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libtlp header files.

%description devel -l pl
Pliki nag³ówkowe libtlp.

%package -n smartcard-tools
Summary:	Tools
Summary(pl):	Narzêdzia
Group:		Applications
Requires:	%{name} = %{version}

%description -n smartcard-tools
Simple tools for comunicating w/ smartcard reader.

%description -n smartcard-tools -l pl
Proste narzêdzia do komunikacji z czytnikiem kart chipowych.

# NO SUCH PACKAGE (YET?)
%package -n smartcard-tools-perl
Summary:	Tools in Perl
Summary(pl):	Narzêdzia w Perlu
Group:		Applications
Requires:	%{name} = %{version}
Requires:	perl

%description -n smartcard-tools-perl
Simple tools for comunicating w/ smartcard reader.

%description -n smartcard-tools-perl -l pl
Proste narzêdzia do komunikacji z czytnikiem kart chipowych.

%prep
%setup -qn libtlp -a1 
#-a2

%build
cd src
%{__make}

rm -rf samples/CVS

cd tools 
%{__make}

cd ../../perl
perl Makefile.PL
%{__make}

%install
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man{1,3},%{_sbindir},\
	%{_examplesdir}/%{name},%{_includedir}}

install src/libSCreader.so.1.0.4 $RPM_BUILD_ROOT%{_libdir}
ln -sf libSCreader.so.1.0.4 $RPM_BUILD_ROOT%{_libdir}/libSCreader.so

install src/tools/{reset_tlp,scsend} $RPM_BUILD_ROOT%{_sbindir}
install src/man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install src/samples/*  $RPM_BUILD_ROOT%{_examplesdir}/%{name}
install src/{ReaderType.h,reader.h} $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *txt README.tlp README.win copyright
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man3/*
%{_examplesdir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/*

%files -n smartcard-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
