# -*- coding: utf-8 -*-
# Cynx Manager Premium - Developed By Cynx2502 (sieuthicloud247.com)
# Protected source code - Hardened Cross-Version Encrypted v2
# Copyright (c) 2024-2026 Cynx2502. All rights reserved.
# Tampering with this file will cause it to stop working.

import sys as ayd7__o2tc66oy, os as t1lyc2ak_3z4cl

# === Anti-Debug & Anti-Tamper ===
def r807ma9oapqeo():
    try:
        import traceback as _tb
        lmqio4a0xydfhnc = _tb.extract_stack()
        for dcnoyz7a5xn4qw in lmqio4a0xydfhnc:
            emfwo0u0wdqrgwlk_ = str(dcnoyz7a5xn4qw).lower()
            if 'uncompyle' in emfwo0u0wdqrgwlk_ or 'decompile' in emfwo0u0wdqrgwlk_ or 'dis.' in emfwo0u0wdqrgwlk_ or 'pydisasm' in emfwo0u0wdqrgwlk_ or 'pylingual' in emfwo0u0wdqrgwlk_ or 'pycdc' in emfwo0u0wdqrgwlk_:
                t1lyc2ak_3z4cl._exit(1)
    except:
        pass
    try:
        if hasattr(ayd7__o2tc66oy, 'gettrace') and ayd7__o2tc66oy.gettrace() is not None:
            t1lyc2ak_3z4cl._exit(1)
    except:
        pass
    try:
        if hasattr(ayd7__o2tc66oy, 'getprofile') and ayd7__o2tc66oy.getprofile() is not None:
            t1lyc2ak_3z4cl._exit(1)
    except:
        pass
r807ma9oapqeo()

# === Exec Guard: detect exec() hooking/replacement ===
def n0c0b1r6mmt():
    """Verify exec and builtins have not been tampered with."""
    import builtins as sf8y0iyw157c
    q6nstzajhq7mufje6a = getattr(sf8y0iyw157c, 'exec', None)
    if q6nstzajhq7mufje6a is None:
        t1lyc2ak_3z4cl._exit(1)
    # Check exec is the real builtin, not a wrapper
    if hasattr(q6nstzajhq7mufje6a, '__module__') and q6nstzajhq7mufje6a.__module__ not in (None, 'builtins'):
        t1lyc2ak_3z4cl._exit(1)
    # Check if builtins.exec has been replaced
    if type(q6nstzajhq7mufje6a).__name__ != 'builtin_function_or_method':
        t1lyc2ak_3z4cl._exit(1)
    # Check compile hasn't been hooked
    _real_compile = getattr(sf8y0iyw157c, 'compile', None)
    if _real_compile is None or type(_real_compile).__name__ != 'builtin_function_or_method':
        t1lyc2ak_3z4cl._exit(1)
    return q6nstzajhq7mufje6a
ds2zceyz1pxapdj = n0c0b1r6mmt()

# === Frame inspection: detect if running inside hook ===
def lzmewwuqre():
    try:
        import inspect
        for fi in inspect.stack():
            fn = fi.filename.lower() if hasattr(fi, 'filename') else str(fi[1]).lower()
            for bad in ['decode', 'hook', 'intercept', 'dump', 'extract', 'capture', 'inject', 'patch']:
                if bad in fn:
                    t1lyc2ak_3z4cl._exit(1)
    except:
        pass
lzmewwuqre()

import zlib as _z, base64 as _b, hashlib as _h
def sexdipte3zpl2c(vcvzeky95jvh0xwac,i2hw9v0wah_hicn6):
    return bytes(fe0c0y328dci56gsu^i2hw9v0wah_hicn6[kbmh2qvc84%len(i2hw9v0wah_hicn6)] for kbmh2qvc84,fe0c0y328dci56gsu in enumerate(vcvzeky95jvh0xwac))
def ttt1yxjm0nj4j0(vcvzeky95jvh0xwac,i2hw9v0wah_hicn6):
    jfha5mbvdc=_b.b85decode(vcvzeky95jvh0xwac)
    emfwo0u0wdqrgwlk_=sexdipte3zpl2c(jfha5mbvdc,_b.b85decode(i2hw9v0wah_hicn6))
    return _z.decompress(emfwo0u0wdqrgwlk_)

