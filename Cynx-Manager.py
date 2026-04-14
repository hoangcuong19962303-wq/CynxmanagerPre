# -*- coding: utf-8 -*-
# Cynx Manager Premium - Developed By Cynx2502 (sieuthicloud247.com)
# Protected source code - Hardened Cross-Version Encrypted v2
# Copyright (c) 2024-2026 Cynx2502. All rights reserved.
# Tampering with this file will cause it to stop working.

import sys as ielo3n8pbof4a6r, os as woqbrm_uc36z

# === Anti-Debug & Anti-Tamper ===
def _mpiocdqs563wj3():
    try:
        import traceback as _tb
        vbog7d44awd = _tb.extract_stack()
        for jp58rteelauhcs_rqd in vbog7d44awd:
            gbrokag0plch = str(jp58rteelauhcs_rqd).lower()
            if 'uncompyle' in gbrokag0plch or 'decompile' in gbrokag0plch or 'dis.' in gbrokag0plch or 'pydisasm' in gbrokag0plch or 'pylingual' in gbrokag0plch or 'pycdc' in gbrokag0plch:
                woqbrm_uc36z._exit(1)
    except:
        pass
    try:
        if hasattr(ielo3n8pbof4a6r, 'gettrace') and ielo3n8pbof4a6r.gettrace() is not None:
            woqbrm_uc36z._exit(1)
    except:
        pass
    try:
        if hasattr(ielo3n8pbof4a6r, 'getprofile') and ielo3n8pbof4a6r.getprofile() is not None:
            woqbrm_uc36z._exit(1)
    except:
        pass
_mpiocdqs563wj3()

# === Exec Guard: detect exec() hooking/replacement ===
def bkaklj640_():
    """Verify exec and builtins have not been tampered with."""
    import builtins as ob8drz5qugbn
    nzr1tmiiog5kik93 = getattr(ob8drz5qugbn, 'exec', None)
    if nzr1tmiiog5kik93 is None:
        woqbrm_uc36z._exit(1)
    # Check exec is the real builtin, not a wrapper
    if hasattr(nzr1tmiiog5kik93, '__module__') and nzr1tmiiog5kik93.__module__ not in (None, 'builtins'):
        woqbrm_uc36z._exit(1)
    # Check if builtins.exec has been replaced
    if type(nzr1tmiiog5kik93).__name__ != 'builtin_function_or_method':
        woqbrm_uc36z._exit(1)
    # Check compile hasn't been hooked
    _real_compile = getattr(ob8drz5qugbn, 'compile', None)
    if _real_compile is None or type(_real_compile).__name__ != 'builtin_function_or_method':
        woqbrm_uc36z._exit(1)
    return nzr1tmiiog5kik93
p9dfejk0im61pwksmd = bkaklj640_()

# === Frame inspection: detect if running inside hook ===
def sku21g9vuvyqbrm():
    try:
        import inspect
        for fi in inspect.stack():
            fn = fi.filename.lower() if hasattr(fi, 'filename') else str(fi[1]).lower()
            for bad in ['decode', 'hook', 'intercept', 'dump', 'extract', 'capture', 'inject', 'patch']:
                if bad in fn:
                    woqbrm_uc36z._exit(1)
    except:
        pass
sku21g9vuvyqbrm()

import zlib as _z, base64 as _b, hashlib as _h
def qe64wri4t_cjs(h_utlvru8_g8jtc7z8,vdb_asa7tcdme):
    return bytes(wgwu4n4whkih57u^vdb_asa7tcdme[qmqj014c_gz%len(vdb_asa7tcdme)] for qmqj014c_gz,wgwu4n4whkih57u in enumerate(h_utlvru8_g8jtc7z8))
def zd0t67fs3nfu(h_utlvru8_g8jtc7z8,vdb_asa7tcdme):
    o80068g1ij0r_=_b.b85decode(h_utlvru8_g8jtc7z8)
    gbrokag0plch=qe64wri4t_cjs(o80068g1ij0r_,_b.b85decode(vdb_asa7tcdme))
    return _z.decompress(gbrokag0plch)

