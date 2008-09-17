Summary:	Synchronization for contacts and calendars for Evolution
Summary(pl.UTF-8):	Synchronizacja kontaktów i kalendarzy dla Evolution
Name:		syncevolution
Version:	0.8
Release:	0.1
License:	GPL
Group:		Applications
Source0:    	http://www.estamos.de/download/syncevolution/sources/%{name}-%{version}.tar.gz
# Source0-md5:	0922da253c521038ba23e5f2c5972954
URL:		http://www.estamos.de/projects/SyncML/SyncEvolution.html
BuildRequires:	curl-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	readline-devel
#BuildRequires:	funambol-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synchronization for contacts and calendars for Evolution.

%description -l pl.UTF-8
Synchronizacja kontaktów i kalendarzy dla Evolution.

%prep
%setup -q 

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
%doc AUTHORS ChangeLog NEWS HACKING README INSTALL
%attr(755,root,root) %{_bindir}/*
