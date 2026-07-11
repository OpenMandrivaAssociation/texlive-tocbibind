%global tl_name tocbibind
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5l
Release:	%{tl_revision}.1
Summary:	Add bibliography/index/contents to Table of Contents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tocbibind
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocbibind.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Automatically adds the bibliography and/or the index and/or the
contents, etc., to the Table of Contents listing.