xpa40z88tf7isk1="".join((
"R;(;844Q?pzuwUH)}G-zyR;l_vjBa8LEn2P=Suv@_Q}tWW-n<R@vr5bhlUkg{$rAPNl8aSQ20T~P"
"X{3Dz?;HCN9q?^?*XY8zS}#A_y<LUAQ2CTMV`96C}(uyTN#<Py5__rd5!eI2AJn@hCpKrv^38A&R"
"W<~MSN$vYJ+7{H$t7!7veQu2Y!c^n@dE24(^+<SSp8eD%_NF<I*|J)L1WYqZ{c4i}w<LMJi(&GF{"
"l}wlosM5mVE5?G^wmP-bkhT<e<*P7Xe#-<2f?13a_%7E3+95{(afk#9J<sDlK8R*bWLjVk!)^1^x"
"yJ@jYkHWxIAP#AU)az6&70J8-D*dDQ6x9)f&{?BB=#7SBlwG0UaCzoWd-_9F5#S@TKe;4GlB<Zq$"
"h;9a1i1z?VviTZB5FDlK^&z}nV)E??!ek<3#WCcc;OV6`^<aUTxnzW8X*imPn7~da#Xi$t9{^wcL"
"{D)cZ^@2Yk6pp&_(MesG7+3B)Ob$2_7Yl=TCoqO;k6d?QNno|l+;<M&NUV^#^zkX3OR%>sDC~-J2"
"hLzYm>%{3wF&;12y>zBq)WqiJ)Bh3m}tRnc?H3o%?*Yem2sSo9Jg_KwRMUu*Ng1pN9-p<hgK=&?i"
"cTwoR3)zt6g`FqByYlaI>BqQnRPvM^TJGNH9m9kI)V&|4`1qK%#f7mSLrCF$@ZCy9Co=q8bcd(_v"
"uX95bW_$-TtJh3uu$OfJxg)O+&^*5rgHFV@!?&+<Z`RKQm?bS7gSQ){ZP^=HcTu_S3mXl$NZBe9@"
"!URUTVBPQuX2RIsAS=<V4fd4rol1X7do>ttsP82??x2hUg|j3sq2L^gNxLIzns&tUU{l#iW}m#Bf"
"IO6!wOQ^YxwLD(VKVp;9qrI};<58GJ_8w1iSKibxfQSjp_tYm2L2+#@$uE$1TvNIUi55YY_+PSwf"
"F*lq+9Yve2ZvVc$Ma}lon)EO|b{(;7mE#==hDAbC0O8a6uKrup>1IBG;^qm2G{J;i}*KfNyLC;z&"
"uC_%<f2u;nKN?la6PH^Ic{)Xuj{^<nq5^Js{23Jyr$(-#@M-vs6X)jr$SO1%-L$^CpAyScQI3i0M"
"Trot%#?CePhH99t2)!ozPLz}^0#|raR8~61AHW_UT?`EUS_5ZsPTSuh!+69qwos)uW3s)Vq0XK&t"
"8wH?eovcT%6w%nqJ4LT#yy5Lz>Kjb8AI>TTQa_=E>{u;muV>KF80q0&cC*<|zgL$C<z;*beOCe5w"
"KLiKWg3JZ4C@bh(J}m+=>K0rND_R+SNu}Z{6Oa~>1%ai<7-bAatMkg?{A4%iQJ6ZXR8i|YT92s=8"
"gyvU%82=QL$iL8-6aZLh-NyIqz6bCy+fE8wCY~!Dqr)bgSPm)hx1SQ=MMD#ehTFR2xuwndx)E9xX"
"eFc3PtOJS;;b)p{KzsRM^xi;f{y|D7JmZb((-M&4TA&B2}NP8v*U5(0yn6>${T5Gq^6<Pp_o{WoN"
"nP2*Oh0sg7^tD8A|yy17?eV`Mit{^JUpo#Nqm{qy{;e>8&)Yx=*he;0F0~^u*M%frL(7_%25v@VH"
")BJ+%zROkAz&-)s7@!CC!g9sU`X#;&838)i>Lm~?ah?4L==M&|lF1$U;PmraZXe&#qf;-dURn@ZS"
"&F%}*=2biY;gl?t(PJEJX=bEA@1ug=_U};Ry1GiGkTW4FC(1X4Bzw=M_$wpn8+rNKvhWk^)#!JP="
";ELz6iO?8=lOSWRpGde;q1LVOYVA(?dX~rUo#^-J;^Kp^(I$l%UlGM<$fpz#A*xwXO0??foyL5H_"
"W4v&jT8B7!6d$v7QgpGB^abS$KKJZG-&Bi~jY2WFl;upZr&mDLqp?jg#7w3;MB$JSk2n1rGU(SFr"
"#eCs3RUcn>CtMO2(5@cvG{GDyv6`F|fEWtpep%sjBMJu#f6&!_kh>b@NvDIu1B$)U)9?AvW8(x^-"
";R33p2k!xVa%#7(#TF`N?nA7Ct8b3vqSA*Uv)l~JPmI}TSR5$;<AgYV^Q}ud{1{-NiB_KF(;}o0n"
"}FeW<&CXSFEG6X;SpRCD4N3W)yM-G5kL=IPY*Hc3<-Az14+fltu(5-MMWOhec!gfTe}_86<yOm<T"
"I*=N9l$v>d$Z}@@YafkEN>nDH*XTI@1GsiT%lMTw<s5wu@e3K~yh5A)broM8=E7U|9-K)Bb*zynT"
"0sZ`;iHt^Dzy7iWR>86-D2qu}KpG`aZgmZ^OJO2;-f{i@>mH#M7iC~Y+0VB^|qfhA@<_k~wfHKrS"
"+O4tYgIEVa>%~RQx@!Z#@2phXcCHIWA>Vxdt!Byc4rYBc%2AwxhlG}=Kn01dTm;Q@k3v*r$jbef|"
"Hy4z9aH5`=P`lQG;Fx%lEZ<xPNyFr4LTwFOv|~`v=Zq>Em)0rD@}y-4h{uf~NhsL}WS?hk|0u!Z5"
"loomxoe+2F$s&hl`!Qe)8TE`SWP@FE}dx~&zU!rnUV$x7>BM83}{G8z<0oJ;mIo$h484%^x$?*?x"
"G``fw%|qn(5D%5vgjt0d&DU{koy2t)|`UMDc#bzb961t3=6K#jNC8#kGc%4O)C=kiohgKILnaaVh"
"9eg0Q9X@YH~`ZsC_dsYK#1mGPcDzfan7?RC>R$lSVCIJl)G#oX$PRh$Is|GH03No^&qfHX2x1&ZS"
"xH!Cc1cF%|`&@Zwctte`n!G|^lMY91CY~*uu1x(2HcFB^Yb!|nf956<qyZsIRhVxwKd7Yx*R@Gra"
"_D}?^-{jt0&nKJILEYi>*R_}!Y?QK66Ko$&*zc<=iRQ`$+l>bk`5T}~{`)25kyEhGSUqqH;-UfdQ"
"HmASp`9MEZINxSpW3P+d+Nl|6VUuYmrb#DnlVIFw6$gd4!2)HitlAGSh$!|wZoJ3Hsw}}Z-YJIlH"
"{ynbFXmv@cq@PnY|h@fH*5w2C9ua%{A>z5u(Qe=$FXOf!r^}GaH=}dXkxFGq;5HEw6_68Jd@`3JH"
"XfU16l-ln5KzTw_c;iZen&e>|}NnME_2^VMWqJ9Uv-*1r^4aDagMgIy_EMrV};d<{5a>sV5iSHzC"
"5#Oumz4H+YdN$*Ulo?%eMY|OT|I62@<7n^DuY8VaeZa;SFoyWR=+Q34~sykA+^1gAC)*Ltz8S32G"
"ahkDl21UN!0%JUkCh~)fHWr*3k+ZVx6Yfy|-F-^*NwICV2Gdqgp0r)SYgAtx@x1Ne)y|f$7M8p8w"
"fFhnjMGU|&Dx@hWtt4|$W$X7n1_XIEtxLp1g6F+ztGvZWGc&z3mTiU*j1nM<&E|%VE-}Gx*dg6Z{"
"f-PFVIG01K6Ya1bohVjzRvsU24Tx4I)~gzMIN+m4fR}>)aT*zzFa8rlAZC$7euABuwx9!Q5lAza^"
"9S(yX1?YYq8XCI6+x38xJ8f_Vb=D0AjLY0zIAA9fjNS_B*gKiVv>?OL|2RDE3kmNR*4i)Nt76>6@"
"LfK3UYJieB!EFNR|m4;W%1&DeH3@PT0Xkw9JE--)wT{LE{=ooD1ERGjZlN5Svy8}~9Z9?ihT&Z(;"
"CE~etS2f3w9%7knKP1<@aHwDULoONuwY=0=t;^}+_s0TD0Uwl&cjByR-^~f<g%%hAPUb*<(}HJzj"
"-Jp8WuT?^U(lpxqOUfg^gxy0pgcV#^t?Nv4BjXCuXC{UDBYXw98+dw*Wxx6u496?S2neT5H#XwkL"
"NL#&e@yZ-=alOs~RCaT%oNq*d!+AG=*3D`+VnqB*f%{ll_Y1$p@V_ldIck75Tu?&ot@v4aZR1p|2"
"FVbo0C%7;fE{C*@{Q9V{VqA*u`ulHq99@A(Kc{I)tJ$~%6>0r}bMGW9l92ohyY6f8&y5<off#xCh"
"IwyOW_K<0l$okxax6I^iU*spgc0OJJ~(xfLm6oQlnNahd-YN0_~aj-L>Lp}DLpp#tQa3YUIoDonH"
"mm&r%D$yb;^xyDU9i|Wo>?XgsV-z{GE_!~u@C=XF8Uz3CV68U`L9qoQ8oJN-ZDX3)etf8Llw)-o2"
"{;n>u9h_*F%ewC-6mYzjt9a}dev0T0Sp_8W9IdvQ*H;~beNx`iiLd6+PJ9pooApO9nDHpYJbNJbW"
"$Nl{1@-7$?*@^5)zF_6U=L-fa05&!zQ{*h0j^Wy4xPcRzYWZPJjgals1&**9#-Sn~!3j2$iSUNe~"
"NRU>e8j)ZUoS5e>X=EIlDiC&8M)v}HHqOqi!_{&I_GzG$_C(2$7JXtY$3Ft#mUwc_{Fo3h0ixQnu"
")D$A)tu>@k}0c8EHIGAHa{R|r3_~|1~^zVFDIz0tE*cvC+Y&!dplA%t;l@l>+CR{sV+Fr|NAVJdF"
"%@=7`b~@P88O;%qrodXF#n=aIryuO^Ff`R0R9sT>{_G#D*o=^xitV0_`IcD5X`RJ&=HbL=JdF*`B"
"CBhC*eGQKi@wj!Rn~N(7po_4`vLx<qK}nBoL;Os8_;W%0CKhg#r={gOl_(QZ0?rIVPO(blE8(q(l"
"do{RZD^i;&SbN#}hk*uSPi&rL_i{lIT7XyKx~~iy9iq^h?QJMGks1WbLW8@C~O5^CRhBp@EfBa*^"
"k#CB+y4Fg&XD1`Uxc|FzdoT#CtY0-`%-bqy1eFpy4m1y2VU+<N}*hmZwDV7XUcNAJ+vSKw{|>a3A"
"XB&yfHZIQgWE!rANu+TE`dRHvCR{Z@C=wh^d#Ih}B2;m_YC;D+Ox+vkI+LQQZ^ybsGctUf`7|lt3"
"V!^E%`zbDR0F%C>C*c?mIvuirpu&LWKdRQNJH%WbmI;fi-lyo@$&ba|^J4nidpH@2%&Hbp5;P6~l"
"E%aXrm{bJqH#>?$X3Q@#?4eeH@)X$j1?0*A-dCOd(LBF{cZ?5e?#+F?wmPDeu#p+s@?7Ox0z^mK7"
"%3UJcQCBa;=B4nG<WSYFg?r6Ir4$OTKdYeyCn#r;IB{FaIfF%OHVd)WN;?kecbz4N)jP%z(`d+Wx"
"Y1S=~9N_qZ~6&A4JJnNnC`bV8k={=ioZHvl=fWs*g)$hd^a&h?z}I^ukPbfLYB3!MHa#p>K0T0pB"
"tTd*6y&4S@(T#ih`euaRZLzXQ<4~y$LJN_t_?UugIJBuVQLt$E`lwO#U#^D@7Tdl)q3@XImS_em3"
"N;UChiKYEttp!|E)4|U;PCt+JN-bC$<ZEd3o6(KKX$CbD6A=%~$JVX9eTaL#)GMf1wkJEzqU2+qB"
";}SAEC13f9jle-b>X_rww+ExvzXMg@{wu-<9W{vA0fRf$zoy%B>W@EFFk5*&se?)@Ld@Vrg+C5AG"
"Z2!d|QZaJQ|gG0z&ixBnz#TT`V{>7_)iC-tzT+#ct;b0PKX8*G_1A22ovE8Gy7moyJ{uurOOduMY"
"$knn5t~!mW${Q=6KF9^2Sw{E8l{sf^G^P@}WwjwY$b-!3)lC4>HV6wCGlboxrl{P8PGvApfh5^TG"
"{bx@vA#5?5tb7)yIA1Tf4Nd1Ev1s@uAvkmmp&PAt*1wpxu3~HSYP-x8ik|6R^c2kLr&E|$*V}cs|"
"$yqU^;?4>AZZLK2`-+BtDD|C0T^4&3_F_?xC*qWU$eX|K$E*ol-gnFl>{#^0`LOFy?fFM3#69HKy"
"X<@_IOzYW9~F{?(Ae-6*0bsXDel70<$R&8+acmdg%Iimc`mh|e9cQ};=!$M*4G}Ayli?p_66Bku0"
")!oFLbOB1&u<`SHmiLG?#~3#KC*(GESC$tb7Rd*EdM0qxa4H@imjH;~dU)Cf5uxx9jp&&|U?&wc1"
"%u+<@Y|A($<?+x)dneb+G@)tBHO46k?<4utxwMFCn@TaE17z(k|z<_PBk`t!#^I;SmTwda=u&#6V"
"9l;tZl!g5&_SWcXCcFF_FsvM>g6jZZqi(>Njz|v;}fs*u(G1wf=tdN*iulaVi{fgNiT(h~AiOh-K"
"ZVHcHJs<ol;K|VLf~w13tf@ZeG9-ld$t2!GFy*XkG*#FN`5ls@TKs^25$fTW#}(xrP4R^&6Ntk1V"
"VbLbaw5w9$DghtyT7W>WZQ9VTeGJCIjs8&1xf77hQ5^1NC(nc3+WWj-XQy=5F6nan)gVYVGnHt#f"
">27R)1U1vr4%rHvAHDX3pu{DM@Zo_1JC&z#W|8pRW{HpieVf5!UY2Fo^fR{UcS`K&~H*E9E2tof;"
"_hf#^hP<?sNYsJyR~NEbjB!sx)QEy@EV^Mhld3U${?de=$T+ZGK&ehtk5)iW@{Qvv2wcr3sI;byE"
"_T?zke6dRnuDj89Q$%iSHsLkv_NT0kdhCeav<{|liQA59(YoS6b9gDhKNsh$0y;8zys+VtT`8o9t"
"`&Ip$kL`(t@KcO_VQD~{-3wD4TjUzDx9UCAh+0;?QbM6><R^1o&=YF_UR~(BE=qVPzF(C&I5V>i&"
"DLn0y+9XY{D+S$U$3uN10M0RkHd7hOMGY->ewC~tL}XiwZXW+nKx!mh#qlMp|phG4)RV(+x3lCAK"
")vp5Ly_b-=*WrAEKvSg?wM`d<1_Ptl|4Y{$(vH*Em2V@&Sd6#)E$xP}Q+A(;#)W7d(oS45^u|wo@"
"yeGxIqyE~l>3u#)un|AAdJ51jR#8}Ne8z2f)3f|3L&`Yg9?&AHi|1=liLMyOZm7PcsGe*2!;Aimi"
"Cft_4y?Fv?!X*dF})#{W7J?>gCaTWKU5gYKz-+{Onx%O!C3g_{Uh@3Lz>JUNdCQ{4#AG_m>w{vhc"
"Kz&(68vgw7M%90j49W{)8zZ(g4rW_@n8dmLC*$kyX@Edw-aFzKZN)c5fxrbLP-v$TmP}Y`(-B|*K"
"Hb(F`;_-=68bs*CM1mAjV~Sj@pMl|O8m3%e7B6520x1X4IH;CRY`4@`N&4e4S;bkYPZ{=QU5Llx4"
"J+^5vj`%1)DGGq{CiXMbjYmgR+Km$VMLqB<5`d7l5ZaW9i(S39_B4wbjTejzpAfgU=^9sXLZ{z*X"
"Ay%mMv3JKUDCb$OZMUL53r6SMtPu#q~~TpWBf`JJ1hVF0ZKsJvq}JBQ8=jP-VA8hv2?;~JTCmgS9"
"~8Z8ZKieCbXvI6v=->Ygu=ImSF;v}E%%H7C`-Xe|&Yb&^ThfE5Z32>@Q02WL34HQwmXJ@MjAU?qB"
";}N=Qiz|@9R|x3*v;70L%2t_@*gQRRP7C*su<E++J@Td_g@rPysJ_tn?HNUvc_{OOdOmOO-PU)kZ"
"<kBEoi#+4<tY4yM4l*>?Xv5-Egy|{I&Gxs20j1>VQdkfS9e?s6v(uAHgqZlDe=1=jW7ddXw6-8Hb"
"M~7o(aZjvrwd`oZ!qvbp5UW!)g}b0v+JYl}(hs-Lca=%E8X6Qh2H-TTQwj7^da4zTwpB==wRop!F"
"*0w5E;UA>M#J4!~Ge)0B1?pp<bZptUAYF;P0DQ=-5lc%3EY&`(luR}F`b*oLG)!j@&GlRSt>#G0D"
"+d;xotz6HJ9YU}q{;Xw}XXKr3K%ab25lL3T^`OnT%PsWd}R*7}r_-jM!^$e~i1`f!>NH}b;g1XH@"
"ddV6o7(588QbUZOJB0k4yb?%99$H%azQntUUTy+EIJa91O~g}uaFVGGegUxu+*}hnn#`^A-YpC^7"
"6jCVmYG8RgS~IQ%_a7PrHG0hbGYM1&oNP>Q2oR3jZ5UU*{i~xVdiauP&(`9pq9zu5WXyPl{Sd}z~"
"^)H;poX2w->zLLAVSsKzCXE?PPMg@zH(<qee@u^EtDdq+821DSXKuo1hc3a_hIWG!4$I>=`cZ6kE"
"!?Go<lzufO=IjX?)_F#+@_$ise;K>O6MbDY~Jl&Z-Th;}$n^#w=mE!@_N<W&9I?*}F_S;DCk@Ref"
"-KHeOyA_a~DPr>9g{q7aQd`p5nC3DkWZhDKG3v__Dm=r{Y0PeKo543d_w7^DmmYjLX?W-uuzDbvF"
"W4Fzz8%LbxzUDy!MvhE0Go*y+Cy7iO(pqcVdTfUOmw(B_UU|fX@OC8H7fvuMcHGNH7X27wmCZg6r"
"LFjVm1><vLna%y`z`NzmNynDqxWki5g!pNy3Mc75S66C&lJm3q-GR?IQwP?js~?pI!tp;?Z^b&YC"
"V*iql$a;EKPsrirYJ<_)r-j0!oL#j!99346TW+1d4~n?|gh1o{w=+rt1(|0yg(nj&LG&6>3t^T6N"
"eF@$EZYiFnnCPW{(WC6jPM(ZfEyh9xi1R0c=e6aRb+>cgNl9p3?L=%v(;7LMn|mf5!2pU$RSO7ve"
"Zlm0v^285`C9N=mlO-W{#01(<sd@6z9d&HfaWS$93ROKnDi99idEh&0gkTI}_pYrNgI#Z+LpwDs6"
"DO^82JQTe%V5JHYaxkF;>N+kx@%p3K(IYA?<pAS^k<jg@UA<tO`Z?6mCDzn%nZL^afwPiMuvm9yD"
"hUnE+%3saoV|Q%=-Mshg}vN%@Dj1MkjcuC?yH(#pw>cFz#Zi+c=NhzA^g1d@2YMib8XBYYB?nLYL"
"aU$TiJft*!L!O%vx3Kc#6P*{m!OT5QHbQP-bl0OBfmLo1`<R1(<vf>Syqz$2xLCF2J8HTnR7*{Pe"
"2)XA|N+F-^2T$H08Vluqm&jY<H9FmR>qm7$q3^E(sIUDM7$vi|o~9-*&cLaXVAto)#^b#ss{+e~I"
"t)e|s|9wN^F@SmS7-eru_fF&+tNiAGg*)0pvpK_Y?%mYQtCMJ{OkSI1`!n5iXF6Gv~o4)qYUY8{="
"bNT2QJB?NMdED_gv4pTR?5J5!l#i4tUz>mg49nJKSp}iFEmO1(Db<wWDZv7a3$>sPs9)qIoW~%Q<"
"N_2^DnJ6HC*<*R05hD*?Mq&Z-hIr{6g?n)mMFlYfaIyQ^_<X~7P4?Xj=7)3PpP4~gWul{d#92R#Q"
"NmzZd^OUT{sp6$?zC%Wbbr4bE07ZDPi-+bQ(?7C)rUK#oY@5uWxA=k{4-Rpgi_gtuoc0<jJfUJ$D"
"t0QA@%e)ua2R8<St!ZDH@Rpaf<@ZJY``AU&VLUQzV$vQ6q~8A%#62~nH`+my3F@QDpL$^0(O9aA&"
"3r|jalOC@Ni=_EmNcA1xVmbBMTy$u&_ARE8^qMln=>T6wyyPO~1d5tp1hqe>i)mjn9Y0NijeG=|Z"
"vx~x68vI;`oWAP@DtpVh)k{)TJCZufMxRn+Xx)pHH{JOrA^Y)AvX@%@H4wbW+VDms!x9VZ#eW7cV"
"*#+hlosPVYVb?JnqpBJjT6tKB>I_e6Sgjv!{lJVtN0F4_!9x|Yi_(@6*FK{HRYA_^5uqX%saq9Jj"
"meI$Rd;SHr+z6bP@xywJQKCdKFmMrtA~2RVv1hS7H2yB+#u&HtR4-C{+j149Cz~<G9hLOhuE*R7S"
"vO<Y(^5(b6Wz=gP@ys(MvEC&;RZ7yg4o2{`>(W(;ks?CD$umj)V@FQ_wIP%;BEM&Q;`b+$A7Y1l3"
"r@!S3nG;Kl12+}UPMT(b`3feW+lRq4|4eP=U2_O*-T=7g)z2J9+y@IIK@H@KS*%MF@Jh7;hzE+Za"
"j509*qTJg5VDARfTuKJ`C6K>`ZOceF11&}XnZ{*Unc3JJ;!k&gyX0>=I>mcGzauogT%8y=8-YL*d"
"w6ejAGq@0orDjoSb$?>;%#z8uOwutv8LFat((GSW$E5oqb=tHu5EV*-6xFVO)_BL;TG|(G_8UShc"
"}jQd(v4~?aFsW<>8+fT;dv)ovc5mw4C_M{H}t)-14WNq9_=_Oen19@7Cd3VvqCjjLt3^tt7|TL^}"
"jz4Cb>*-T#MCOBe!W%n+jnR&I}82+PuLL-zClP9Q{IjTx_%9-E>VBHIsk4zMmgXy##vD*TC9K-lP"
"vat2u6NG1%Z9hn9hj^pMseUecHbv1B3?Iu~AgM9xlb}={ZPaZF6NU_3SGocmcfpZroYsOAmd8Q&<"
"Ew6QH;6qH_U!ipS%K$X8_XB6zxAacDf6#z*Yig2H9Gmq+H1wfCc;sn}74-7~X^NSFs1N=fG?yF*@"
"3X(3ZB6`B3dH_g(Emd`5P7uTK%#Fbg*9`b9wK;gyDZ{&%=F^YDvc5z(2302gNw2s1pUy^&B`ped="
"vF^NdlF8$@>xNh0~K>Kt)7{m%nk<nj?*G36cVnsdI3^f2p$D^apMqO21(m$b-S=uSjd9BgoAXFeg"
"uX@X9AqoIn$DlDUg=-1eZ@6!6oGXbC|Km8|H?NYL4w!_D<28Fev{5EHA7nN2hz<awqZ&j@5;t|6O"
"jDGew!t=CIF^|2Uut2W;cZP!orCL>~Y+lIE}9lps~iyxqN673u_U)ch6vEOPT`yoM>;;^B%C5d0^"
"_T^+UoZ|p7ZT~cuaP9il16&D>Wx5xowq;WX5X%&q6YcrPa&)Q7SaDslGlp0`Mce&e)&`V3y$np4L"
"T%geBwkua`CnQ$y~$KgG}`HCnL|~QO!vv{nva;LhaIL&BbbI-Oj<<-^MxctQ~A|UCUW(WR+~=9@}"
"gL5rZhwRf#>sL+&f)rn<n5Ia0<-#zqR&E*v*2BGd^QsEXagODgYSFxt>Vd*`Nt8HgzxkbCD$G2uf"
"=vF+ClY;gzI<eHKf0ka>Zgz_-VkjOv6ydtM>MiqsR92!V3V#?{;+Tok`bE{zuyXVdm>zOZ4L=WOJ"
"E{T*V~jV&Qa|JkDJKvVwB@Jy>~3>H96%&QkGl{pj3jb0WtE(V>hk8pW~KtXX6N%G60Y4ymZzQGS3"
"7_lAW4B!SVLEM(<N#IO9R-%ZXgXav7fv1;^Tej}&l;K@5A6^&|er{Td?k?<g&xXIu%XTXQ;0`Z`r"
"Qw9}RY3h)$9z1G{89{gJ|CxD=0TW2eHONJv{ulB1@nUtlT;ido@Wo_rT>36a{I@Nf=$2|notin+?"
"QP~t>6}ui%{+9{$6*2i36aI{ZEZwS7sPUR!Foy;jCQ1?@F3bF)HkC7AnW<Wa|w0p1IaLnSWOt*hK"
"8H5XEjpd!~BHMMb>`1H~>*W!BPW>BM1)w+J{d1b?8%-f22+Jd{~g*T0mJF)K}FPT>c085uDkWC4{"
"3uuG|{@XIIYG5~9rU2X8pQgUTL^=cv*AF<$ZJ1nOHttBeo4Gi~mW_x?}U(~|<B=gBhCIO_=nE8p|"
";~5^>;k&cp<T$#*_(|RYDW_lod*d_DHuohIvY34_pToAx*4Q*oBwRrB1={d|!oFb$2nlq1EUs3~y"
"B{4?POV5Ojpmnj&|J_BlVrC02Dp}llei#5War4CxmW!4a1Lc)9OYgh5n8~22^^1Khmba71j=_^h2"
"@aeu$Z`)NKs%@5c7IM8eG<Hu-gheu@lB<eAdxjm6?dM;c=#E<D~|Lg`RJr^ghZIT0wE&=GKpb@76"
"~Oc`|3%aa>L3-GnA>$2m0p9bSv7(O26=iAa5<ARm&>uY5D#8KS>~pZRc>YCU_!2H=Xkfq(*)$2Rl"
"zME(#ZGyS5a7*oKW=);jPE|98!@nQaMA)Gy7DY5COG7d>s!N(|%FL}{v_C$*MYT$Mz#QDhnb}Zq&"
"K^Tq@Y4fXlG}cKg6D`Q!-9>WRuyKh;-9PF}G>jiW4Tg9OV*r^(VdH|03~oW+bD&Q(uP^w-nsNX@e"
"%%AxTE%d))YGzRYoqDu;W@Ftz{S%qO?t<`Ji|I;ulHb#kd0(1<T_(jeT=Z)*?I;6(_&oYV)*?;8r"
"#2j1e<7j@DUGKPX8!ha*w>V>cO(BD2*LRNgh6Hh1tE@f+4;YXqbLi04ybljx0THI7|n3DKupB+4l"
"4<RR2qAEoe940i`R%{DniO+cu3Iy_ZMP33Nz7CeO7;3=OE%UFW($dXpZ@GJGG19{k*9Eb&Ho*j&v"
"xEgvMp{MZnW8G;Ju`Bg7whYsltasK)ubpm#L@h$6!UbS;z)k`NQ5`b#n{6vSj9@tEZLAF~a;1`<A"
"_9Ii*tH9c^b-O>VIFpOom|&^}3YJ|Gc<wP&VK8U@o=w)r9ZgE9q$O5tyX>D4@H=LsqDE8?so=NHf"
"0@nP5(yJF2Mc7GATpEGl1D9&+z<2Tj_&y#cD2w+3Xv>lL_kyIkCGL-dpwWKma3=F@ay1Zu<Bj7X="
"NDBC&ajD(*59^HE|AU6A(or3_W(ir2pKi9~zN&c9y4WcOXh6)rO#@m_p5pHX_Pybk$dn*EfCe8_7"
"Q+UZtII%<cE=!h@f{z~?S6U+`5--&J7EQ+t8IT;p1MEwLRF-na(+6PASz$?g(0);Px3AEW}|J>BB"
"+U3ZPSLo|}neTCQM`2dewHm1I2AlGM(SpLexy4gbR#_e&A)MR8p7f!&59|s~N75YMM1iSBOsSv*8"
"5*18L!R`=Bo1C;Dg@MfPV+Zt4{%Ke|EM`Spc@jR{f~EknPldt^ev6`zG}M5W#e(S=9im{YnVdBDI"
"8g3bnz~+f+9_ApzhVI>ryLMB@r+Y;2~bd;KooQE0krg$0j|X_>Dn1=!#(`TaM>^UB~TnYUbaAYe$"
"h#L|I`HHGA@{i*~fU=HiS=gpN^W{A{izY4?TupzL$v=zk%X%6O_nkDr<}%>rHJJyqsWI*9O7|G$B"
"{COdY?5E5c#&W`<!&=VIPEJINBI&4H#Ao;8PWA{MipXV0bh@8SmI))lC5v?8JwRo^{kQTTd^cpWj"
"(Gc-|#vea1R(G(|&%S9o6&6uPMiZ-hjC`$fX&iB3MdV!J8>2vA{t=BOhb(*7cg;Z^lP?~=GMnaq3"
"elF-+sD#cSMI!E?8bVq8LUGE-t(M_zpGFMbI7V#H<So!;#LD*2%jKrP^4^@)FW~=rR2`odDvBB^^"
"Vny9iyh)(_f%-!?8v}_NfG5L9=@V?u-3N0>KgLid|0HZDBhNsBv1e!FjuD2AIQZKAGG#@AN{B9ag"
"4(D^d1;XTtL71Tz>DiXdyag^0)Zbtj)!~ZX5P3Sy<zMH1%_dZv<<0g)OH=jns&FHdWD6iM(H58tT"
"V55{jv*G!3^N*$u^r;UFPem7JYz@`<GW;M(R*U&%eyC?@W5d&0?iI_-&3kYJJSQ7B{Hv7TN0fIuJ"
"$g+H)rHf(0gF({%W4yf?iw4XS2goYihw*{TlD$M2zc-jv_I#xTvv<D2B6ibm`K_0RbOKK#H{oa~+"
"<Q-PF3Zy3sb}@$z0dk8U^JZqL>E8sfENqx(K6fGicu7gbM$1PJG7#KZY?C!%5=+oCRFJ$rNV$Wyx"
"<h!U6~;!&OZ&09YiNj`PF0>Y5<vORYF<H5C{{QqQQLm)hY2w+@GUW9(p$g*&+Aw+PA^M!4tRPIJh"
"}AOp<#B<vZaqnzy{0j|F-qOo03-ho8JP)I&&+iKdbUh57FLl=+3iH*PygIm2wb2FVFmjVK1ziy^-"
"{X3{qH($>bZT*WHEzC=2boi<K-W_Im2snsrw4$-gzd8sGp0T>U2W*Ny`)$f`91Qm)SDkoZxftTLU"
"|IPwi|&`aA+(eEayZTRiWHteLQR;FI8AY7UDU=P>K5f;`U8^-$7Ne#DVDS>r31?zL+P5&H5{V^kv"
"LT&9B5-$zAC4tmO50wH3ggf%Vzs~GnTKtf74a@+IaJ{2Ki95K{GPnLsF9o>tbefD%3b8_NB=lu&N"
"DdoCtgcsN6RdR4WeG3!pqd6bf4M0cV#6$E^~1i|*Qo=nuNV#@6~;BIAO+xDSZV=M7KHv@UNpYW7#"
"p+k(U^*zXV`&f=5%@MLY*Iw446)pY2BWO-+w<l7aOaqyGL?5)othZRka-aY1;%SKA#V+t1^%x4GL"
"5(4rt`Ax(&lfxIs<Md5OTe=LbSiL(M*F1(#BZ;)_soH^GSXjb8F4dQ8qkEDtC^wO!(_j5H3DIqm#"
"a=;s?9NE`O7(M8VAm9^U=tlqt3mJSjtj(W;cHE&FEa(zI!%lj~~OzOGlytzogYsPR8P~o2BlEe4X"
"Qi0oWcwr!uxnBYkrsu$iEYUR)5K#$lxV~`nm|VT|=iiuUjf8<26ku3Njw<(xm6uf%5O{KKgcLXc6"
"Y#_Zgz`h;N`0?OS~2c1kENrCV#7$1MOYpN;GZ%#Ak9`C`vhodWskxvM*pR=tsGks!#$rKZ$M(Q5X"
"pvIG3J(ZjsA|QC``$EKZsM<ugKFhTHj_9?0l&^Xi87GJJ=Oo<FU0wg?)CVd*WnB@ch=~%j?gOtS|"
"7EL+LI>zA;`|GjoBrEX?g-$jEdx^h|Kmyw=KXT8nwtm|hJI!;dI7VjMuk4ds<lm!R|nlB7#@ND=~"
"EvN`D_Tm*xR6tWLDWWu4u5Tx5j;+;ctc8B95wyHg66aBAl+?9xEO~k0YH`y=rQ!X4g;p=dkyW2Qe"
"u{wWwNd6qmf(Yb@qS1RNk-Y5c>vTiT6u7$SorF5V>26ynX?{KG69Qu2@!=Jm=dq*hxMpcD!Q%{h<"
"63a#yJf1AT9-t701ZF^;LM&V<HYH~BBWKX)p65)Ls;g_rEE$y@jOBtIS|!hWAFQggZg!K3CG{(6T"
"qb9b0Wkb5P=WBga;L35MF*tFb0vzTr3v*z23r{w0kk2yo6%vQ6vRCD;MW?7>lYMg9NOzh|BV{Fp@"
"WUeaimZ41rO=S(!GIdUf?@5MS(mF#J0o!9rdeo5N%Rf`Xwz9LT8-r*N)H?uB2jI8e9$W~{cE5p3l"
"GYb^GKwHI2OYiahOXoL^taCRx2?GQfIZb)wsM0<5WY9VG;7cN$(g@z8RPT$@eN%9v9(|>i2NUqU?"
"R>`SRP}Et`QfvVaU7lzjaf>@!dN<(I<nRio1o<1kmf_Yygt2h&a^PrX@ln|OnB>7G7R;&p5&Z*C0"
"4N0%<5Jl~0g`qSb)A2e)_t*d=*H_uToA~QWwuhn^pb{YX7pgR)0bi>N2vnm2yoY3rB^)@9i|jlKN"
"%%{hs!QUs08C!FpOUa4l0B)oY`;E#^e@u_TD#;oYC=E?^dEC(UM?CK_U=kpF7Jm^ABgC&1YoF!Sg"
"&o_3X~ZCQdXhlPqPsXorR4m)%GA0nb1+3v{o+ch*Uy!+&Q~;%-P8P=yt-Jm$$zBKtPQ(dwzGgpVX"
"&K)5VFh)yJ`8{g6!mHDY6T01)Zm}8_2OOLZnVUd!`Fy`|frL$T_?jM~QP<il=BO(;r1Fv!6JS@|-"
"%0`n?lBOwqMlk&;nRE@nk)6vDSQI$Q)O2B$P~wNwLVBPDyVEi3n%DkOKk=w!Q!Hr76jSk-Mn3>=`"
"*oFpXRg(tB;K6dyXAfX#Xhu8L(l1$4D&KxLAgN@A1xQ@qJK|rwPm*r(+MZ<42>uI;i;I1eU&X$x0"
"vkTkb0g+-Tz7Z0tEbNdW`tKvnHwO4S$9ULf*obKtv=5{M`hEL;Tb0$DT2noxmLy$}?*hpa#jelLq"
"?@R%m-@#s|8KR8H=R8NroqMd!8KY_MR$1fRE{OV&1q?Cn?-KJT8QMxVsOcyZQTZ|I)^7wovbRS8b"
")U+;8@cn<l(ODdS+*ION3Wpf-99epdTvw6mSfqNVv-jQ8=?h3T`qyVzmd<>;Nh`fx-9CKm6u4x&D"
"MZwqiLGdm3e`c2gf!2cKLMqfs>JVa_GIYf8)*rCD|71L`aVJ21!c>0_9QS6k&uee{4OGFk8w<pa;"
"JSG{lkzFU51yNJlw-4Mvi3oCp7Hz6jy57AI<9WykL>Sh&&<+90M#C%28I3oTWOj#e%_;!$%!oiv!"
";#{M=hpK<p}0aCTwq;Oq@6(9%+5?*w7awXp56s-q_ja@ByxSD~%p~xagTjWH5P`T?TQ<yRJj-2TT"
"Z?7@xd#@)Cln);~*07%Le&J?RuZ-W4i3tMk=ZTO&I9%6M!$=zEs^)kelQPq@5NL*>=goK!$o-dIa"
"#Jie0C#^gGX79GZj$$er$5E6qFdqNvPI+ZGa{UnE8L?DNc2(_W@xb+OCE&!C-n>34#MndjyGX;(|"
"orT~?`i22IGceNaN!*dQ(SQO0-7T8RFrKOtzt($_d9v{LK(D06Sk}}Y1loAO6$GbqyktT#M2C4W2"
"1L4frZ<sQXI371<{;1beD2q*k$miLWJP<<c^VPm56hUZA5J5u@$u`xlepmvpRGyxDM>_Im_93@6o"
"f`{85u)-Ns9ud6SELB!tV#qwlc&Y43)faQRNvOf&7-`78J6;ki#wF#3;z-9P!tHT$UJhPcrrFj5_"
"PhP_-exC=$1X2X?Po%$D*OXK}pBnn9o;m!SpDGtf#b;w2<tZR=e>NlUs<IzJmGUHG(O<1x5oSZwY"
"%RsUVMQJ+iYIrSc#15C|QDgmZcdD<s58%q5Zq7l^<km_VGEP^#-dme=MWPr*K=y?u-*S0Wa30T$e"
"$pR$vzB2_c#g9y`8>{M#&HX=AjmFZ8HsqO`RE6ojc}#Ip+|hamD!f1fFG5<-7VsYOQ%zxTinOPG2"
">O>J0P62WB(ytpE8=a)n*xu1RSDo0as7D|&S1wLiL*Ap;@x`5%J(c-kIJ;s`gvO=ch0K4%)1m7#M"
"KPLXlicR!8V~&gyMtWkSCc3`Xm$1#cpDq1gRv*4ev?F><5X=*DZpHw{%Bn)HCXH3Tf)$V4`oPO5d"
"YABJ6v{D=3Q799n`y>pLKIpUepGLI{M(p_cpfin{h-EiC5DHdhBu{tycHXOyocpf4S8C+!m@3P@0"
"LY}YYyP){c+%{rKzj`$b*4ZR}JkS{1}1Al~wN_c0sHqApf&N%o-WxRsfLObn#G9G?UqW@P|0U5P`"
"#QL@YZEg#AX_~@5DL|dhJSAk(Y#>k~c8anoDx#?Tg(r`v%^>8U^6@{^ef@MO+IwN#mB%Y?r6<Df8"
"`uXO#pamD4@`i^@GIz86wA5VV$m6XIXV&w8+OnVNo*L$#|j;5X}HkGvQ(H)iprb&A@14=$ZQ6;yo"
"0)T{6Ac9_n9cU1RJNPBbnQSAPQpsG_gqDm%j~8BUt=-4WjPntqamOa}yRTRW2_!$2)#3R0YrD&vP"
"LO=9r}4l${t)6+N#z3Czd=FrM2O*Q~1_&$Us<T?}zwW6JANt6Cj%+o&K4VCot;sDqVJR}l)0m<uY"
"zLL&!pgO|v2J*50NzY&+~e!&4fT<X!%cdj$Fqe*TKsnSsCCGIt#n6t={pATP5tsx#QLo{;B$cp>r"
"K#8d9e1V2yBPWny2a=v6v`fIV*OaXfU2p?N<IG$o1DTAg6uYz<GA@&uX(ZGplGx$nx8~7SSr7dKu"
"4k9K&(o3zeD$F!i-oP=>x<B!ibREn3;)J25isA}IBZlvlEhZF8P|F)9oN01!uv>@^FaLdP1WZdhY"
"pN2OmohlzugbK$sY##sSF~@bLicJud9l>u}>-t*vpyF2sE|tcii6!5LW*n@j1V!R9baoo0vCbryF"
"%BXv82rs!1D~phVNBqce{O<h#ffQ#{27MIl2#G;Ru?GYxSNKGqzIsCQ+rNA^wBr|Mx3xa7e?G8av"
"Ilm@h6{y_p1j$byv$z#|FYf*33Ai*KteXvYteAS)@wyuzQhFn=tg{@gWXoRyloO7G(w-ph<7d=CL"
"nP~>w$nujvGr2)r$3JYcqzVNEc?TBk7A=AtEq0wJ!5ii2D05np^1%ruh){KZY;Ti@d0)3<YkCa)o"
"gwN_t%v7=oI2B(!@K@`J(w29=~#<xn|qmRN}yAWFnhv%(V_Vb$mcMW+Mop~a`IVWI#2=^uSV(_v~"
"gya)juSqMG1!s5JmwD(3dz4iJMS4+t0RW&BwGSCyabTle3v=o}Bo1kv$Ohh;^t)vqvJ?sHZK2TW?"
"EnFM$iY0jul1S{(p$xeOahHj!wf+t30Ou$SRmdu^a;WT3gGPCkvUd**7BLVLN+JDjggm|ii@gCQn"
"q2u0MgoVfO354Wy|#7ba4@%lMFx8f`0?CVDF_s?KQT)$bU3tzG*AIyXk7-@F+|8rVNI75bJWnRW`"
"OAn6rH*!b?M}%L>A;=rJVoV(L5%~FHg!bF!RA5TQEgF-@hJF*aPo-rJg_Vi*@5W2Nhhzmlsem0Qz"
"%|OJcKen^5l=!)P7}`you_+SfvZH@yvfx6bQS(86|RxN#^ObXS)eo{Hn<{LGX*QvntL)+SxMSI$e"
"OVGTH@~=O_)@n@gEU`GiA!M*Ogi9KTR96Nw$6$I*28%*S!`Z$YPXn6+CJ^xr$}1y4q@G)rh3Vc$;"
")0D(r!R$xot@VzLp3q2kRUK2Uf7893g82!k(4B>bjt>$%Z{FbH9E5xISFvl2@4vYD{@1C)?8fyT^"
"5T;WO<tNiAkBb7O^Ye30(F=bE9A8w>XCrBB+gzBi>OrTgH?sN1-%||mSG+)W(qiK4qKL088zQ;x)"
"RvI>0CZ@e^YWR#4nBnLMp_%u2%aT~v#b39?H>g7;UC#_guw=~|dTQfy^=7WavFlzy{bV3;nSph%8"
"fe!s<eFsO$hPUd!B@`K3QJj^06+RpjmHvv7=l^pqQ_ZfF#-h=otKoD?ceYVaVXT)@)-CoT5Dl!Dh"
"O~KpjJIw^T*=;O{)?gDDJe-GTAY)$R81es+N*Wv(Vv+x7tR2C54_JIirFOCy2KQ)~&J}WXKyxR??"
"Y9oGk4K$*|{)t!dN+Dq|pSF;YAqY`YP&LAg2T(n8c8VLT|8F{xfz(wO$O${cbKWP<{bC$uN=_x=1"
"B)T4p00o&eq0KlRQE$5tNp3tD6pwd>*6EOI#EbfD`1y?G(jW-cWDo{asyxcbbi{J@&=9tl*I=>FB"
"S{b<slD)5C{GDY|<s`EyFTr1Q`qR@JPy-lS%KEuq`Qi2cJdxP8oUu9*LEjmtLL#O@ibR`3AhkjDK"
"!BFcq(dXp0)Nvcf#}o=c27;D`fAGR3z)LGFq4ID!TOPJgeNS6#AlhKJe>&<#`3qT?Au|{k+ur+n@"
"UQVGn@QBLNwrG8EA$(G|G_D(SQnZpqj{qlB+RgN7tQ+8kacLuApI2An<LZ2K=_6`j!^)mO7DWJsG"
"P^^ku`qR;>;Gk`R?AkRKg=GXLyPiMb=)ALuro2S>zlTq*Br3G><i)9j_(Vb3IS+`~5HtX3M+pnGK"
"gMes>iXD^yG8Gujpgw3mG*u{#q{t321f1gBzFrV}yT?B+(=v@)j#K6;ie^B;3Ynh8?0#3)d+3r3~"
"NET-WOXg(A9{KSgdb$@bTL}!-<go!k(!*P?z&>Dwz`Yo|bu{ttHSmdCiN+MA^9Z8!L#86XBsU@oE"
"~bEr7jCV=3W;S3h%;eyF18WUS6o+81!yCdJcApXLD+|aU7r>hl9nn@@tUf<nWv+VPn=lgIeFmgde"
"%lKHMnlmX*%>RYzt>>t?{>fo?qF|4(pr~z$nm6i(ciP_G`Jn#US5LGj7baIgCo)RR}c!Dlf_N5Vc"
"o`#!xmY0JA+OG{ZJPA?cX|ZQ#_$QGGR%OVM|uwaC>wMDcQfN+H(TaLrUB@4m1EI?^48fkHeu*~yI"
"SE10EpVlIM~tZ$?h73dF5`t`h+I18&jAwRl$!uK0V{(fbbc{Q=<X3R^Nu>Yw+TrFxtfW=2hW%LVO"
"n9n)C-!mWFbgR9}b;>&e$G~wZB+d?L-$w?m5V~nh3L=%L{-=@by|ZiNAbzPOXqgwx_hKPo0n-kxi"
"2p#~0KfjJL!JW7;vbVu=sJU;evqdb(Kzq1?V-`dw{`!9@B2JCRkL29$x?Nmu}71LNo#;+edZmi#y"
"2+}pCaKy$Rf6PvaQ)=g5%uVo5@#2=MzQ95A7$<yilfD`bQA*_NAiBbe4R<N16kjupKwaqU>C_tHd"
"9VqIQS~8)8GyxaWF7F8dV84-@}mt6-M;6UXnV8(4|r9B5Fn+4w@zSoY0=j+P7%>8Bycz^q9Q_!%*"
"Yo_(n?4!-HYGVQ7I!DoG;^-rBPamNyKy2$!@X&0+l1y#v>{{#N_T#0!-b^u;w2kc7^^QISlk^H=D"
"BQVWx-Cvqz5ztVy4l|sR61%{235`dXncPSEIe~&~kn2MkeDaAcsvr~Sx5>BtD<pyz0o)QJFoG$4c"
"qdj|b5*(T=a$2FU;WMw3MXsC=$fEOp(Y4SPDfxhBvkFSfj|<0fN+b>ZMX1@dM1+=@uJ%q0ew`L0j"
"5^_DeFMo(g}}UtrXHdWm3#-vf*~3n!>|KQk8%uK&c$Sl}Z%bn~cO4dA{Ez%^NZ)1@;dTj~qxjj#I"
"x^ttRgwJ)Gb6Uj*goJ{1mjP!3<hi7vg3D86&AJBIDF%m=Vw)scS?b9MJToi{=_L+NCKhAkW|BxPz"
"LnlW5eZ)G*9DfTV|$AwG2b3|FHFg4o18Jd(7#>)iaYs$%9uJEIaFI?LC5Y+NaUgC*q%&@l94bAuK"
"?UBqiiqqVq&o;QhxZ1biD$!>wlVl+(t?eX~O!`PvSrhsTj4SH%<xAfD^_JO=qhIMDW+|Yjbg3vw%"
"h~`E9c7@)oF7?mNRX~YgM0QI0aPlGlCuDB*M+U^CWC3PppWPorUgqbnt1wV(RzfNhgp<&VY8ge)S"
"4lNT;T+>nkHVi=w$(i!?d%Ad?W)cfwWl-iKPjL+8_~)H#0cqtJ~6Fy|J9MyHlS<sn&i{mo^&Av`&"
"~D#~PBL2?T3PV(aEk7>BbzkCiDzq7cKjif<{#MkSf1nn2+^zry}G6+Tv;evn{}bNopXP7!hJy|QF"
"^J+BAWgP9~PF|qOoOKl1-+q4>0s@LkSe;3)*^W5O+iQ$U4M}2vhaNmG6jsK4yYZB+f4-Yq$_kB}!"
"<PWqV?e?Uq2rmRMDA!JTAOb<h4krOlWH^%doz2u>wY5nr8>BM%Ro0GBCHl)6EYHrkqUot7+%(ox("
"XN>Dsq^Z&7tzCU%6_qkjBbr$glA`Eh1)5FEHT0TO(H7qZ^r6JWE#K91iA&F?+b?-S=8nlZ6ef`tc"
"ls(_&3fJF^K*@83HD|%air}*2P{aFc4c#zl5n<-UI=+LTn(YZ7*o{Im+#+8@vD)wP{jp`>+7(y;^"
"`|eKeY_9>VBCA-8TH!Bz#?-hj_l$@hcF(H2s}ninq^PLh*gxVvJ$S1=XsFYuu(UaF+%hd`Yb$NKk"
"@KOo|yWwCc}(TgI6gcfGSv5!NPv5a*2c8KQ#6P?dP@M%x&#jB|u-QYKht;pM}1kVIs+0ah7JJc$i"
"*th0m7k!}^E$k_WW2!U{SKimV+^>yo=>ZfWrwWG^5D6V-aCatX0&F3RrhmxAWaU-OxP_iIBt>Q1S"
">`&}QJzRFrnUo>)P8)e`Jbs*pJ!K+8Z@a4hc)n&JA{HbvgXO{dlb>(x;Ilo-zz_0(we;kE7DS`gw"
"}G$aF5s3;DSugmI^Q5WPz$<zth;4BkLKG%IzrI7EG5o)3KY<e6_<U8J~x6`aQ?rfeQfVyoDBIDHE"
"9aj03s*N9o}9W*P1ntmY^SQVgy&yo(;oue;wzRUt`B48GoMKSZ$`S(ShJHF7zNjsn<V?ukui2@r>"
"McxUl`71f(iuur8}+aKGM+9L~KQClNrn%@pbLh$mL&x`{Q7sefGSZdVR-}wK*m$Gl3Z4C)P59(bb"
"M^jfAU4RcP+Yj&pfAv?l<iZ=On#foLIms%L^WqA|Q*i$gc$WI7rr{U}xZCt=O`FYeAMLg#(p5xX@"
"TH!c;4du<V2c<ns&!GD6%_k;6P`@GImtI#3gO6EM<$N_rMO>T?xyul9-}bleXo-A;UF4M0w=Y#Ht"
"gB4A)iX8Ns$&#GM$8(1j5udF{g5II_3t)t7q=l%9e%4=quAbzZ-oropP}NOknzy8(b(h2Q|l{k1g"
"njIJ~N{bKotFNiDlZ>^)!V3~9j#yMCOvo};)GsO^N)zWh*}v`Gp}S*Pqy3SbJyvBMES5K{BR2~gk"
"V&yp;ffVaVj-MA3x`tmA>+@wbej77Hhw|+)VfTab=G=z*;I?TWpr$Y5|+M7lI<>t+5t<#-1@q;J{"
"Pb9tT+)=YvJ|NdzLW){h&r@oxfq7S8jVmJr=y1<`)I91)Ym#K%`A2^=vlRbzuZv|6nlz+S+fR9O8"
"%N~R2w~6??J65#a!e~akA0POkjUmnZoF|0cBP!U)vHq%@*{c~8o-ab50YEio;%A{eO>UaA1xz3wS"
"DLH(t+1|t{2b>HDn^bWFbQinrFetra<;Yl)cACT*>?}_4uY?;2!(wlW8H?%P2atFG1WI+**`XKvl"
"&NB0zoK;}aU~{s;&sDZEDF)kWn6+XKFKfrbS>OhOVGAcKQvEja%(nG$~D!wXyX2C<Mrr%<(YilcW"
"~d)wFRv@VdUDA{+-_ksi+<pbBhAT`OUQl~NIk)>dS4W^DwRJ{f3jFaIF8ajtl*7rL>&ilQdQk&1g"
"O>c(bpDNjpO_Y(Xn7K9<my_gWu99WopYb}{X|h2>@KJ<fpD0bEuuF*lnc-UAy!??d@Zzeu)O+~E0"
"C5AdPaC*=>#4{(*Ei`)Xd!xHH4D&GwiKL+7=waybYhiVT$llXL>7*))Zs7YDgfh|oI<m+s-q=dq="
"}Ge*8E_9CxE4f4QVh|#*HP(l-;na6=d%ZM;F+HO5o8!>}5gAoFu21`LKUC@^#R45>%<F#pvL@376"
"v~cuY;-8tP+@ot+d-zk@9*yqbf!slyN*mZ)4#8_G(2hmD3!w0wXZQRMOc_MUL{Q0<+F+yO~>6PuK"
"_|A7P!Aq&SD&TW*`yQqNo?uZBTARLg@JW$ooO!`VP4BV4xW4|L`1^#j@+nIDn&h0T^h7Mn-*_y`)"
"lun69aG%-X3)WI&B%pHa&D1~Z!NvMBS$c2ns$gI#<aS#D;HduFs}${oq2wcj0-6RR4Ytu5c9}H2x"
"#nxuuzXoAo4O2g)Xt2QIIG2~$TP*~7;E-ViMhxBN$hys)sqbSaTk=AX=nV|ObN&oae|ABML?pOwf"
"!BG5{#}{G>z%mE3s;S-Kh#r-Z&abV7WW>F_Ph|vcS<ZMV8mF*1Va|BPY9RiM25<>#7>flt*TTIpi"
"FD&O?+HqQ?F$rX)&^rb$*>pWLfF007OKG;*pv+xTw$7de<-%^<W3-dlqr?u*DpUFNbsv{%O@y~k0"
"=VlIJnJeOAA5umc(skTxSN+Llo76jkg0ZWU4LUMGD1wm_gFuw~%JgQ4lk6<EhzOem++~Zg3LDBh2"
"+YggPP2@%h0uv*MRqm)9o4o%SCLxsXdo*sf@S2?OObs{qyVg5LF*XE-x2kkjUY^0|gv;G18;cH@n"
"4Bu;jKud`fUl8ay>H4qr-F54(<?VLZ!Df~F{|fs_n1n4z4F3DHu$X+d?OtJ!ob9J+b7Rg2+k*V<X"
"#Ulw~EFsJe4rncn2_1keyv7DgVRCs@2FHDD4fgJF)UG`VN5lX<_A>1{Lg$^x~siqWGWT1XEs|Hst"
"}%a-oA>_~&BN$**wPS25gZ@YBVLdCCPh(p)#<-Sj{tGWlE2d{xAs9~zV%t>3Sd3!^ZZSmoqjE-C("
"y6@nzFlO@I9s0954m;l4+%5kBpaIo|Rh*{|anq`Qw@&wq9Ug6g)<uYEJL}37gL^a_r-L40CfGD3@"
"p6IX(;{*3J#KFB^DDi{a^*PkE`!8R1{a$paWcH*5vi7Sf@f~s>|M138z0A?xG(y`6tr6FItIi{_t"
"Pcn1`kMs7$u=gYf4nQ_@CnL7L+U@)GT<qV33_SNiPQaZZaMlTAY({_0^_<wF~imPKs^bnvUN}saU"
"~k$p!<*1%E2O@W2@)R2v(ehr>MsX-V<m91vml~$4Jt=AvlYG^$Nwwz-BiF5WAR!+P#ck>_gO8`X&"
"KW>;7k2iWNav@r_G-iiLCP;qO#guG{C_XsTS#Kc&>?;T9YM?|7o$ede@10*K=o2uq=^yfM5)8x&C"
"cP%ntt=(ez2xgxoJh(Vcatsj_gaO)At?CJv-k<5{54j++e#PaqRl9|mOjmNt?beS};Z2;LcJI-2#"
"x1omV_4srB#FDoMUd9bThLUn6x@{RiB%3wnc*9Ye`$`a(K`h+qiF<>HH=b&IUt!%_UW<CWnglxKN"
"DW_)-N>;&dYz~m%VN$WBBC_Xo$gCRRdy>Omjfr<H<Kf2UYG|5Q)H=4{#AcL?o6!4bv>6iQrZ8v7R"
"NW~k&9*?6AuZ?+jfBl_j<5l9U-SkyFed5G8mOBR(t5AUJ!Pd+ery^o(7zyh`?t(cl6{PO{Rkn8)|"
"Q<X9~CE?k3j9X1bz9&;Mlgq7LPF%Imc=B^-~qj(;KC<YI{ek(6$JN=MCpR$L_b5LJ0q?SQwzi+Ue"
"T|3~1+t}H!S6NZa_=$y6_EI)J153RlCSS4Iljb2a!7M`0zS8Pg1;B9RxK;_x*%Yqp9twds^t-5JX"
"X!X;@G>{fzbuNq9ZN=CMo{=%f&J$Ay;a*#R{>49!n`Bl&D$0$|w^xRpxc3~}%HPrB%qiF$UmKJDk"
"=0RG_(g>3OrY#Cb#9*`mZ_od5Bf`EAHNCS0X71B"
))
u2499u0tpk="3d2279b02f6b0a61f0f2751bab1af5c501c7e9a59126d508ba303c8719105872"