dnyz6dxcvi72="".join((
"T9=}XRxsm1xSJr=Kr#n2C?F-E%gGx9T@S5VpUKR$`0{CDs)WzBJoy%egB1h62^&<jmj<1kPSRre8"
"vQVMd^b-mvXqHvtV~D?eryeLK>BlTT^eS?ZDcO@HXjIgt6q6XQrExAdrW{f84zI*-(8!a@^H=w`Q"
"^RKB2EjY>_d?Ti`J)g8_|JmIwY`!&Q(gM!>sNyg6Z7L6H_E<ed-%}?0CT!Pt8-G5@!sozslB9OgO"
"3AV^U8hz4}G-{)TtpDZ2T(3MjCj0p*_5^LVlhYSGZ>{_{G?Z+3qZ`nz|o<8SO)Rg}st28&z>LZT!"
"<f<r)m?|2N;O^|&QvDWTHQ=an*9w){o7XYN+HHPm?^zUr36trNK_}~X*+{rz4lZ2xbhvegW??`I5"
"P@k9EN#ZCxLRid0)M`~Mb^@tFo|9JEXWzWV$W<qxBrq~7;7_`M*OVOcCtN>EmmA@T)2Z>bN|8FSK"
"C^Jk)X5Ot2^|c23w=b@%zm~_*mmV<{BOvOr?EaHM;`oo2<t%$Vf?zDQ3eTPWRf!6if2g6ATWEwq7"
"KQN@%d}|6%R4!D_VMO`oa#~ipT+4l~8z`ieV;!l_jh7uyUo))D?X5MCJZrzAyGVz>GVTZ*Z8K`uL"
"8gt{NSqZ+0~!6iWo+J3I4g`0>2rd}1J`-*E}xBAHbDi>WRDrsoU28x6P(`C1nRTdBAwtdc=L>?E#"
"|PfR;#d@OK8+DHbszybs<V>LKbyF%kX*<(&}=md^PCS@^xD|=um4>R#Gy+F>q>x40r>@!9Go54EJ"
"{7p!(&zf0^3a!L#xyho_v99QU8xWD-jbxO8{SQT~l(+05K-}B}hv@tBesv%)`7{jLS=sg<iqK?>O"
"0c7psOUy}Mjef(Rh>g;<o4;{r(B%45kq+Yn{--&X{$h)c_(qkC4jp6m2yyraRwwlxRT#KID}PH@j"
"cBWB-CuUx)!tEdnthE06clinUS;{PU2kt;Otl5qu^hPBzNt92?IF4OEnh=GsLkCceY9_D679MhlM"
"Q&5}E42kCI^RPlCRNjKRETq$W{B@Cd67W=9p>gEs47O}iw2*5YjVEu9BTcyN7^I3KN`v<}NND1?j"
"ovn=tn+geRwy97gNj>%@(7q*>>Z_J-CHuqd&aqtOhA_Rc#qxTz#$Vx&PHpl6k4R!w64#aW&%oLj}"
"UuwrkWVY52n+G@JuC>CYg>vnfZzCbUzU}L&o|3#Eh;@5r>?o!H(C_yq3#jFTI4Xs7&qYl=1wcvF$"
"(QIXBF4k|`CCb(#WGd8AZ)9`G34-Uek{zk1Ij7Z$NJWe6mxiFP2<%d7?>7HCL&noR}PGrMU778=I"
"Zz{@sTUN|C9JhpL((0;OYUNbcnOccs2jP^mQD)Sn(LSvt@TEeFO**<`1aS7-4Xs$|_Z$GJhel-gX"
"1@XNO97a1Jm6e8gIH3D0Eyl_E3i$ywL4dytCv9R{dliG{{s*{v@LGw4!OIgBM4i3uR_2o+N1BHmA"
"!oG1~wq|8a{^DnnN`joPp)+EjBFCkFRE!BbuAhHW>3Bw-G%6;CvST4eFkO(Ct3hQ;|N7PF0bf<^7"
"*fCug0d}~XnG4q~;ySpnl{j4b#f4zsy^!fxU2amQR;9T*EW1hYf}?rb7)E>%rj2oe7>xZ7-FNBrg"
"~vJWE7pCBOY^2!z9?fc&<|CMS8NYsa$eo~c2}`q9-6VZloMOIXuS#np;~}RQpn@--DAXHt(rx7T>"
"sqAjN@`)EIz;x`t?QUxnWcZCa4O$c?PC+U?ZL@C6OU_VGpZ^?-cLM8?6;%qv4(IG%pOtLS0m=MgO"
"9o-KWqM>?Qt);j=ngHE&b+2=g4qWPn|M*7JWI=pPI#at<RTkNYc<h53d8Wwrn6M<>&5R8DBHe~3-"
"}S&LGF_UhVaM`UE{UJb(Sp0Kz*Pt&_A>Y4lgbRkR9r~c_JU2FCK9A?J9=M=raOr4ap+KM`>7xni$"
"`_cXu?^+*@>moYcWY{{fME)gtNpZhn&n8KQ{r8Tk&~W&us6l#?ZnHq2h@}HmNg50MQvr&MVZ3nY)"
"dneEJLSKkHF%Mz+0}tJlX#nD)e-@GvjcKk>*u^@o53Mho3q2q!+l07;*ojl{m%k!dajyzr>f$Yx3"
"zu-dqd=|+fhRdfieXv>Vv)<t@y+OJmW+`D%g3eQ1kFu&#>Bh8SU}<Pnsy)wmT6OS}+Q&zmT_(O&4"
"8U5k<7-%A6rJpOqEPc>5|AdGu&(e=?X&o$Q>>{vwuq_$dl4#YjdP*w(2n(`H+s#!EG0hUoYL{fSK"
"WUwQE*9a2mnm?=Xwe7&n^^mFaf&<X+{)tA7Gt>WbfpjxuP9(io$=v~e9>-l{NF(IkYOM71uE^lPt"
"QJQ{JYGSpVzPrQ&dk18Wffdv$$joIW$Z`5N{lCl^x#Vg6?a7k-IQ$6Jg}@-$^qNv+o$pDsIm+}}O"
"ZhjhWt(}4N(Nm-JU~iui&+*$NmI$jS9|K^McX?Bmu_g&G)^+f#(-0_ckyZ)vlnh{SQO**Z?t=Qf<"
"Ad;TVnt^qkc#^{A?C9U&np$?$G9;+v~<g^U=83O=U)d2Yn--iGvhGb|^>y+fTSF5q;r7@tSy`&qV"
"ROSg(eG4ESn`*qaQOf*~M;kh_T=%eiS|>DTMRfE~m7Jv@AO>Wt#W0dFhskJyZ=fKC>*c@Y4Q^PmD"
"6yQl}M-XxV~0e={Ro>FK2^8BTo63;&1)(SwhX^WgnhGGIZY#-17{tv=}#K<#J%4WZpLgW|?3Ls`B"
"ps)|1nwoL+M!AKn+=_@tUYZlfSR%YDw36dE&gmxLEatcWbD8<j^*s+e;4R54IwO$$6m>f!yY%>5y"
"gedM_X-fT#Jhk(H7(T<MBOjKbYR0O=nHo<wB(SWJ+a0!jCkyraA4D8>7ZB%YGlA*Yf1;=Kc`TctJ"
"LjuOAy<-{KgXIzWKSGzZA04`FU3Mr{|y3S^sy8^Frai?lg1zJqf2v5HB#5$@8V)ZzjY3lXm*|a@+"
"GBDu5f~>V$oQuMn~uM=3k%T<~7n`3%~oQU2kookd|%4W%_HX=rg;z5tKgE&;9<R6!g~z~FW-aP){"
"$dc5r)JE>Ise!di*B6BM}i>vqB97~mFes93i=%`A<S-auWLCnA|1Uz=MXsR-Pe%x<Yw_oH&_+QiN"
"?V<g#XaPHy&lhtDs}Na}Nkk*crat-1Yz+~S0dnJ}d)>OVVrr4;+psi*xe9Rbq9HIQ0t4-}2uJfh*"
"BRpzqI-HN9{y_yZ-iV$_#nWIa+d`n-S$77Eh8N7LG3UpCA=4)2Q2c&A9fn|TC$VyPs4yn$onK2NB"
"z-`r*6=?%1{K@dDQKP!m=Uir00`a3@~(Y`yJ}^^R3QMi7>)DaPr!cBhps3Oeis&XOQ$6RKnX%_>R"
"1VnkxTKp`R(NnbYZh`iw#rEb%K+EHNx;auL5G2Nkzneg#P^3{I=nGgidqS1xq7OhT;RFFIz!#`9w"
"?3crlrmT@puzf(@E=XCEL4fuub>u$WyjCuYAz;K1{KEdCJj(=q8r~8-66Asvrea5ghc3gF6nZRyk"
"Mr7JHtYP;xshLpWCvI6R7u|^PuRx+wgz7u2*T2)FsHKNf0&%Mkj&nVO32e9MTzcp2S6PEH6dMdXq"
"EIDhL0)Q1-qs=NMRdP%;~uLg%{c(P@%{hFap^s;2c;dMG+2|lQDe;i*5n0g9dxr({)m24*mL}R_#"
"0!B=p59JNnF|d$n9nZVaA7;<vcgi!3W5T*upg8l(fX1L1f!Pp8gR~LH69v58EMd7VF&s=?9UM61b"
"<OETPK)giVyty+Op#D!g1x`8G<|^SXDA{=G{-y1y@b8u)`kvEf9&dau+lFJA<%O_Pv~{OT;skC=-"
"p%2$V<XND&I)fjwCxAH#U=%}gR%c*B>Sp8i%>a|<?eB?xcN%uH9;PIOFS3Da$cXKo2)5qofuffCW"
"UaX>p*lOesGviec`v24nn_;J7K+~N1py$%2qyC)c*l^3M91i>+UnhGvGnm!f&YAGp;kG6+IsRkbU"
"`~n$Y2;`d(jO}Ti3{=K-H5I4lE^OgKLnU94wc5YRqx|P*yk!1=p=j?!{vQt{2>ljSMUWzp|39fa<"
"Hz@Gl<YWttRolTuuNT!b1@*OO`cr7GrMC*_V#yn|#_M^LV+aQzqnD)yFPrW<$Y5rQmjn9ZgQ0Q-|"
"fIomV78#Ejp>-UHAs)UJ>I(3xGx{!mmd9<%CcX|JJyqVx)o)k<8lGd^y{Bq+VGWFgc0v-}d_-fMK"
";EyA8Js4$O_eLaHK;p-RN?9(fYa@eHu?Z>z)<^ZKX#wCoIgB25@oJY7)*z#Zt19Q#exe#*2WbR@s"
"3ccZ9)~6PLAV6c*qOJC%2wYk$CmPQ1>ZkKgXKu<v)Wr~z5Lb#9$x@8C>{g$HK`itO90%ME*9B}{*"
"77=rTzq-s&w7Nc5*?TeuV4KdAR^-bdgUt(HtIY(z^|$t_K4P<rXeFr?C&sbEQEk<8f1(~_t!~U{+"
"OFnvcD^6%c9J<sByZsiMd{T)yhNHrb%IG#<->LO++*%9j-6eGj|+GLf6fsN|IWw(s|;;@0L@%V$m"
"8NL-^xDe`-3g=au8<t?(p$B`AJGpa(@@Cj(bSMtqgh(Al5o&$2u-FvT+44m<iGUbHqX7KjApLa-p"
"U<t>rF1Q0^wb5snH_2G|dwY{!=`ieb#)iem;{3QX#LJ4Q1H^DUeD?5OgiDfOEaRxg{hFw3v(gc1%"
"*l^O!k3^KL>BNq~a7<HY6sQwn`xYQ)bq{mqYOi$zqtINQbyD2i7MQa&_%QOr8uopij4;zjd?!V-G"
"=1o|ih<|@n})R;qvtmIn{3@wDgxos^%A|(dMKA=;|5L*zf%Egp(NKA&uy8~n<6#i8yOi)V~>nYBn"
"ZG}aH9yjRt@5+ZiD8cfyp$;@U{s?vD@l=E`|S$zdDuQky&#f@Fx|D#|9y;ryb)OAy&?Y5p$`vaJ$"
"3CRRLdJ%x^n}^@*H%IXd#2xv;pW2U%GG0T<Hi8Mp@(zm-;3^vWXcl@3$h$sZf@4Yhm5NiBB`jO5z"
"E`ecqhj(}5zJB2>NQo1XhwzUVwe5hKXM>kOB5wAaI5UIppi?wgahBOv4yDN!MctU}%Sz1_(O`*Vs"
"SIvw<<~!WlspxkDv}o7rb+<b|AuJHlnTJ%}-(zktN};Ou`O$2GzPtyUXO}_E=Ny*5adfc{q^Oa0="
"W8lwS{q_q+7L?%tp^jN8y0KC{zPJ$QI61Ox;&Ywvs#|6la+Hga*2OnB8PMu@L*f*UGMv1H5JdWN="
">)L#)P7LHcmF5`Y(!nl%93c{yKX;omF(ohzA|90qpf;z9udRF!F5fSUjHhII9%aQQeFxEJ%W@P#<"
"tSu!1V-6vJ~N)AxZfJsDSEX>E;2hLi?wYp-8a6E*GRl}V!Ju@k}_Jgw_L*cWYc+4psiMN#NfFk^!"
"a!p%jC$L?4DNdul_X^T8(g!Um|fi^~a;Rm8pJJi-?Uac>+{^|CwxM4=F1vBs-6}9kdKg)Lm-Z5Vz"
"eIDTX<(o102x7fVp^lmTyiysv*y8wBOnO?Y?#em405)a6np1DPTO0`7Xq=l&79c<0PBl3%i|vCmN"
"l2wD?N^3A;L@ma$Y%h<U=lJ9c5<6m)zo|+=FQPh;~gy0C5nj57ib@ou{9`v$H+vdc@CM5Kdt8QLQ"
"*pSe)6VnSa~d52u~-D`BrA-OsVLb6*v3Bv?KC)ny}k{tlIvE`l6i2zZ$;YLk)+vh4pp|4UN$!s@F"
"U!6*uIoAx}#dOkr29GhTC-dkah4`|N7CYe*E1!JwRkz}qS-RUZ0fiUZpv3RKi_4TcFr8H`R4{d_n"
"Y6AFe)or@`_^%;gP@HMs~#|`gPB3SjSfI1NMdle0cp&NXYp|=P%n9LE9{3T+0XD0o@cTE7`G6SIc"
"z#0(yy17?!JS-oYh!VJy<!69z;pqsFs>IWC*kwkdmM6ggr#IbxZvCajfY;V&mjnJ@+q|)UXl8<Fr"
"4MB+Y&R}=bBF~+a>Sn0b2wrR^{~<*DIp9xc{MW-JfBIQ6Dwt#-0wCl^id@M+U%qhrYoz0c-m9cSl"
"u=%uKk^4nB&n|LjJoqi-ER%w@P-*1heq*leo<fUiq|Ov%)HjGv~+3@eM39!uAlmOvFa4s$C!2Bpw"
"S-k}46$u-jA9$T+#aI4IMzZV+}8)Z!hpZ~DDIT=5L5RA8X0AO%Qkdh<EWvLQ^8tIzV+@T7r!i*L|"
"0P=(~FOeXx6x)X5735W)M;jZ%V$#Xu4G7i>2I-TrBu-HeUCtVOhxR+A`2&~L{w6gksc6i+TuDd5|"
"o2^Gfm+wOH-Y{9M`B&x0x1wWI=1|PUI#@K$JbcF}m>zU{Oa(*4^W2FEj$;$7QXu{;u@ssr)J1_)q"
"uNf>Ws7u6K0v-|J5<(7Mp<v8suJVg-X<*5Vm0*3>L!{jR}kt`dMxicNcLb^4zHV#!<G5>ffP4jT-"
"ZX{is>0YPrYau28s8Re)BY2sXg?I<}Sl;K1k1Nn)uKoqWMc~L;gYaNNkbacHN;hR$T~*SBJ5u&#y"
"C~xJ3{9Y85IRO}8yT(S|+d3bept6i~{_>!KG<FZ5jS5afX-SPXyc2r8NgdyNF*q^k%p_eff5${4-"
"F=r(X12w80+rW2+IhFMv6bSk!_Lw(Wvn{*E9rG_58NI8c+8GbWGzn#QzwGJWtj;T7|9KTVf$WY8J"
"!dvb=Gekwa5X1AJD=MRUuSCMd6}KFks>yu4tspFfdbdTm`@h}Vs}Y9uD`tRrl1jidAMfBbs3Ei_9"
"#vwAwevVqLZOoUH1}pk0i`E67l&2}%r@dg0-Rz~k`WS_Vm=lw9DPu#m#l-gk8(pB*EEr-6YW)W*&"
"oIWRQmVpB{z$_FG34`EVeJLRwVnN7~UDBldJzVZ17k6W<bG`7MgIYCGu%qm;ueh6P0bI#(_hwOW?"
"1J`Nv?n&CRU9?J|4s9P&abrB#JHp-I6hq}zg{UwdJNPG-R!1AIqD%J9(zG%C14i7;~Xq<CcB9plA"
"oD>J`~2FMp2=QRWwEXr89jn;%JS}wJdR}7xHu&zdOk?Baa&4oB_d7;b(fbLvxE&r{v`|xve*soC!"
"bAur0niYHiXviMZlHK%%!QzODscF=8CiaLO$tbL}vxijyGVK+nJ0FDZ1M#hdFVg|B*l!3{4;IO+)"
"B23bmB<-m>5vaHbVry{p9_Gg!!KpJ=%k20yg<21$;K>W%m=mWPYn-Bbd;%N*S0{06S7_T??No5#="
"~O9(*{eYC05NN?ks@%n+KX(!(CIi)Hg$Z>0y`Bs6XfDGQL{D&IjiDpmnvoLOsTdPG%-2pQPf?t53"
"QndY|cA8!tTySJxhYuXs1859b}m={F-wUs{W43;^KBah0$@)?)ULLI~U!cWHu~Ob{d34C|58)^)-"
"~0Q8TOvkKAJl9cC|xMu~rhhfBbI73bK(wtE6N&oMcZ^_(oe%yIbnJ+y%i6s0YPM>exhk*>I(F4*U"
"a0tm60BR8?2xc-(=yGYGwDNT($bW3==xBg--Z)3D#7GPSj5cGalh(?;Ro!A8pQWvrBb*7hzWUO9D"
"UL$%)uHSDq?ee|_B7Q$OdTV>I{d>Mn5IT*A+Y|Bb4pA5_u;Z-ly!(*;7Da`aUf#N@M0{+_lU$D)x"
"|!726_Khw>WQh6Wk*#01FlXK0W#=QzE+;m0f0mCH5akUdR<)EG<g+ycHGSQ2e$KezG|Ztc%J~JH<"
"|MH<yQZ>(%SsiCvvF7nE+u#x-+$lb*Hv?*e}flwDyHR7DV{(_HzG>`9p%62LO~J4%;%Suo;US9a3"
"Y<?ctf7hz}6<$=X>=MUg|K$nS6R@gXxA2xQRI}h#Z(R-!R2r*{eIv8*$ihx#Qd=#@hqk&oHZ4|xY"
">0Gr3Q83aIB=`tZAFE_*9zr383`89g*3eY?w5R=Un+2Tm!uts&OOwFlVk}DaaQZCS!rQzaL%7?s@"
"=z}HmUltqzaG9w31o+=0s2oG7)_pH>*<C%7^?>Z_sRVSSw349dG_6G6iCpc(!XUdNHi%~H@ZEb#@"
"--tw7tT>w{(j|WeWYcj@{sXlS3iD;4y5u!&%w@u7C6Hx7t{lTU!(Bh*l<E@F=k5mz)RYWauc8^?|"
"X~b>vsQnr%}%7}{T`$HZT@AYNRTqIQ1Uq=h^=OmH9#b{I^$d02f#qc8ZV`3H8l|8`nCrXe6$#D)>"
"&ccn7;%H&#Eiz!&+^&08!9xeBMk)}?s>{EowNPc!FsY>cUyl}s32*dQG8_Yt&$*F=OnhtT!#6t8%"
"=aU`ZV-t$RpA=;nDxP1~%h70a%$`q74TEqXesG8-?Hu44K${A(A4THBJ&A&BI^k)p$K0E-t{^6_X"
"WtE%S2wog;`K})k9zywmB&;K-@Trw#3JVZ-Rl7DJH^Gj!mCBc(G`rTL^kmPGc`*H#KMXSN=cJzM^"
"Ywp9s>Nejx#Dc89|)gIArX;wLHk^*Nxvy@D(Cw|6^s~ef$m@?OdOrBY0}W792r2-2qFPALd108Ac"
"CMw5#dfWxr+6z`-cw_Luf6OA^qiH9p?u=vRM$CQ$Z288<}YX|)}kt_i-}JWCAZMMO7Kk<8szFYv&"
"5vIzIbSu_+qlx{JPHz)!N7a68I2}|fdryQlmznjf+zIyRKvUX>7M<1iTqj-aoVcLKMNs(-zWy7dY"
"LzF0yQM>;PVzuh1p&ZHs<R5)cvfAu+QVe3x^rZ|>LBGa}gkcLj*b7rxh_WuD(39v?*uT1tPN1+6?"
"d(OK0V@SzRkO;CK8LirP2%7q7%*f)I$~I`S!pkX-eJCbaG=kr60^VP$J2CO;a8xz`I9%4ewmr3Qw"
"R>fz$g!ib^ap&Uv;`Co?7+~ZNA(t4*CNtZW0k^61<#gCzgFD)U?h&UAahY7>rz5q54(@8iF#)=fP"
"~q4CWK-u28J(caRtwK;hUf$CQkQ=qxdGhEEpPs)#ve+Gp>W?~bLoqWZ9W?wte<>(r8d(iy}Xj&XP"
"x1SFGA0F~J0$3kuW%nW#OEHxMM3F+^`9qB+#)1apuawN+#*l46P&UjO)T#ByecO%PD$bDeGzDaVa"
"fDXk>{P_R=3MZqy)`_}~P4o^J8&66_nA?PdZ9+wFZJ<sJfE8Df4yF`kq0pnc<?{7gxx0V&7NuH#j"
"|qeU>=4qO3MI0<Ogmr<ftfISZ7b|u@l2K)uGVu^#}a<dtn0(M54rq(JLNaw%3^6jkBR~!*pl&g0T"
"8cMSukboRRM%zpeTvaWmCERW8oP@+U8Av2}&d7K-X!g>CiFcH&-KRc6SMeV{&uIV9;hdN_umrL=s"
"7q+G}&6!H7WeOb<O$0Qqf4E`10#a^vL_h(1!gEdWJjduW#HGJtoRh2}Q*^y&R0Pwne7Gr0^v(vc6"
"j3DF|mumNZaClw+>zvK!_Vcjb^i66G*b_{j7=)+sB21feSCwT%MV+9O)R`Oblvyd+HPxhS@%n3Cg"
"8jto)UNI?N{ylp*0&tTRwL03R;q~=&VxmwRsjoePyXecR1TXB%-Go?L6kO0)Fc9I#mW8zy1zG>$*"
"L-8Fzh)C?8#7A(n;IfywaXUU;;{Y>qeWHW=0PAy5UGE9j_&hac=GsMSMP-c%Y;b3`*8rq^)whW?!"
"J2L7=W={%%lyIJB<LJZ4gY9c>-RK^<2KfgAL;-2kF6h*qd~zXe$(CQW;AqQ!O$VoaW-EhYQTl(lG"
"6@q}q`~Fx2nYQH1P%g6zI;_hd}>P^H$h5&p4VM%JYtSF&M8de<TVKH}sU(TF{}z;zgF-|Hsme`uu"
"nLY;a25H%a8OjH220YQi4K?MLPv$mPZM!~1HNx#tFSfMXa7sCd=QZP%AN^G8QcKo!R4bz4JoVvb@"
"1J(sk$W*eq(nmSHP4dTjT)bykshJJdn#F6g*m+0OeRom8g#DjShqJ-bXm&sk{OS?gz*nSg8mA2S<"
"F1(3ORz91Sesw$=Xe&gQD!@dO8-jhDK(`#C;@2yi?B310YbDYDrP?WoP+tu+amU&G#E&v!8PX`Y="
"1=vy@384k4Z}r%;HN$x=8-Vt)J_EIg{MugxuYmd<KG}`P=5c)F*#PWDl7K2(($eyyn)xv~|ZNPB!"
"ljd-{pro-rvs*qt+saYQJx(Iqpwwstdl_0CYeN?#2}@OCI7+=GIB#U?>d`9n%IlJkv%`O|Qho^pI"
"K1}r5!$G7FJM0&_L9N6XJ@(dB0p6gK$#+gX?mh=rPZucaJj(99F;ATwmWNtO{%M006j$qQka?d1?"
"VX$s)Y~3rFlD<6L8rppfb#Dw5q@s73TfUS;^=E35Jksz>TIg&afrJ9fX3;^Uz9r~3^VsJ2-TAg^0"
"BS@;)N$)hW=BmjEKcBb%Uu8CIB~(&*&cR~ZWNfye<$V8y%dI)Cbu3o62n@p4H1~1!R_3QE*4L&g1"
"R+B;YXH^cNx|x#+<p9Q1N)YXKwUpB(;By8#K+kYNjDn58`c7Wu7Sv4liFght;qR7+X{@KTdOll}#"
"Q%pbX)R1)LTvo!_{Dm~A0zff-}OEhf<#`e$a&q5#VtT+2e-_=8t<O#{X}FI&~Wc5oMO9xO8$3b-?"
"c<?U}$M)yH%HaB7_Hx4>GJ5&wL2nN^v_*-~`bR2f&g0#)bPxe}R3(EQKQsv|?wL2;JBS?`Wv|`q$"
"_!$_0q(;d?3-403CrlnfQhQDw{l2{LOJLVnnG?&|vZRu7A!y!7Ytf+mB?4GDs%LDMH-ATe*p>p!0"
"#SN0Q<Q?IC-|g`!OYbUJ}M&eo+3>PW9LE^UM7*M^lYSSu&!|%o^VZM5>G67=rFaD<>H?Ir`6X!vV"
"a@#g*yR$p|$L^5g>3g`^!7~niz6F|9rAV%jteIUZx)V=ofT7EXfULTQMjUtQT|7R8pv(w*E6>1QI"
"&8+Mc1rd53G|zi4zB0M4l>Edi>{mTBg>moPE9tUGJ?L|bn}#7iz)^o!nd<1P7M()T~7##IJ;{VZW"
"LT_=KoQBd$!HjFscAHLo9%P1W#?|-pgwU^^n;*zcW;!o+&fvJIQYpR8Z8>)rM>{LwU$5^gM`u4YE"
"C4v`1Fyv)M>8t&$B=3nG_MBz^bGpfx)92)_+xIl?hGllSktaaUQlFn6UR+>}6V~F)pjnJAio#UkD"
"K#DL-g%f~c)J6FcxfA#I9snq<!c~a3r3IrrKPD#?1t*G2B#QjJx|(I*RvNMlW;zW@9(2Xz_a9JHe"
"C6miDrW5YigQRu5McfPe-}=+9SgR-s!vmxvhXbj~z4FmRX6rjvm{s_y*AFlBFC*654}_L>7m`dO7"
")Wb+MZy7R37(4e=yl=`ZsjO36l06&Xr%$X!@^?%<`IiLZd$)9Uk|lg2|r#``o+(|mrgx_#J`@2VP"
"Gq76XlO8b2L?M)vUREDIBkq6U*S~V?M^r#sV&y8rS$U3#P#~FnrHpOqO7P1fqtRW>TR5p-@(Zy#O"
"M41ypfu()6IvR?U^m=|CerGPyFI{V)l^W2T>N`M>B(BfiuACTlTRb;t>}^Tl$sshNBa|0%(b?9Fj"
"_L4A!5)Ly02>?&HCv2s_~YvUI<(G8cE2pDZN{?QWDG#dW3}3+D6Z7n$@Ve{;-(I)kyq%u2b=!{PK"
"s<}F&BwFRPHBY?Zg*4j8sZ~GFY5+a$<jJE7|UpLuI0;*_}~q{imW%`4xonHpJwgpp5F8%8`erNry"
"qG(5bbfM2a&vwgKsUl45q5ju_gVABA%({HHiC2$Ud$Cb)Ep0b;PL_@fg$msYpOU6m{0TDJLCPx;L"
"f5&Vz)^Eq%N^daQpoys12Sa342i?{<gYgiT_6$%I*AjcI`%Z7`{V!?wZ5X)Qqb$#$t2QV5%lPpez"
"+WFUieymXrov<KRT0P9`U5z`>GKwjNna*I-b*93AZ+$|17nhEF_JJ^^N%kN>l|OR<6?^GCZV0kBv"
"C7&@eB<M5E1wKJ&z7h98|(Cz$;}q^+b$f9X_>Zr5jHncGS&xvlK4TaobsTzfV-`TDI28J)o$TCI!"
"d++&m_)*oZRQE#@JnPCI+Bx{A{PMJ9Htt)#8$u!9>s}YJOYkH#{FzaQKU+4|hB3(O&gvW~p;Nli0"
"*SU~vJ0+<FPx&uqHwC7gWvA%xT#vnFF5iLlbQR2MGJaM@|d@kB&AASKqX?O<@o=0ex);3#YejXL6"
"G!oIw_+v6G;;poSR$3={4D<ITGw-hSYx|1;L1RajJSzy5t9@DT=?CzrItQ~85D&sp~PW3bDp3#_J"
"7nvtDJ6Qm$IHp)9QSS!JE?b7fsCjC%w$h78Fv?##KQkdx5-Y1r$_gsvf)Dy$gnCxlhJ{<mMO;=}d"
"KRiG&m@eG4wI7WcPJ6vL7SsvfeaIduQ|_5di%M~NFVjM{BYtgNElr%Jn3JW&Kr4!IGVYp2T?Y0Ip"
"WsAx#c}{YbE)w)}CyBxC{+_c%H21<E-eMR4vXBhQHH5Vz~1!|7U!l>Gk7Szt5C!Iu*xm#+wW^PqZ"
"e;&v|U)3giA^KV=V>Q-hc_=PP$c{GYUpeja4Y!nKTb1W{F1)MS&_Sm^dy0D-P|AL`MTy&e*THajA"
"dQ`K%KQ%sAnvfV5(MU}I3OH1t=Y%DFv{cz8g4p%FvZ!TAX&c_BO;_eWWr2<Edk*b#dY~J8McjJk_"
"(X^K6qhj!`rq3OguZ*36@@kps$!#Vy)EIJgNu1`cKDy~LpS8mKfXcCYjdt8N^`+UTL5-?JeC>RD!"
"}$e>2%W%G#s$qa{|mGp^K8f@m-#~yq`MG?tHmeOah~!&&vHP$ha9H#s515?gr62eF4sl&#Q&|~P1"
"Aqw!D=@LA46hx7`Hyg+JgEg*+oDa0DZQQWS1(CE*#i^&)nxk$R`F`i4-yn{isDt`)XK(`k|o^2nY"
"A+7l&^2YGcx5tCX%a+b=uUi6W;3zi$GXYd}n3*e1NtCRs(ZGp3Dhj~8p(GlZJ@F8Zig{?ADw<j%$"
"XL!6AJQ*>WaYcen+uV?pUPIIL4;*&nrCSzhHOB(gl%x@l=TkD*t(u?xGl(Kj`p#7NE%hhy^S8*7="
"jW$a&J$+-mXTOAFd=u!c?av$)^chb&eJi;R%0m@99R2IZUPQTfk(?CmuS2^}EoNVV_03kkr360K$"
"huESD^?cSqaf<*xB$XY>xMf;t;oz7aBtgmTeVcxal2x{%ma1ztK5Y_|Ge1WfqjSiu`0xi;9d7sdi"
"59j&C#uV41xUHo4-%o2I@GrwQfJ7N_wjC;MPZ@NvbjBX82OL3o?vDC=Jqkkasjso$U`G$0eV?v=t"
"-JWC8!}Gtt}jR6$OCDV;CKnK7KbKn>UDiWNP!que~Q${Np)+{?+@Os;52k)YAo&$nWuGaa0doUBz"
"{Ix?w;3BjqdPU<bZ|H1@lMfQ{!mxP+aB2T}X8O8gC97L#$9&YJ|>xT*%$=_ugNH`TpSE0x)es)Ku"
"=@heW{(8!eBU>!%J^fOnsgxyt?frc#dmy^*9|o7)liKj<iU6|(ybyL=s!h`{cK-WAWSF=L58tJ36"
"$nP3nyPXIQh64lf-`FxzV;^O6OJ^=k&A-voOvx4!oRx&0>_EnRxr7_r_hE}ZghvvTi_?D+4>fEfr"
"ZAKWn>sRO$9?&R*QG6Ii?mHeqN|L@=>^91yC|0CCFqJ?U00ki`>9VBb3kz^urtOx>^$3iS0t<$RB"
"s*72*!vd7q&{m8;_*IQkLHaywBEdTv|8_TmSeVZX(*Xq|z{O4eK|I%5kN26^i+AbgUG0dylaASMw"
"C`<CGLpR?3Z_4w>?teQ}HdA;oiBR&5_Ql!vuB_H)fURqFk!^e#>Bf&MWSZCVbE)0P6>4_NsutOuJ"
")W3_EPV)2{zHJYa3_Pi8*MsZaCr<KL72hl4sQ~<g#6n`U*g&9&4D1Q|m2%5uySfle*MyZc6$;5s_"
"eFegn>?xiH}7HSMr6LHKt$AsijXqY0be_eUD+ZDO@HBR`Qo=qYSb+)t($0V;K=Xl268S1?AV82tS"
"><#$I1xS<^hUQdM)1p;_E%;ayJ%Ski>NK+KKK^2t^*!;o7C`aHl-tP^>TG9r~1+nM!b)*XBej%E?"
"Y^)KU0rsnnLiQZKADTrSFK;@9}h$v$z(K1-yx<{zJcB1{T<bpnTkztp+;@v`e`)M@bSQHQ^8%f0S"
"2UbLhwoTEW9gnVz>`nxfdcPh^BM=wOxU$jq8BqlQUGP%a*c&Fd)LSu+WU{&S$H79K5>a7Hu<Fb1z"
"SfvOnuoS{Q=94g2_s&R`Qx~^X4q2aFJv>YxnyrHPcc)5qK%)R$V{`ik{%@VS1ZfI8Uu~qtx3#Gqq"
"pp27R%<cB9<MnAjoj2Gd+CbGZlXf~<0-;<-egpEwfIG)m9Syh0sqt&edn4MQ0wG{rNRA&ED?x<Cs"
"bfb{{5x}Sgdg7nM7}N38B@<fJSVG0as-wO}W;FBBRZ}8uuc&N12zzd3r(R*)|<wQlUB&#WopFrxg"
"G2KY8*IDD6*o8FSD7eg5j3&|%Hvs1ZQC>oaGfkk!50z+pWQ@Y*NsErdO^7?l&EI;{_wF~RLuya>C"
"x#57N#jjn0DVfnSOm>iYx*KiZ6VzmKrGxTzRy?nB0k}M3{d|$~rwF{|2&su93pdL80LTSS13KzEJ"
"{7R?>HN8xkgTRW5YM2CXbPjX3>Q!2*Ls0s)O%7fjb9UqR81F0kt0QnsDq!R4*pcV6V3~XSO6RQ@K"
"tTF#>A9U+K6A7CL1#1TEdFfa&|emF%tD?|cLGswJQ;!X@iR4m`9HL+8sJ?U`GKbAIiWYFfoO^&7j"
"SZ|u0BC3fH&k2PahohwvYP{MpICV-V9&flgiIG2P{hVFF)rF!O$m3+L`WM1L<GSN_DV#_fqG$trY"
"P~;+8)xZ{<3O$--jjp=p%M6ar_+gajG$>BDzx*;^nsq}5j9%#n-|ecYiyrc9)Q0OolaPGnQC=gm|"
"@J=h)f1c3l3%|6wrJdG(F_FXMDYxNuGKuS4hi5kUsb5apfiA<L7|K{pe+j)BIk(}NBL9!lY84WHE"
"=jM6M=mg~0mk}x+RYl{z6g1Agjo&0N|MjJZ2El6LEjv&N#kNr93uqDOWcl=h{<>g@W6aVQPZmU(v"
"sFSp5Y1X5@4gc8J4(gl+7(Y?9-UCC?HixsT91{=N)v2zH3BfJS%(n%J<z_as|Os_i`FcwlU<Cmn!"
"oTy;nVG>0e>41No52ajNH_aAeX4p$U4a^`31UDk}|mb(z`R_74|yywffx)TtnGE`Rei7W%V3oPOI"
"%397xZ`2p%&n_>FAKLzbE|NlGERpq~KWartcla-*H83o{Oi@^O&(^Zjkq@YJ90X8ef%mI{XrRhAY"
"1u<BeFY#MZ-b;=3+y+3ZTKe>6$y1-)J4h?{>HTZcayz$#zR0#}q%qn&}S(=SIrUvbI5093^ubjFK"
"PIcH>HQ_N$AE=_uEriyL?ykW5zTn+%2uLi?zFwtW^N(;zQsdKc=0BlGE>(Ul6NfcJMwNl_Y@l?S_"
"`9Z;Lt6od)-)+^ZKcW*DO*3BFIyEkZ2ShT1K~ny2TCsq{vRA-IU}lW$?0+Qa;*_qa1db+Y^c3+KR"
"4By=UM0xD4>^e*%iYDM~Yo1wwfW}J!NZ>klbg0Z&RVVBDB({^R3+CON{>F1DH`&oK*5Gqt@i0mR8"
"BR$o@}nctMg;#ltw(kmc%vn!T`>=iFrr3ZHznlWt7HT=R=+X2HD+p%dUrg2Ca(zJr(j3>pJM@i^z"
"~MNaqiC69+GEQ%2J2(j!-${oo?M$Iw1LQR@y;D_OkXhPpxxUsNr>~w0ky0nVFh_*G)KG5Z^=9>l?"
"Oc9J)!C}8;2qB|^$6TlinLF+};;}Lln7Gj?`jX=Vaa+y_e($BGkS#w~nqI?3Uutjumw}(KL6({A3"
"~k@cMVeW)aC--<knAXgHk1&os0>2K!y)}D59mLp;0WlLdOP5a^l?u)bl63nb>K@?n7pZ$G-sVKf~"
"=0fJ!+UGeA5^+79^;>SmTy1$NDmnug<pL68K^&Gs(VTW}#|qjh|`AiXxn-Z}O6UwiFbPk4a5^sLR"
"JY_zM`IY@_SuxG$9&&iT-ZT1QqchT{I7v0$L#hVvrp4cRw#V?~e7&vedxAsUn_$)>ClDBlwMxlk<"
"v;`8a=aCtTE)PE6x;rum0Q|Rlg=Yn7WCA{^G$3i08xb|JOr-F};%>AO;k%Pj7U8?_MY=IO4y%J1U"
"c)qE37tzpG`)BhhplX8llI>B|TV)21xq;dFA$J*qB~l&z*2<1%fMcl=d27Oilz8iON409@0P|Kcv"
"HXM|^>^vPJapVky-6dA!GY4l(Gz@*MQ*QjV4fFawcE%5)7?c}ge|m%69C%nWLUU<F14+vE^(3<2R"
"mDS!aOy~j@-0|+DfCgj~pe67Rx>+zBjT;Aiv1=z?_=tbbBJ5T%v{Gi43gf%S*!JGTrvG8W|ZSWE&"
"OU7Gkj1^gq9fnkLMkFS`MjhC>mPQhS{@1kSCqXojcS7ZDfRGmR)6IY>Bqc<rE<@S;v<)?@Zkg{pg"
"uWwhYj6hX1p)8sdv?49c)IU}*$MyXzGJW$o2Ymrg#W9BePp!3ouZq^lK-Fe~jEO)i<gaebPX-A5s"
"eBM}o>Q6aSDJnz0kmfpr&pR>0`bWQ(2?{6phSou7m8wsCnS8vDOn$K57}Q6%-?;P)He;@T76;wnV"
"_(^IWP-zmIXwP8N!@c2L=;~J<fs#s1C%1@;I4z^wdRNgxYmv-QaY|Iz54jYNM!7-iX!6Fc-tuQ5n"
"8F<m-i2up0`Y?pQSoDOoHgg^O_yppcYCGcp;`ODB+AmqS?b8$&3_0u2i5N*aPVEZyrpZ1q`P-89;"
"`fwRTB%O=NOe?y143fNn#QkvS$+2RJo8FSM&qSUh>Gt!(H$>X0{}Z<F2rdVN?@mT@p1gsdlIC^Yg"
"i1=Qs_A7E|7un^<bK3!iZLF(*Y6$q9`j7aVwIL1@eKW#0|nE`k^;84e&eF+iqej{>N?Si#IakuJN"
"==hjHaj-X56r*V^hMr`xKT<`@d?Js)*QT)ERrogZ|5!m~O2`%a*{2)3s@Z7s)k{QmcI>M7Gw6Uw5"
"8kEZ`GC2)5N9wJm=^>dbo-yjx-ZyS78QpvcVx3<BbN4ZOm<%p@QUZV;d!dRLYkMy(I;JNHPy;(k*"
"8S}F<;O!TUY6YtT6I2Q73h4a!ADZh&vWy(IwM>%U8ll+G9(H(OgF^P;50CPkVwEcx6xv0jjirt+I"
"1K3Ddv2e`kN*Rff!Pq}a!1*e==6^QJ6|V>{c{7Y-o0hJgd8h`TVXb*xU(*!906{^?^TlbLKdgAf)"
"_ue0h_LecFGVNP=AT|58w{#)vU8#@pr%Y(Mz{`UEou^ASP-oSQ2_76v0r?bwW(Jra7$u&<;-cokE"
"FQi&FWMsrH4+H5Q0Q4n7@-B3;d{sdhw}we+x<h;Io|A*@SX;+NT*hxN#bUy1etYNpex`IG5@j65;"
"ps{`a<wmv<*)kv56kUp7ZP`PfZ`FeK3KntgFpfyI{APsgD~dZq^S`ni*SyBWXj{AjjY5-nbO{aP^"
"-HQBJHkxsGRpa{?G|eSzjkuF7r7h&z8GsoE^wEo%QlA%YkSwEEN-a?G%4gRJroA@4Qm)5Vd}nT)e"
"s+3U0t`sn}?NT_D-EXPpeZ)30E7gukdPHIZ#H+k?P?{(nIQXO_i<;Cvs1!N#4FOh;=EaSVxEA3oC"
"swsJ3i`l-0X5R{2w7dJJl1TU*#!N>^vU#9$<K!f(ecd7>0PY)Q7mJ#rJ^DaFs&0x)XH)TSrym(&H"
"oRZ9;0$*actoQQvwwRH`#ztz1@iZ>Qm{u^7pukBRxQJs>{Str`oDxgEw_&~H=#yHpm?Y7BOEDFbe"
"!!HYUY^j5>A771-wg(K*G50+3gfjt!=M=Gd=Ol>)_tK%gv|}ER8jk4M-OdZ-^UUt?`6v_9#(Z8f6"
"9@I<6Uc?q8?ez-zY`DneiCfAd7!g4bqE`gcutBr(Oe29i{1wt}!+xvt00oFvG*IRo|jc{^a-vS+F"
"GA{GC@iS|#<{bQ53&;B@G@@`=G4Eocz@b1DQ$#4CFEPzk|AbjIeCdbiHWb^qe?8%%3$0}-&Be5Qs"
"&+ErzulrD5jfQnp}8z9DgNTU~X#UhLxI-(0wPE1rLAZ4yxzxP~Qkb=rC_CGF2+0(4Y*zUvrc1E-5"
"c`DAP);)B^<Logt9-afN`;<33cYO3`xeo&`?$2JWQ?w-ASyKJtSAn1gk2Y*o&a|pcD1O6o-^u)23"
"r*JGTi9K;85dgV<^)c|b9qFYVB+frdYWUE2qYJw<h8OvF{)kfc^<^1Q{W7=z1{D?or18x#+%{HaG"
"S`u%)UJ{g3kQsg>c^|HGDL$f#Kn@=Px;|#1Hh|C;!Bni2@b7uqsaN#r7G|Vpt~Fx>Wh272@zk@`)"
"^4p6CNxegc8cSw)hk_qe%d!1};ecmnm~N2%|~x>3vwSW?WY7%y$NFQfYlSPA?b6jk9o0ZBSkLXXk"
"s4kdq`m;VFq1()hu1CA-2_+7%|e!6bntxCdhqvJyymlKo{SRf@yyDIa$xb@W};AAlr_E*~CJHXc>"
"UGBP<f=IP2&|~hMrBn0xr=7o^m?1w5m~wzH>KEpiawlbPKA&B996>xUO2UbH`6j<W+Z!%%Qke+uX"
"z|?e=L24zQB32TW5Z%M<Kt2@^3Wn;yL=O<-U>6eu}`x8_0h_|%3aeEpwDvMxcf|Jo$UkVKV_yL4)"
"WxgFCV)mDX<twezh+;72<RYTylND8Y_#WQ5>7niJ+En8ijmSPxDTDM|&JrH*G2Boj~Z&*wpkC$Hv"
"J?0H(bBvEa!n_iY5Kn%TMdEA;o@hqqY3IRurkf|0@Wbynw822jr+F6!Qv1gpfRYKxiB(3SC|sv_g"
"{9Y%8DjQ3C$^P2VRIjU=XGDENway03u<NDb^RU(NyFdV15i5yjJ@+2vj3X1qsXf2abeV|G_xN6Yo"
"a!1a>l^&8j*^lT;iHr88j{5R*mW*7nw$Dv#UeH1!399u`2kE3N>uyjMP`$37$#KDB)2c=eDkXD}i"
"r<Ep>J-{CnrecyL;t^{EpG7ZIuIr^!ox12<?|@DbuSjUh06QBfpk#tP$qK1lQJ0jtG7)MgISM@{3"
"`JmwfJP)U0cegEkVEJQw>AB-Iw8X#2`j`V0J-0w%}<P^(%481_~-WxOXC-m{Mg0!9bjOHWTW2lls"
")74(l?G8y$i_@*o(V%*#)XPD}X8j<q6?57c+2nyxJfMq*k!<%>Z<Z=!5&1UF{@n=0>||I7`Z>kem"
"c{{k;Qh#-ul68A3UlG~xo1niz}7UlWd`bJX#%o;K<i&#8tZtlUe{Y&!;o3mt`L)@!vq0aKoHLDyq"
"jFNfnecn$rvM#<_zvk}l;cd2@nq0yBy(-3o1HvnUGH7OhYRuoS;47c2Yukk~X4Z;I^{&6n+h+Z5`"
"|OZ@(&>1{@sp*W`?Y3ZL&kWe-tYUg8h+B(@SV&oY=Xwdeqr2L#uDbHiUQ5U1Y-a17t?5#r8y{0MA"
"MZt^UiV3OyUaOC3O=dl*@hx*F0#GSoJeNL9+R;|Chpz>T*z%pxc)wT4V=HN=I};70a$C!PSnHN@k"
"EIVrFCx0&<$b%HVut?M$P^xYBKXdHQgTmG=z5g6Df`oV_~GYpeQ#h)Iw_r(mewwd@btyJpk@8=I_"
"(u>piKS$nz0Z5a7J30mggwdM0Tv}=$dWPe?>n&&y@g|Z~Cm#+~{TU)OG8!iV2{te*&e5KEBg-Z0g"
"$%Vr;A+L@6lXRd?LDfinY$g)y7<V`P2~q-x(m-gqSO2tX4a5%rz-WPc7%yNkCAaa~Wyz!kLH#hw="
"FizOm{Sw)D|v3u>I0IU-9Orm5w(Izjk~wGC4nbM*2D0|)2^<ysbO4q{=p3lo9JF2$68!J|9^%#Hq"
"!QwE@a>o=qwxxbZf7r!vo2FVicZ;u!8ct6>$80zd69Vaw2<?Ss|cj45@v_<6yDDKBok_m1-T(Tc="
"LwmH@gyY>Ua^Zi2XF556&^hV4mwOxU{nAKEP%3|TFoSeQ}p12BdFuJphfO>)gJ4W>R6OS_f7jkV#"
"d(kZ@bIj&jCMbC?Euz^;dw7IY%+5zw?KI1pXNQ-MLmdQRuC{b?YG{E*MKozb71?`VvoG#vb$G2)("
">xwiG6Rl0lJqFbpn7a8;DBMNjffg3|G?%J!1%_Lv?N(KbM%}53nqgf?_8s*`hc>KA`yfY1PAd8sx"
"b8A+ha5*{SKnWeHKjnDxTE!FmHy_ikSi=$uQzL1D=9<sEyr0o*YEcJjiB)P`O!3Mk|LS-8B8$mH)"
"=SL`_b%dqmGKZG=Uwzaf|q^4c9>b&xn#JB$$mK!dA%2+QdY{+ZE&3(G_)miwe<kaL6CG)0-V$7a|"
"%<hTLtml>3U|zA#}X>zw3%HU#n|6&0s*-Mc^?>VVde_|tzk-r_<FybUeDJ}72(4b3z<Y+R$`Ebnd"
"j&VruSo1n;;))X>^bo%2u=#gfUFOPg}o=Y<5jLni6B8ScJC3~D)Vx}{U5vgge+4@W|Z~FRyJ>e|e"
"p^atCl&RbmxtQZgsql8TA4UCV{nCpH|B{)u7|EksGgn$h+Cy|1%k?M!-AJK{m$><YhE+H&>OeG@w"
"n{WlX^(%%%Z1O9?V*9GC|iTpA#1J{_0pe<+tm=aF5XvTJ@S$c05<VY7hx16^(I`(k)%TfHfHMEWu"
"0@0qeoY^S_64nU5y#zT&z7F>{i@Rdqh3a#~qcY&EG)Jhk2v0^nFN`BCoX)|L94;G~P0`$FmY_O?n"
"BQCO%{eTcuuz2=R})TJEIwIi%OLV`28{9C09t7NgH?rX9X80;=vX>>P`0Rlc5L?w7d6iW7@N?Kg`"
"-_`Tvig7)IE!!~;BV~L@3zU~>7^>NPyf1=W_*Ks(+T!{0aFMrcmH+m8<Z}?w)biXS`g)yYNK_7q>"
"=DkD06U3^R_p>q9NZdQ-Aq~7)^Pu{&{q1g8WyM%ULeOt3>fX+V++@{|W!>EoD>QVPJX@zvFg2(4D"
"oS<Qg7hX^z7(D6jy>BB-@GI{6o>(8^6AP*lw`l|oNmA>uj^B__T<I760$Pz<%ppph|i6zy4R#&F+"
"&CB&{gc&14Ep%bg5}LnvQ&xjk_ebIB45;VafcFo>0}`HF{5f6_68Z*QrpN3^TzekGmYow+<25!j~"
"sm<a?VZu1qCth?Ie#l7Sfh_rcy{nitF~FdsuzXht9&OP!~}8b3$w4H#J`+V;F2d0TI(7<2tX_Q(!"
"?$mK+9*hTJN=kngXJ(+QE5hkrKsA1H3O>ld;Mp`Ob=b)pVphXh;me*~}*d!Q)a}r=@@hoQ*o6vqX"
"e~ru&`q@J9HT%ax8$2F$C!_VBDFu)jdiK@GeQ#s1?mNW>?D5Pri*+<@d)0ZtG0Q4Y4^Wa$>$Zz-+"
"szYp%{iZ69kBPO9h(z@L(&^~uCRhHb8E0Px{EB~;}d@)520seJ(UTVH^k+U{}f*L0PUJ!HNb2D{8"
"s+@W!u54PZ-6nk*^LLU>x8#bXrQ`H6nv-{B03XKkdKUi)nRbPvMNgbg8^(GlvObh9fE<SYvGBWg9"
"vo=!E;p1{flc+2fDS+A;}tKeoDY6|*sJH>cBaW#zGii4e1JtdFZ@)u!cY!Xp<@(&_)o`=5HLgR&A"
"KKAyZT`6~C$>pnP{La<A&UdT5#9Hk+CC;Hb<0S-kF9+!h@$>(y0ulOF>!-!XG#aE^}4{|xhWzeEC"
">7oo+{+#toGr0S8*A1+Qz^HyKo2I|=usHhm>JZNod(@3pnMqzDs65*i3NV}5E_ye3CRoR7qN@2l_"
"|c?MFGex5S0xxW4Qu|-dNCj*|I&F`Jg2+g1c6JDQ_PO20lqOAKo|KBivoDp5(LZEFf*&HW+)@jbS"
"suqELi9=2ASjwqJ%JFa`s>K*ClB+pE<!HAJ~hE?`=Qw?Sc}%66bx<l2CT;o!jEIvAMzBLGC{Xa)W"
"Cse$OzdM`?orMVI^0xBbvw%lo%XG9b_Qy#&rlB<8P!kFxP-WNx)`)T#rL3t_Vvc`tmT!EWO?AS9w"
"YXJN{KuBr8?cvg0stoiWH?ooMk2NZ(S-OpLL&5$?J&OzXtRC^+WTgN^`CPb^U*_)W`Ebwh_!*pZ&"
"oOAURw&nEZKk`wdn+=#WT+oY^Nx_Sj)FtcCAD5PodG@O=#4c_&a=PB#WL=<~aqes<1A)=E78)^6c"
"Vz0Nq|L2uwu6j%O-gxbdU%ccPQDDqmhhS38L>m#-lt~G)n<ynks_ZAmwll1+^lxM&H@pFXuQ9c-r"
"cqF&K+$1gSgz_H>h#joc!*O^b#px^PCaI`ef;AH(1?Q#Oerp#I-li5`#7tT_?r!?^k}g?IW=Kap2"
"<B>mk?`sDEn6%{jYkz++hb+hW{_Ylk2pDR5XLgl8m3zV{T*DADWVw{()<Fg*4=cDp<5oi1XQ(4(x"
"ZsG{fhMb+%q$&}EZOG0%TC_JXB2t4$A@);&o`Yst8`PG)?8#HEhuf{(f$HB^X*%2@78^?hXm-Fwu"
"B(Pzxh4Y!@R{fBtQ`%k"
))
d1ffqspfadae_hbu="c7da49f735784605742851c3dcd56a928a7dbd71254017aac204f689415182df"

