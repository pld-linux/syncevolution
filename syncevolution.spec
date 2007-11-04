Summary:	Synchronization for contacts and calendars for Evolution
Summary(pl.UTF-8):	Synchronizacja kontaktów i kalendarzy dla Evolution
Name:		syncevolution
%define     _rc     pre1
%define     _realver    0.7
Version:	%{_realver}.%{_rc}
Release:	0.1
License:	GPL
Group:		Applications
Source0:    http://dl.sourceforge.net/sync4jevolution/%{name}-%{_realver}-%{_rc}.tar.gz
# Source0-md5:	18ac5328fe863d0ebc2dbc3719020bdf
URL:		http://www.estamos.de/projects/SyncML/SyncEvolution.html
BuildRequires:	curl-devel
BuildRequires:	evolution-data-server-devel
#BuildRequires:	funambol-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synchronization for contacts and calendars for Evolution.

%description -l pl.UTF-8
Synchronizacja kontaktów i kalendarzy dla Evolution.

%prep
%setup -q -n %{name}-%{_realver}-%{_rc}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README etc/*.txt etc/funambol etc/scheduleworld
%attr(755,root,root) %{_bindir}/*
