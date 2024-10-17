Name:		texlive-tocbibind
Version:	20085
Release:	2
Summary:	Add bibliography/index/contents to Table of Contents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tocbibind
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Automatically adds the bibliography and/or the index and/or the
contents, etc., to the Table of Contents listing.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tocbibind/tocbibind.sty
%doc %{_texmfdistdir}/doc/latex/tocbibind/README
%doc %{_texmfdistdir}/doc/latex/tocbibind/tocbibind.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tocbibind/tocbibind.dtx
%doc %{_texmfdistdir}/source/latex/tocbibind/tocbibind.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
