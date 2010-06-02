Summary:	C/C++ IDE --  Write and run programs. Insert statements, idioms, comments etc.
Name:		vim-plugin-cvim
Version:	5.11
Release:	0.2
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.zip
# Source0-md5:	bfad20328d13d74941519c609ab60817
Source1:	http://lug.fh-swf.de/vim/vim-doc/csupport.html
# Source1-md5:	97bbdc566eade34ad6b3ad0f3e87325c
Source2:	http://lug.fh-swf.de/vim/vim-c/c-hotkeys.pdf
# Source2-md5:	c2f5859dfc567db1262b5f4f6ce3f36f
URL:		http://www.vim.org/scripts/script.php?script_id=213
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

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%{_vimdatadir}/ftplugin/*
%{_vimdatadir}/plugin/*
%{_vimdatadir}/doc/*
%{_vimdatadir}/c-support
