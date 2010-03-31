%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.0.0
%define		pkgname	dkim
Summary:	PHP Implementation of DKIM
Name:		php-%{pkgname}
Version:	1.0
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/project/php-dkim/php-dkim/v%{version}/php-dkim.zip
# Source0-md5:	6d7e89b035f76c83ad93e597ffe9f06c
Patch0:		library.patch
URL:		http://php-dkim.sourceforge.net/
BuildRequires:	lynx
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.533
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-openssl
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# bad depsolver
%define		_noautopear	pear

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
PHP-DKIM add a Domain Key Identified Mail (DKIM RFC 4871) signatures
to emails sent by PHP.

It is based on the openssl extensions of PHP. It can generate DKIM
signature but cannot verify them. Php-dkim supports RSA signature and
SHA-1 hash for DKIM. The relaxed header canonicalization is supported
(only simple body canonicalization).

Php-dkim allows any PHP application to send email with a DKIM
signature this should decrease the probability of getting this email
tagged as spam.

%prep
%setup -qc
%undos README.html *.php
%patch0 -p1

mv dkim-cfg-dist.php dkim-cfg.php

%build
lynx -dump --nolist README.html > README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a dkim.php $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a dkim-cfg.php dkim-test.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/dkim.php
%{_examplesdir}/%{name}-%{version}
