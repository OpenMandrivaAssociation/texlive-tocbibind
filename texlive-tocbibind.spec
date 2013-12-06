# revision 20085
# category Package
# catalog-ctan /macros/latex/contrib/tocbibind
# catalog-date 2010-10-13 11:41:41 +0200
# catalog-license lppl
# catalog-version 1.5k
Name:		texlive-tocbibind
Version:	1.5k
Release:	5
Summary:	Add bibliography/index/contents to Table of Contents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tocbibind
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5k-2
+ Revision: 757000
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5k-1
+ Revision: 719771
- texlive-tocbibind
- texlive-tocbibind
- texlive-tocbibind

