Summary:	Click Modular Router Packages
Summary(pl):	Pakiety do modularnego routera Click
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

%description -l pl
Click to modularny router rozwijany przez grup� MIT LCS Parallel and
Distributed Operating Systems, Mazu Networks, ICSI Center for Internet
Research, a obecnie UCLA. Routery Click s� elastyczne, konfigurowalne
i �atwe do zrozumienia.

Router Click to po��czony zestaw modu��w nazywanych elementami;
elementy kontroluj� ka�dy aspekt zachowania router�w, od komunikacji z
urz�dzeniami do modyfikowania pakiet�w, kolejkowania, polityki
porzucania oraz schedulingu pakiet�w. Poszczeg�lne elementy mog� mie�
zaskakuj�co pot�ne zachowanie i �atwo pisa� nowe w C++. Konfiguracj�
routera tworzy si� przez sklejanie element�w w prostym j�zyku.

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
