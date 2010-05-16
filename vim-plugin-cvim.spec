Summary:	C/C++ IDE --  Write and run programs. Insert statements, idioms, comments etc.
Name:		vim-plugin-cvim
Version:	5.10
Release:	0.1
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.zip
# Source0-md5:	c471cd4cee46ccd4faf91f59da170361
URL:		http://vim-latex.sourceforge.net/
BuildRequires:	unzip
# for _vimdatadir existence
Requires:	vim-rt >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
C/C++ IDE -- Write and run programs. Insert statements, idioms,
comments etc.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}

install -d $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin
install ftplugin/c.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin

install -d $RPM_BUILD_ROOT%{_vimdatadir}/plugin
install plugin/c.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

install -d $RPM_BUILD_ROOT%{_vimdatadir}/doc
install doc/csupport.txt $RPM_BUILD_ROOT%{_vimdatadir}/doc

install -d $RPM_BUILD_ROOT%{_vimdatadir}/c-support
cp -r c-support/{codesnippets,rc,scripts,templates,wordlists} \
	$RPM_BUILD_ROOT%{_vimdatadir}/c-support

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/ftplugin/*
%{_vimdatadir}/plugin/*
%{_vimdatadir}/doc/*
%{_vimdatadir}/c-support
