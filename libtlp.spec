# $Revision: 1.1 $
Summary:	Library for interaction with smartcard readers
Summary(pl):	Bibloteka do zabawy z magicznymi kartami w czipy wyposa¿onymi.
Name:		libtlp
Version:	1.0.5
Release:	1
License:	Consult w/ www.gemplus.com and file 'copyright'
Group:		Libraries
Source0:	%{name}_%{version}.tar.gz
Source1:	%{name}-perl_1.0.0.tar.gz
#Source2:	%{name}-dev-1.0.5-2.tgz
URL:		http://www.gemplus.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The TLP224 protocol is used to encode commands send to the smartcard
reader. The command can be for the reader itself (Power on, reset, etc.)
or can contain a ISO 7616-4 APDU.
This is implementation of this protocol made by GemPlus (R).
TLP224(R) is a registered trademark of Bull Corporation
See attached copyright file !

%description -l pl

Protokó³ TLP224 jest u¿ywany do komunikacji z czytnikami kart chip. Komendy 
mog± zawieraæ ISO 7616-4 APDU lub byæ skierowane do czytnika (w³±cz siê, 
reset, itp. ).
Ta bibloteka jest implementacj± tego protoko³u, napisan± przez GemPlus (R).
TLP224(R) jest zastrze¿onym znakiem Bull Corporation
Zapoznaj siê z do³±czonym plikiem copyright.

%package -n libtlp-devel
Summary:    libtlp header files
Summary(pl):    nag³ówki libtlp
Group:      Libraries

%description -n libtlp-devel
libtlp header files

%description -n libtlp-devel -l pl
nag³ówki libtlp

%package -n smartcard-tools
Summary:	Tools
Summary(pl):	fajowe zabawki
Group:		Applications/Utilities
Requires: libtlp

%description -n smartcard-tools
Simple tools for comunicating w/ smartcard reader.

%description -n smartcard-tools -l pl
Proste narzêdzia do komunikacji z czytnikiem kart chip.


%package -n smartcard-tools-perl
Summary:    Tools-perl
Summary(pl):    fajowe zabawki w perlu
Group:      Applications/Utilities
Requires: libtlp
Requires: perl

%description -n smartcard-tools-perl
Simple tools for comunicating w/ smartcard reader.

%description -n smartcard-tools-perl -l pl
Proste narzêdzia do komunikacji z czytnikiem kart chip.


%prep
%setup -qn libtlp -a1 
#-a2

%build

cd src
%{__make}

rm -rf samples/CVS

cd tools 
%{__make}

cd ../..
cd perl
perl Makefile.PL
%{__make}


%install
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man{1,3},%{_sbindir},\
	%{_examplesdir}/%{name},/usr/include}

install src/libSCreader.so.1.0.4 $RPM_BUILD_ROOT%{_libdir}

install src/tools/{reset_tlp,scsend} $RPM_BUILD_ROOT%{_sbindir}
install src/man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install src/samples/*  $RPM_BUILD_ROOT%{_examplesdir}/%{name}
install src/{ReaderType.h,reader.h} $RPM_BUILD_ROOT/usr/include

%clean
rm -rf $RPM_BUILD_ROOT


%post

/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *txt  README.tlp  README.win copyright
%{_libdir}/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}

%files devel
%defattr(644,root,root,755)
/usr/include/*

%files -n smartcard-tools
%defattr(644,root,root,755)
%{_sbindir}/*
%{_mandir}/man1/*
