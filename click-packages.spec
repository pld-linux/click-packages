Summary:	Click Modular Router Packages
Summary(pl.UTF-8):   Pakiety do modularnego routera Click
Name:		click-packages
Version:	1.4
Release:	0.1
License:	MIT
Group:		Networking/Admin
#Source0Download: http://www.read.cs.ucla.edu/click/download
Source0:	http://www.read.cs.ucla.edu/click/%{name}-%{version}.tar.gz
# Source0-md5:	8e2779fedb806bffb13d565f59c3ba76
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.read.cs.ucla.edu/click/
BuildRequires:	click-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Click is a modular software router developed by MIT LCS Parallel and
Distributed Operating Systems group, Mazu Networks, the ICSI Center
for Internet Research, and now UCLA. Click routers are flexible,
configurable, and easy to understand.

A Click router is an interconnected collection of modules called
elements; elements control every aspect of the routers behavior, from
communicating with devices to packet modification to queueing,
dropping policies and packet scheduling. Individual elements can have
surprisingly powerful behavior, and it's easy to write new ones in
C++. You write a router configuration by gluing elements together with
a simple language.

%description -l pl.UTF-8
Click to modularny router rozwijany przez grupę MIT LCS Parallel and
Distributed Operating Systems, Mazu Networks, ICSI Center for Internet
Research, a obecnie UCLA. Routery Click są elastyczne, konfigurowalne
i łatwe do zrozumienia.

Router Click to połączony zestaw modułów nazywanych elementami;
elementy kontrolują każdy aspekt zachowania routerów, od komunikacji z
urządzeniami do modyfikowania pakietów, kolejkowania, polityki
porzucania oraz schedulingu pakietów. Poszczególne elementy mogą mieć
zaskakująco potężne zachowanie i łatwo pisać nowe w C++. Konfiguracją
routera tworzy się przez sklejanie elementów w prostym języku.

%prep
%setup -q
%patch0 -p1

%define subdirs ip6_natpt unibo_qos models

%build
for dir in %{subdirs}; do
	cd $dir
%configure \
	--with-click=%{_prefix}

	%{__make}
	cd -
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,/bin}

for dir in %{subdirs}; do
	%{__make} -C $dir install \
		DESTDIR=$RPM_BUILD_ROOT
done

#echo ".so tracepath.8" > $RPM_BUILD_ROOT%{_mandir}/man8/tracepath6.8

rm $RPM_BUILD_ROOT%{_mandir}/mann/elements.n*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.uo
%{_datadir}/click/elementmap*.xml
%{_mandir}/man*/*
