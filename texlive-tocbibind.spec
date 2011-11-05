# revision 20085
# category Package
# catalog-ctan /macros/latex/contrib/tocbibind
# catalog-date 2010-10-13 11:41:41 +0200
# catalog-license lppl
# catalog-version 1.5k
Name:		texlive-tocbibind
Version:	1.5k
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Automatically adds the bibliography and/or the index and/or the
contents, etc., to the Table of Contents listing.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tocbibind/tocbibind.sty
%doc %{_texmfdistdir}/doc/latex/tocbibind/README
%doc %{_texmfdistdir}/doc/latex/tocbibind/tocbibind.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tocbibind/tocbibind.dtx
%doc %{_texmfdistdir}/source/latex/tocbibind/tocbibind.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