if _h.sha256(dnyz6dxcvi72.encode()).hexdigest()!=d1ffqspfadae_hbu:
    t1lyc2ak_3z4cl._exit(1)

r807ma9oapqeo()
ah3v1zq8q9cn7_uzqo=dnyz6dxcvi72.encode()
ah3v1zq8q9cn7_uzqo=ttt1yxjm0nj4j0(ah3v1zq8q9cn7_uzqo,b"B2BgxufkG6pdOD91fiW(")
ah3v1zq8q9cn7_uzqo=ttt1yxjm0nj4j0(ah3v1zq8q9cn7_uzqo,b"GN6JG1S`-q&iS2?aC5BV")
ah3v1zq8q9cn7_uzqo=ttt1yxjm0nj4j0(ah3v1zq8q9cn7_uzqo,b"O&E_E<O_?ZFo1VG;(x4!")
ah3v1zq8q9cn7_uzqo=ttt1yxjm0nj4j0(ah3v1zq8q9cn7_uzqo,b"pMGfDT%nCg^9N%QR;9D(")
ah3v1zq8q9cn7_uzqo=ttt1yxjm0nj4j0(ah3v1zq8q9cn7_uzqo,b"St+L+@%g9_cV9`_+4YS1")

r807ma9oapqeo()
n0c0b1r6mmt()

# === Runtime code verification ===
y4zgo3iys9="c57b169af8b87551b4fd385e59003e6f"
def m02wlxay1u9d(vcvzeky95jvh0xwac):
    if _h.md5(vcvzeky95jvh0xwac).hexdigest()!=y4zgo3iys9:
        t1lyc2ak_3z4cl._exit(1)
    return vcvzeky95jvh0xwac
ah3v1zq8q9cn7_uzqo=m02wlxay1u9d(ah3v1zq8q9cn7_uzqo)

# === Protected execution ===
lzmewwuqre()
ds2zceyz1pxapdj(compile(ah3v1zq8q9cn7_uzqo.decode('utf-8'),'<cynx>','exec'))