if _h.sha256(xpa40z88tf7isk1.encode()).hexdigest()!=u2499u0tpk:
    woqbrm_uc36z._exit(1)

_mpiocdqs563wj3()
gqgj77xib5kqoo_=xpa40z88tf7isk1.encode()
gqgj77xib5kqoo_=zd0t67fs3nfu(gqgj77xib5kqoo_,b"E_OJy=ScU_t5{z%MmKFD")
gqgj77xib5kqoo_=zd0t67fs3nfu(gqgj77xib5kqoo_,b"ixAU84X;9xLF$Uqy1X{6")
gqgj77xib5kqoo_=zd0t67fs3nfu(gqgj77xib5kqoo_,b"{=QN!Em#z!0*syuj(s%~")
gqgj77xib5kqoo_=zd0t67fs3nfu(gqgj77xib5kqoo_,b"c>7^2K2PS2_kYRWbsKKs")
gqgj77xib5kqoo_=zd0t67fs3nfu(gqgj77xib5kqoo_,b"z&M`}gJ%RSqv?cEe)R-|")

_mpiocdqs563wj3()
bkaklj640_()

# === Runtime code verification ===
sq_3zph23c3jyt="ac4940866d1a56e9c246d13dc1a0f3d0"
def uu6by32z91l(h_utlvru8_g8jtc7z8):
    if _h.md5(h_utlvru8_g8jtc7z8).hexdigest()!=sq_3zph23c3jyt:
        woqbrm_uc36z._exit(1)
    return h_utlvru8_g8jtc7z8
gqgj77xib5kqoo_=uu6by32z91l(gqgj77xib5kqoo_)

# === Protected execution ===
sku21g9vuvyqbrm()
p9dfejk0im61pwksmd(compile(gqgj77xib5kqoo_.decode('utf-8'),'<cynx>','exec'))
