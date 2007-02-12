Summary:	The RIPE version of the whois client program
Summary(pl.UTF-8):	Program do odpytywania bazy whois (stworzony przez RIPE)
Name:		ripe-whois
Version:	3.1.1v6
Release:	1
License:	distributable
Group:		Applications/Networking
Source0:	ftp://ftp.ripe.net/tools/%{name}-%{version}.tar.gz
# Source0-md5:	07802f588874d66690e04ec73b02fb17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RIPE version of the whois client program.

This is intended for European users as it will query a RIPE whois
server with extended whois capabilities rather than a standard whois
protocol server. The whois program is fully compatible with the
standard whois protocol and can thus replace your default whois
program.

This program is aware of quite some extra flags that the standard
whois doesn't support. Just try 'whois' without arguments to see an
explanation of these. Please note that most of these flags are NOT
supported by non RIPE whois servers. In cases where you use this
client to query non RIPE whois servers, you should not use any of
these flags.

%description -l pl.UTF-8
Wersja RIPE programu whois.

Ta wersja jest pomyślana dla europejskich użytkowników, ponieważ może
odpytywać serwer whois RIPE z rozszerzonymi możliwościami whois
zamiast serwera standardowego protokołu whois. Program jest w pełni
kompatybilny ze standardowym protokołem, więc może być używany jako
domyślny program whois.

Ten program bierze pod uwagę trochę dodatkowych flag, których
standardowy whois nie obsługuje. Uruchom 'whois' bez argumentów aby
zobaczyć ich objaśnienie. Większość z tych flag NIE jest obsługiwana
przez serwery whois inne niż RIPE. Aby odpytać inne serwery whois, nie
używaj żadnej z dodatkowych flag.

%prep
%setup -q -n whois-%{version}

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install whois3 $RPM_BUILD_ROOT%{_bindir}/whois3
install whois3.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog FLAGS.txt HELP.txt
%attr(755,root,root) %{_bindir}/whois3
%{_mandir}/man1/*
