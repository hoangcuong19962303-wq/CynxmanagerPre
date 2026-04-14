# -*- coding: utf-8 -*-
# Cynx Manager Premium - Developed By Cynx2502 (sieuthicloud247.com)
# Protected source code - Hardened Cross-Version Encrypted v2
# Copyright (c) 2024-2026 Cynx2502. All rights reserved.
# Tampering with this file will cause it to stop working.

import sys as _qmold83baxqbf31, os as fdcqhyx6e6jp59kjm

# === Anti-Debug & Anti-Tamper ===
def pkc5rqys1b3y4_rzq():
    try:
        import traceback as _tb
        w6vz4iz9aw = _tb.extract_stack()
        for b_6sn9um50tlv4el06 in w6vz4iz9aw:
            __hg156u97x2 = str(b_6sn9um50tlv4el06).lower()
            if 'uncompyle' in __hg156u97x2 or 'decompile' in __hg156u97x2 or 'dis.' in __hg156u97x2 or 'pydisasm' in __hg156u97x2 or 'pylingual' in __hg156u97x2 or 'pycdc' in __hg156u97x2:
                fdcqhyx6e6jp59kjm._exit(1)
    except:
        pass
    try:
        if hasattr(_qmold83baxqbf31, 'gettrace') and _qmold83baxqbf31.gettrace() is not None:
            fdcqhyx6e6jp59kjm._exit(1)
    except:
        pass
    try:
        if hasattr(_qmold83baxqbf31, 'getprofile') and _qmold83baxqbf31.getprofile() is not None:
            fdcqhyx6e6jp59kjm._exit(1)
    except:
        pass
pkc5rqys1b3y4_rzq()

# === Exec Guard: detect exec() hooking/replacement ===
def e2s0aqkp945128z():
    """Verify exec and builtins have not been tampered with."""
    import builtins as _sd8lfqrjlagk4k
    rit_m2v5kuuf4d = getattr(_sd8lfqrjlagk4k, 'exec', None)
    if rit_m2v5kuuf4d is None:
        fdcqhyx6e6jp59kjm._exit(1)
    # Check exec is the real builtin, not a wrapper
    if hasattr(rit_m2v5kuuf4d, '__module__') and rit_m2v5kuuf4d.__module__ not in (None, 'builtins'):
        fdcqhyx6e6jp59kjm._exit(1)
    # Check if builtins.exec has been replaced
    if type(rit_m2v5kuuf4d).__name__ != 'builtin_function_or_method':
        fdcqhyx6e6jp59kjm._exit(1)
    # Check compile hasn't been hooked
    _real_compile = getattr(_sd8lfqrjlagk4k, 'compile', None)
    if _real_compile is None or type(_real_compile).__name__ != 'builtin_function_or_method':
        fdcqhyx6e6jp59kjm._exit(1)
    return rit_m2v5kuuf4d
wdjbsis9ro6kgm3i = e2s0aqkp945128z()

# === Frame inspection: detect if running inside hook ===
def xbx6eeqzji0l2rola():
    try:
        import inspect
        for fi in inspect.stack():
            fn = fi.filename.lower() if hasattr(fi, 'filename') else str(fi[1]).lower()
            for bad in ['decode', 'hook', 'intercept', 'dump', 'extract', 'capture', 'inject', 'patch']:
                if bad in fn:
                    fdcqhyx6e6jp59kjm._exit(1)
    except:
        pass
xbx6eeqzji0l2rola()

import zlib as _z, base64 as _b, hashlib as _h
def t16fqcra03ey2i0j(u8k0bthbybm2,pvsaryi_xd):
    return bytes(wo58wpp_ak1k8^pvsaryi_xd[muz97v9dzxds3o0%len(pvsaryi_xd)] for muz97v9dzxds3o0,wo58wpp_ak1k8 in enumerate(u8k0bthbybm2))
def gpjomft37c(u8k0bthbybm2,pvsaryi_xd):
    y5_wyjluaesn=_b.b85decode(u8k0bthbybm2)
    __hg156u97x2=t16fqcra03ey2i0j(y5_wyjluaesn,_b.b85decode(pvsaryi_xd))
    return _z.decompress(__hg156u97x2)

ruik9f96qfv2iu="".join((
"WeI<~5dNR(%xA|?_E1AcS&D6D5Iq0DAi&{K_Xmx7VknTGX0(jw2sXjRSckyFHNheBu6~?rISq=0z"
"Rvb5%N-^e901NVmDdgJj;2{}#uyxt;_QUTk_<g2DY<G?212E%VMhSKNHsqJrHvpyTJyiO(%x9Jah"
"?SMjAqiB8g7`<kWnE%?|vpURYA%}jA2`vVkH~y0x^Dl*i!-&%zPbu$yrBOH7f03NH~Ip6Xw$JmAQ"
"dh#V8@cd;U^Ou#F(U3wxx*%$)*R$<ph)QoLOjtAw`a2a1WeKNLPKqoqoRDH|@{?sT<`@?`g4B}5&"
"YOD_GHButG2QhiCVN2!=ru!o3DL7Q7eCN{C1)-E>!QC;+YT^G|<FjbNroW45f<dx1UBAE!$3BRwr"
"gex+7u%;aD=Er>}qgy#0Ksms8MdE4KX9M~wvc`g_*X#$O7Mj;!HdFmoz_AKyk!bt^WeELLDbsw0-"
"Zi(%Qm;$YN@Ozg(^W2{=bnLFywKx2<!m@-!r*$t46-fu+izpPx+rpsZL`lK9Rp<^HRc3$zkffj%T"
"X{b$UNZw45~5>^Y@ynflgP$?*9ErB|bJ==ItLe!~FwT_8?2HX9c#7wRp0~1+^1`7EWzqxr1JZ90`"
"6@#{ey-6Qm$dtln)r1%dK5OKM_1<zz!$`DehIF*Fu~7#7wj{^w9XYl8u9=OB~190b;J{q>cd8F}P"
"b3WUtgC1lxxU=&FTkQjQ8AC_mh=}~J`=bC|Sz{I#TDVBCR(RaZ~Z9pt6J8t(J_Lu(UTFEG9%Fv()"
"+@`5#b9MBW=EKLU{!pwNYA?(HtvjsGjp|jTpgHdlBFUn>!Iw62Y~6hTTR8=@?z@@*i&nCWvJ&QML"
"=AS;W(Tzcks?!NtbEpnfXbrQJt8o+2QyBNr1z3>Hge{})+Ml*>v_<21k72z5tSCai<3rO`qm=B4{"
"a+uIGdtO2tRW$Dl!(vr{*pc(&z#DBqcS^ZA(Las)aLZO;{YJj6}|>r8ipopiA>#7>F+`34hUgLZt"
"pc3U9x{W`~wkU^=qOj_Vm#mt;*9IlI$!)B9HODEdJ+@}HLmnsQ=+q7ku!Vzu7CJW)cRWMh_B`kVs"
";%Ckoq9Jh}Tdhg-xWfxA~uhw6#=eI)Ip*RJGG%Y%w6ppGkOn-EpKVlF@Chb6}Pc}>5U${RK+?QM{"
"F5*K^;304~qDW;T69y)Twz5UxPIC4!H-lxm2D^)8I~*=5&DKBg-HYSB{Q0BDz;&<1(+nH49~_8u2"
"}UQ+(fy<hrLwR$Zd<fo7@*&<HJph-<Z(P|BcVGogf=mcgSTi?pyiSx)oRcsKeAl{dI1IxlIHLC=m"
"nav&5Hh!nQZnqN9zwjvs)XQwC{JE!97R{wVc2YJTg?NOlLIx%Z&A-;!imOfhF{>su+8lgYxE>knx"
"2h&nd>T-j7D_4bX(<*&0NKe@;N#;%;sK!=Eg}86IyK@7Hu5w2fbC*)jXFfFz7<uX{G8Y(68Hslah"
")oKyGzQB}hl2kM;*wz&Uo^;#_pF&GaN84PQPV^1<XE~b_+Juy2rSThyT4awUv#v=#6)!_Zk5wQZC"
"a|)zZ$U@9p^~q%^V!KuoZ=@7l<ASoi)=^@zp>QS!%gX>Z0}>8<_IY@-sWIaPYphFZ;+}A9We^-HA"
"qEF8)}WpN86&^V*+5@>$#pud^-(p6BGIp$#|EVRxftYJ%`a+H{b~5w-+T41$YA7~?1m7DB~0TpK_"
"Xbi!%!1C9wBBS`L{+VOuKaa0fh$tx7zn+9@(1@qAynWWT}TzD@z|KvCJd&p#^VlVs=G*vd^Jg@2J"
"70jBrvVpAJU6=FJ^KGI;U@GQ?_=RyF~P2rf?J@L=N-%yK(qad!F7gL;)T+ijsIA0NCwgn@EY)V~t"
"=3_h2*5*HPt=P(A=*m%k+kc^w~nx-9~g9y$?bQMN|u9pYs{~k)k*_y{#Nb6%Rt~oi=HhGB1kppO2"
"2;LQltx9%Ucer6+(9cnt<RZ&TDJAe00an9>(a2{MLCQn_nKqWK362w}Y|i?LBoEjU$@-Q?e-`Lbr"
"I6K~+DTQC4S={NfnaGMNpQj)zn(s^B;EHjK!*MqXZ|Q;PrQ(pG|K44cQ@B-;AXK3J26;{{$M;Ztw"
"B2~kU`4-Pdv`QHOLWidaA5|F%Rund~-Ca!d=Yg8fH<Pbt9i<Nq^4k_l@@)sBq*of%i(WZ|a}OXQs"
"-@|KCM1<eb7o%D(EIyRHCyXuIZb*ec0c+(eVuqA&P3&TMC3#VE%QLEi}dA^ExX1KW!N4}v(d_RNH"
"iOrdJ4-LQ3%NuabTy%6Dq5oYq?qgX2L2puk!6X39dTwd^|Yb^Y;%lWK;YjCIy6YV@Q?|^tR$CG&1"
"Qy=xB%EQX9tJYs!;+9bBUXK3jpXZ*2n~Zn@Nw#Fp8&Q;2Cr?H5M}VO%1w{0VHtqTc7b3TMpxIq1H"
"2nXatB3YPKi=oC?~+L%?q@38vpA%I9pME>^m#qr04-4VozV&zL?Xs8&3;`y?PayuYrJEJ%Dyq+{c"
"Wbi$I748E7T!&nLSh102Ro8<P){1wPc1M%!A@+00m3QDGAG`kS{p?f#qa!IVks3kM_z&V#$wsdBf"
"4fx^I^liP8!$3aY9ctFGzmZ%a9pVP&T^VqQC$nXciy|K+giKy5{?q%i-&2ty;)S%4idnl2JJ=~ae"
"38%V(59ko>>&Hyq{i@KeBc0=>p@0=7y3I2r8_=nx`A75#8XzAsSe1l5IZkFdsw0joA9|`yzNj;)b"
"4Ma_lBKo&QaVw#Tn60~>#%~9ezJOe?QZU`?NTDENAhAJXm0A6gt4g}>FtV0t$93&q#8;ne>=~U4&"
"j97V_I@2=l}g>)?uWYnh%V*(3`mGaC^q4fS2!A|lp39bwWOX6Tg6De5Tw;!Ht|=iiz3$$LE*@Mkh"
"^)rQ3qrh3L4%^$XaREc>v<NB81#!RMqB%eeSJUjty01QoEv%p5e@PbD;$D@H<69Gzme|jp0oFzea"
"n}GpiMM(=><`4YXC{aNW_dqQpt_CipH3bi|<Liu1sC0Nccaiy!+<U?pDl69ZrQN%Soccn0!?#Fw+"
"ITB&U~>XUSgYc>~FzG>^$GgQ#uWgCNPc$QSrU#+at_^Q%6%5T2-OxGbEE*N<~|JOQ=ZB}x<0dnRn"
"A&%$JnmTx_G7~Kg2~<wD&$Q9>DNl7?a~V#;mkyn7^yk{mE?2VIG_fL*IwOf6(@#>=EAX58L_IHl{"
"MmGIO&ORWb9-V)HrlaFM@kFz#I*Z=f_Ln}DY8=;(2&mag-D;kx}speTsl~;#XEOCL#@1h?Bw3R5G"
"o_#X!YzdtCYhh7!T!krDEu@+LcFj_LX<6M6%_*gs@GOe{3Xq6E1xRQqeD7Uw_m+8$ku9l2T4?qQV"
"eIb<X!WFYhX$^Bll|nxtC_{zOn_lJ8`@L&?@r8>qxiYbRkWjtNQTaqXl$%E4IKF8~(a1cs6Q%@>+"
"q=ObR464bTuFq#sRG=8LuvDJ_xFISAmInbazq@N6hUX@bDtk-^a)41WwgH(?JvQ?{_;<>}&%hL|3"
">FKRFiHs+fD^nmf0cP1*5h4J6WD;pY{p)KYrjCKo)dUq;S~7(a;U52{0-!7<)(lXM8vYLWFrHnNa"
"&kji`ZwVbe>KAM2#+u-g_UcnpfA0-@-iTf(roQ2V|>NfC&8{!00(G1tluT^C@#d@#&o<D+GE3FT6"
"ApOC2~f%w8)ZN++RxDaA{v(54Z0Z$nd}H`EZpZ?lIiu*!Jl7r03T5tMl#5pQC2Iuq+WD(D-_6X2$"
"IK>A&7IX$1@8%C=-$zTyaXgMaSh;6F0_Us`6%ZD0W{;SpU@$*VrUscI*=nMloUu&Aa95<q#L1zla"
"`E}2?I4w2l3vVcVl&g8p0*P9G__@Xnt!sRdMGB|weo~rfUrxfUfpNE2~$tY;G#4uURgVW7pK$&0|"
"V3xUuC1IH9ZH3^j21jxfNSx)m8nDC4D;jJV>ar#rjjDqnxRCw`+HvOVQ1zZxeQBjF_Q@^uRyh*!J"
"Ng`2{jhdWNcJnytDLkNM{z&GMG3K7TEzS#3n+6UuZFH-$4@r|^hUhemIp?PBx*psSF16Xr^}qcgZ"
"HijVLLM$pBa&wzOrLwG@wBQsbfY_F*b$X!+}qK?LJ)R6yQ^yz=YOCa`0J48dLZ7`0!JacekY*mwG"
"yaY?NVmu(HG5qepBb@n8xuLxkrdjai6@vPe+1h=L7Iy4q0+PAWDo8cU=}tT^3z<8n*Bt2l8*&(zg"
"u6%;rc-_|)H3Y}w>vmzQE>z0xgb{YIwI4-ixjiZlmg&?<vrHsNUE{n#l>P-=Upwo(;GkUv3cHXrw"
"Cvrs{@`LsCI%%H67d((CjeW}m%_n~D*Ltf~DocUAqHd38jLG%2h_lJ8`dl>~uC75#!s;UoAr_2t0"
"no&daRvWfcrr_5{+Y3DBPMcGnz9bMwzSeB;sMh9Rlp+f0Kw>_QE`J#ZS1Sr)qBL)GIsp$9Tmkn@s"
"lF7axA7NAiU^ec-~LI6>KeNqrG}+<LD>cyL^%n`5Qu|ejXP`BSF&$=qA)bCLE!mKQ~NY4wfJ|OWG"
"h<qnu^vnW!ogZ0#Dl4=-+$hM93HGd765LN~Tl4wW@6(o7C@Czo_Or=%6Gf0HLr=4SWXr9d(5^RXV"
"!%*vx|gNtEL*?a7cnNpCBG@+uJivzFfZUF5fus}3*>N@0fVu4FTa=RBSv+t9|ipiwHyp}%B=SHq_"
"oYE1WVUX*=F{4gB@O6T8^KQN-_TSJ~?vui!8`84~=tgqytfFGrOVZ#1*6xbCwWJPn>9$mlUlZ+=a"
"dF(sD&VuPRWeba7-9|CnkF_yr|3#dHj4y>9qA-7LOyg66;t;3bPwTzA*@}_pgSmiW8BZKOo{MeKs"
"b#mE!9imP#6TnrjQ?0vpl@U@Gdl33=$qcrm~<QrQ3S-HK_Bm>Vr}88H2LKa-myy$-Z#6!)QtyO*M"
"KB=7nS4a5ykiD#a6a(UE}XZR8Cp!S?+FKP=JlSQk%^QmRg?(xa#dMK^In1bG{yS_l_bsPCaWOc=P"
"8dK1q!gFtxk2zt!tna>Zwr8$72SrQbv&Ja+F(ZjUo$@7&6wI&O-CC;$R#DgyM)Jt)_y?qiOK4&k7"
"kwBitu4Kqk=C-?2z+~mrB6Nbf*Bc^^Z1cXJv8c}V$P8Mxjf#gdLt8CEBJLTp2N?-jLoJfLsf`w~="
"-yt7U$Fm|yH!wCW2MrafT9oI$!!*sM;^xIe-(Qjg~p=eQ$EQJs>Tt$Xx2?Fb)O3Qu;j<j_3DiGtN"
"XJU#Ie%pZ2dTZ?1LVUtk@<d(BhC3Zi3aPLTn$@aBMI$-xz*%oT}CsMgs`VTiXr*YcI@PVXnBLfQx"
"|LrklW!aORxzEV}!T1n7&3-%qmsPw26A?sk<R@T>g2OZ-JMYMgC=*<va*G~I5~o2P9J?VBhc?=JD"
"D<y*U*?@0~KSP^wUV^vJ!fXto&;w3{uj<rv<Ikr;we+4}xjF$(Lp`vejBy4%!z{nV3_~u)zr6!|^"
"dG}-g11V0r%~)y$<QLw|;mc86TA7zNdBqTu`pkm-e#YFd1J>do00_5ZVojTyGW_iH`f+$u7oxcn&"
"4JSZ-WA^6ZdKNJ!giNK?lVS*-eeWfz?C5n4t`9J*jEe9Zt&FEU#ejp>{4dk%G%0r4o`j>pwY-w`H"
"QM1dRV(*UVe2na1xPZFAVWyq+A1HY&dj`x$1G{TW0q<#gGuvs%BiD0tI_Y)8>}V?!z|o4x?zOTHT"
"iiibIElh4dzJX~hjp`3|5WDLU`em~7NG-g$2YY%mrQSHAa-P<D+WXw=*T5UaVr6EKclMM!hiwd@s"
"Zw6~$|=Y!}Eao)C7W3Oqru#m-p&FFyRC{^eh086Lw5B@aln6d+!i{JG+YSbz&yN&T9Vi->4KWNeK"
"n&aJ0nD-oC$TA^{MBT|?!C<V$;`NbEOe~5eAw|r{U}yHNu}Egrh})b|a$CYH0YRR6n##a!Crb&o="
"DC$2J1Ks<b@{Uq;m-)R3CGD3Adk?Th>lFFQsM2v#ScU<R%gI{x?|N@0rwq*eJa(ow`zozo%y0ab$"
"A635#12HD-B(tG(J!=sjpD6A)s7&;T9&6_}=Z*r;1i;LQD}0|B=c}m3IdkA7#Ug^(O6q;o6UmJ{U"
"nZcy=`Ic$KcK3ECM71II4aTe|)I&Bz4mi^QS{7X27bcke|fNXZDBmcsm=O_pq^R(<3r2oO0HEHr}"
"tw`$h!Rn|JKpuTqV)>X4{hbEQ(KF1ivDV#W1*#1~(t?H+<z3s$(Gt&SIG82=YEsk?adv0TrGBjh-"
"&zs^+s)cy<H5)x)BXh0H!CsF&oq})a$0=x`NxckeLqY(c9xwE5XFE)<r-N3-Wu!*GIX+$oXr95H4"
"K`12i_1KIg7$()<3fEvpQ7V1QO9lAfCGTmUR8R=SnPvIt_D3V9l}nRpfr1|YQ~`VjtCq_1>WXCz0"
"m`ECCjC$c32n~Uj3I#d0Vx*Gz1#eM`58L+3JrvKN(NEK_^~IBWSQDgv^)Rz6i*<B7tP;X=v4B*1S"
"JUie6K1sK%8*f!Za!a7315!8Y{-8u2!oG2>EGf8GRsI@+<OGrCmd4`m(x_;LVq$CxUZ+Ny^0k*HX"
"G`OC#aPIT2gqbNOw1694|=y*b_=tnCW92+tD@qqbOs)zM0V`n_@<HRWCg|OFPLL-I(+tnhk%i#LC"
"=WPQsaTROQ-W?0(5{2H-g{#r78tMG9*EA5#y3?;y-mDcM<H4?Lv(ZBs^|k{Xt0s#1rFzdnwTo)Bu"
")tuC(2euO+y^3#9bZb|Xl%fRR0OAu{)afITf8@H#MJ;o+F6AewZIITA(Fvzs<_tQ+UzB2OoKy?;v"
"xl}0?5DLUdI!fvm5#P5SAJ3<0`M*%2rvBpL8EJeZ1cQ{CO-nL<-7*=_ya3**twoQBFBk=KECj5vf"
"?^Dp}GhA>{VS+IiF+iE&G{oDtj<Dn=6Sm^BdmaM|itu0bVzqx6)$Tex9Qy%O9Pt6HY+QplfvBx3M"
"CWE&6_3-)){rh_gqgAD?)Cl}z$p^9Euv>oT+pk=Nv1SS40JZl9F+u~;0c~`c%h)xjKM8-t}v^cKc"
"#<|L`l)lPkMU0Q2T$YBbwLSKMMhLf>#uuMnZ)M&gfwv*0jJ6y-l>hK9(Typ~uP`k@<eZB^>bNOr>"
"iMW4K8C#iQmSh%FJ}_9T&O@8j7O;qCuDaOgrjak#eJ$58l?F!0K?%7;+dLiumpfz88y54&`uJ(dw"
"la2(X}e3{z!U_rCD7d3+@Bt9CGBWZ$7h*91ze{pVpXH7zBaKAlc{CNLOy+GonxC#oVQb%q*RNcJm"
"idc^h}^SnH=(_e_28LZE*HN0yeOem72g=*4b`6s@`<L~=szYNb%0`*hSGA!5ZNHiETe%Mmrrdxc&"
"hS{(?!yK(=Wydh#lxKj}viEPtm41fSfpIidGXbG_H+IHh4P!hjs(`XFslnVwmY4t`wvz0_;vQmt1"
"DtU~EWO^JD4dd1nVa<t-LL~L9I-G~Fc`m%3C<+@yONiBwpeQXeJAAGU_%fYza%QV!eqZ_|bKQX#r"
"3Q7C;y}va?UtS`<MM_!8l~M6K^)mmD-FRB3f~JnIhlDk@bJXSKZ#M&XbSR?dm^txxQ#`bqg;MxfN"
"Y`b1D5jG^GZ!TkB&Bzn7H5hfrKdQ+Y^OsQmI>Vpbh$ZBoIbBb<Mq~cYA_^F)DxOBK2Fq|E(TLv33"
"-tHQv92K2X!*hhU;uh(stcvdiyNMj*Ze<L-Up-3ZSwEbRaa%KHrF4hnz3#8j4ta){tqN@-3!c<Kl"
"wZ-o6Yyn$_gY3<g$hGGgdFIRx(WqfyOsMlJ)HaDH?0?8_?%9QpDkm}k0qc0F{AV?7Ly#d($IrnU_"
"i*jnGhuJg0ol%zyYOK(_qcb^+VeJ)XHxSJDUn*i|6I`I}45F11wtSXWp|-uOH`~yD20j<&=?@bM{"
"Wa*1v82&mWs&V;kyznAhBdJFX!6I8bvrsMZ<$dp@aoR?q@jRtmev(l^e<JYd};xdmWfLnxcCV|f^"
"lapQLx1hx#X0Snhdiov?DaskUXn&^N&`h4v`xrDi<CDvjDfVTVXg1g!i%)F#@b7T<CALHorcOq%j"
"cVxkpf?_Iz4xx97s(x9OTUJ=cJ`1c7_a{2qs)aI;~@2NTHfCD5&r<qji43Rev#sy9@xQ8k0aAf^;"
">_ZF9@GB!q8{kk$&>KpvjmRr<`3k3Kxh97*qZJtKf_a|Lt1t#?lWqq8>>p02zG?4xdZCizy3pt!t"
"oPsRt^nw0eemla+fX0k0LhScu3se!^iVvBORfo>0%%t8TD9Fd6L0-y&UVM57_TVf@u>>SuPR`+P;"
"xMeZ>!2DQ<L`3E*&5+F^^WGW9~RZ?Ua(==?z+Z`54}=du!ZnRGUqCaoOh2#ujEj(Xf05XJ|KZ}VV"
"UHz#jLtJ*9W6~81qT)(~j|9<SxmCQb3HZ&-Gw`f_}p~#9DFSOPaW!2lRp811F-T%e?U!VfDM>#m)"
"0>CXq*gz)se;Cw_ZDSfTzcud`!DMssdw^0x}v<pJ93uzH+a+s9m-#6Bu*3yad6dMLiBK(ZDG$Ued"
"FH_yFblM2X?{EFsx<t-NZ@Lw4aYq6pQU8az+8#fp;a+(02ft%N{Ztw44Mj@p(W2KiDEBeNLK<xeL"
"N^H${1AREfbqJQnl=unBe&;`~nAT7XSdm2TXlO~izH|k#7FxQpU5f(uw{9;~FqHOX!nTuU$EP~vf"
"xm9V`VF!g>)Vgn%4Z1RYM!#2r$>m0=>WnaLhn!9Bq>B11MzT<n3h~e3s=E7rHYQplt3E%B00bzs<"
"}?W?<KCg2XzyXyuQGhJgg=GJb&{3kjLiDhbbb8eBaVG^gq_mw#7#-a$7A`06c!pPwy{PDyTI32AG"
">y)}XQwNeH~2eQUn&!|EWi4GX1W%m)S`zF73{&TA$<qPVWDp};3r1h4OC18*fHF1LQjH?>$Iq_`1"
"v$Q02tY69R85l#ta>n)D2j;*KQ0x>eclrxrh{32nudCE>nxDrf!*}t0}XbqL3YG~Tb3L@oL&^+^7"
"{5+!Wv69wn=Z-4AC2-ai{-^Nu88BjSx!>{&e$g$HaDM-5)1cAf`~C63i0FgP0KGHK$>V{JRz;`{k"
"y^710>+%II=3Kb3Cx;BVwSJky_tw>K*5G~)}I`Lng^h3{`m|@hy#pwO&hHkcOiEy%|!J=+`GG0&^"
"VW>3&7_lYmncS-&>N2!9lP*GUtIUY66MAB(Ynz%|P_54s1b%K0*sHJW3b6M{67LCaJeLiolw7av("
"vZo-|f-r#&a0BayO&g^yb0Pi2Iq^@(S`M2<)1&9ScfFA-=wtbA2=TOm;e8^3vcE)>iM;xi6vkDh2"
")lC#W)2lyr=AB(x!d;O{mtA820-JR|))jxWo8|bZc6xT^NK228LFgfFI(71?Hq;sL{Ed#l9?1?~p"
"Lv$@$MxlucM{ggEtDK_r{citcy0{pcLFNV_sb8rVMs)=zMZI;H^+T8Cn6@Pb0nL1}q4PUUH6GmC9"
"el*LwGPUodcazaVg4$c#gLvhB-dCSee8L(vNEUr@D1syya|<AVGS~8H~?O%d{6SHjJlWa;&VnkFn"
"d<m4k^`->K%DhOqAA##v~8i`pcb@17wT;S_}{k^?D}=UgPy&z<aqG9m9?^nMI#&i9ME|sl0@G_Vh"
"a_H84(WwEKoaxIjIRM|a$M3xDAcO~#PV*(xw4wa3_Y&<iHL2dI4-%v7rhsS6A@gB2n+xs1bY7;n<"
"Xv}^*Za<m<MP$-Wa1tzA_$W(E74B1Hg$Ls-=9!>}Mcc99N?1RAs&2lVFaC-$_V`7bxs_Za{*yxrb"
"fjqoSDS{#G+-o&ud6*srQm6(f(C_0oO@zjwho)*_A0B3r1)vXe%XAG_qaClHEK3U<A7b0j;|y5qH"
"R)iFfJ|wV-&V*TO3y>Yh0Joo^ba5I{)19`;w5g4G4!W1Q`2A8ItoI(@($*kWu$`gvV#%pt}q+&sp"
"#GVzD8o@Q%&BJ1r^#Jfl%4%cob5ZPvcU36NUzukG5x#5St{#sC#afl)6Lz0HQnak+Q3K=H7&~U=~"
"rJkWhG;AY}=5S*t+nmye)rh~u+{E|P+!*@_V9fsNYauVkea$?9-hnOf<C&Phq<$A0ER_2aDmXlB}"
"v0-9Umd9R;q={30wf;9aZfUfQ~rUU8ILIUeQh-SqN2k>+LXQq5z<Sjh-SuAxs;o~}?({OJ)nYIq<"
"e=(WLA&@cWo!P*UyFwQpm6^L{l*Hgaa}8J+wOYrIe#cd1I%Y>=I&C+w2;k@-f>hd0=k7?k%>djBD"
"4vyaYh*_qwl|3w)z$=V%CKPbIWQ6-B);S^uWB0tRZ@vNNr24sqBM}~SJB7WW@Hd!o4O<dWUi+WfA"
"Nu{z)lOyaJRbRVRGB5=8drYqCvIW9jbudc(n1up&Kb}B9N_J$lZzY4=stk1%l}6R3lZ|Y%<n(%;W"
"FBYFbM;pNeJsz#b0V#6~68zcRfyK#jy=l4#b1MU%$fPf*y!5#V?m0;u~J5a}3iy^>~L6$&wKF`i9"
"{j-_L?Ky$DZ7R~%$a1!@$MyOsJPyZLMJiUy1^tMnYBDg}jdkycvW8xq~d{CeGeiSZOdqEK~$^<>T"
"UXeb{*i7N^x8W5UE>KOq{@9xJ(pE>u0fh*&Zl}1R<<w>uwdcSb>u!pIydC0RlC8j;^(LlhIj_m=s"
"X6NiE9z5yl`9Sw<;$NMvxX)FaxGkqoado%zkgKTzE6CA!z1w?!cEOadG6e>4+Z*8s`|0roKgO}l|"
"CZf-VF9js1Z<v$JfkXlsX6r`(rFlw=CvcWKwz({<F`lhbD+dI+Xe{hnRHFR~1A@lGdvSC?S%POUD"
"s*ch2XaN``3n**Ab7lxIqVofd1AR3S_9(|Pw9EC{tqER-9LIfbNHjrgjue2Tvki^qC?3aNs{zbwh"
"5yxap^B*8Ho<?lPa_o=Y<uy9gm=LN)g(paJEuU8kivRSUn#YgG0KfGKV2%lEp1L1*~#f&q?(H@i<"
"q7#Mx&h}u#d-M>>ZaBUTps;Y%6Y}ohpq;=}$VzhyJRC~%C>&j5R+C7392nQdz>_qN*2D=j`JVpKZ"
"Kj6BAUpw|OnUc#A-M1AhQ}v*)KUKGKVIFl{T~a~_I`GJJA9}CmPE$Mf{w<T=cvn^&}t(lK31QfZC"
"H&^HHEqQk>Cr~7cKph*^hW@w6G7bK|~RD6Rch7Wh8m7BGs?T8Q9lfTK;_oV7m)Y8NFM~y8MM%CE`"
"Imd^qhrv9kjwh2CO<5@=akGgKoia_d}mYfD2w3##nMgyMPpsQG;|0=3z=76S_43p=JyuZ(Y-<GCg"
"WvFe~4G0fdkXv_mGN%zWdj*X{npVo)fnF0?ps!B0Su1gi(+=ENKKeRN_)(;f0d0LWc*dj#|@c|09"
"xx1Wh4P6(znwmkOe4e%ECLFF!GUj<N-c_^{G>RyQE^xcf?)CRCTy$;&W;^ShM>xB5y#L#{_uimmU"
"d2s&R&=0lx%KEY1F)@JRePtlyORBMtzJt#V?yPR%F|3qgUIVbSk@75VCqu$m5n3w7YI>U&+1;)>("
"6iq!Mn&CTHVzDLm!IjYdJOd#=GLf+8Ki?#KR$Xc&X3_4$M=JW{5WQ*6)b;@_EZ@Hd|NJnq;y=#0+"
"F-kAhnw5H8Y!XKLWIUQ%Y`3ec9qCu!pM_4fkzX8@mF%v+-;<6V!$-P8<sB);8iJKyo`;P_08o@D8"
"}WIL!jH(Y)-Y~}ZsE=hNiQf+ZXrQ8JYd$C5f?#%;KDW-dRKK2J1D};<U^Dw_+IamZuWjGM97p5Xe"
">g3?m!2r82C|K{#$~e4q0@0k<1LC}v437c7geZW1pqt+1#{kQ*q)Hd?0j_v(XJ|ET3&-9HI-}El@"
"@Nq5MWcVn29%M>zE<&v<HpV$JAGCFnY=4v%2}AUOc=el%OXpSB@nmc_c)}RN+f(fX@{VQ(WB7WEf"
"Gsmi7+@ib78qr*3pDw1qgL52vE33z-yga8gxLPU4nfZW18i2ODUpB+&7XCqfY|?E8&C4^j(ft#3C"
")FbGs*cpxy74d7d6=9L3yWv{aYvGBZ*XCnmwgbBMLQTocgyaSX!s<+ZF<&E!{lSbLV(w!KjDWR1*"
"$r(IUUpnDdUG72v7!Yoqo$@m7AV06GUo@D~-1^|9pQY&ynr8;Zxm;=<ey)=SUa)C76t_B-8#g^NP"
"C<#c!AMO3!pBVNrC0pUB-Y&1T`s_21jL-=N!N3HTFHHX&-RG7V$=0`QNQtl%vP+)CaaGQ{Ke`f%i"
"RyYVwcDZB%6dRNM~r%RZr}_}?Y=6mBwByB4z<gup}@`eLRX&Y4q8sLi%*)Vu-bhZL(Q0dDu6kzaP"
"Co}-U;FyIb-_qS_U8hVnVgBopUcc+dZn=?u!>PKI@Cblr1ujD%vs;?4&Cs80HcaSjb=oM>69qcXB"
"z?F>;1-DBfg<b>5-M&TB#~GmZ~HFJxm*14a23&Z<LoHAme5w``5I#BaWO7MNv-WT<Fi%?mi$R=hj"
"I<i+zU8bNh+<8e9Gc6Y`Jl21@BbETx7F|7ZNx_+4VEUlWdauBC*LGz8rXMd#E9MWKsv&`u1kYlAK"
"bVX%p+)(eZgbcO}0Zs8%sA))|8j@7CiGhNRPH-w57WjMb*5$Arr9#FP+2Z7BL6T8_Zr~*SqD^+Hq"
"qVmOOzPMCKs)p26Ro!ud8I+k*@NL2NE-9*e?e=?YM!r?CkciEv6yqfr&%ag6Ijoqse#~#Ld1iTh@"
"|4a9jame1|eovFbEs~be|B>px<wbbfpAYT;EkTYyQ7RHXy67@*nF#=v+NNs}~ZWhhMCQ;&AO{as}"
"|{=jFUJlx3csB<mhA<+l2In_S$vJ;hEtGszzHwHTJXC=eJ3SBL59ER{Yb2ktt@6F70w<GaoK9+Mc"
"ls^1iGlcmRAmOFy*7i;`D&#m(bb>@d+I5aX4sZ+e$bDECh&eOHsz#A%E)?b?9i-?Fs3I2|xSSf|)"
"yCR-G7x7i}*X8FuZUl)BxO<Hilf<7<BCZ<$oqyMn3cAocuf{j?Z*g>pk|r0JN6e%n$5KakPQtQ@a"
"G;MhgDG@Ru)=}s^KYJH)o_{jfG!8`U!Dfa!*35dtXCVt_$~<CW8XEFLR=g<517YU;qgH>X>T|KNV"
"`>*H;L<H@EwPEwsO1BS5#|zp*QaIZ>P0{k3i+l8U&mVY)QY<z$v>?+g6c<1AbvUlh@o6@<`-`;fd"
"BL9Ma&rjH~c+a^fJhOqvaGJToTZvU??+v3-f{gZi@)e>cQ59_J$Kb)&6ha-Uk%N)^OCTF1;aYp02"
"uD5TovF>M<iAE^id?>SQ)YZhrHI610WUA_((Xl|t-U^owC5`U`T;*h$)JV_6gK@>Vf+q?#0i?ZOF"
"DfM_n1z?xicdcgDdV++{2|g$99*%=|nL5qx5(rj}p!6AluR~{QO}XAVvBx*MOpR8TkeIwLXJLl!S"
"p;akk?jLk8ipIP)#jBCu1#5ZLCeb&BG=IG<qZZ-Y!GDhMXWG@m@)}3>|4WjK~rBrcw|4LQ<YLKhj"
"z1dlq##tJUw?WSW9NiwK>UMEZ+;e?oz*9<N2iG69-rc($8*FEFW~EsH!S*`BU;{O>uYDO*JP)v|~"
"#tYYF_&(Ve1f%C9a^3VZWTd|W|0Mj8N9C<eTh4P}yMF)`%Q9H+T_=n!R%LGYDuD9Sj7_xL2Ci*vS"
"UHNKVF(%<3(8lOYfqln(Y#1b?HZmAjCb;?E>FCkyHqwF4IS%;@9+sk*sSV!JPt>Ufj>f$<@WD1Jx"
"h>V+D$6Hf){(!e(P#Y1@)391FCuo@OIOWCZDJQ_+zYGC6Wi^}-NiRr1(Y{9N?h*7v5rY_Fx8e@Ds"
"JZu=v)xu>m^#oOoyNVn+n$5Y4phoh04=SXpd4o#FGmg7!vmM*K>}MG>679JalO~5w8{m9fRlg}oS"
"`c!p-4vmFM+HwD(z5r((`dxND&Bs`Buc(c0)pux^u}2_!j5QJQisn2!jy77b5)?cCd``uBiD0KeS"
"S1CAWuE*#fq@%>6Gv)$i8-WE)1Q&m|hl)eN<bM$^x*qQm9HK-V9vA9%0<qMH{Z;>FZH&5v2rGi9D"
"?h-5YdmNy|1Ti%tHM8XbeP@so$jdQ+<=tnEH!cj%qkvXA^ntNCW#(k$6&_ReQ_l6c|a%RnVS%LVW"
"(3@!i)kDIOdRG7((vhfr1SI;HDrxpV=ruKV2m1%863=&A$@4c}4jYJS^!lMDIly}DI82l`W=(h%;"
"dtYZYFNYe-Rp;Vuq9uD2)fQPtPFSl<fDXfWLV?V)Ts1qu5iCotb}h>ae8=;=r0Sh@Rrhv&i45}8g"
"Dg10cI9+XzE`0>Z~1?I8<hIJTmZ~I~as~(x(aVd-UzF4J(=rouJWH{sz`2<)O@m*Q;j_FdG9oLT-"
"ol?9U&msHgwL^4?744$yk9yx1>(Rdt!IQ{4+LB)!!1`~?l0>G+U3078!&>b~~;a2b;pyX7cDCZ{f"
"qFk(Ms$<IOb&v}Zt5;gRNJu+=QYv?yGp|mX~dg-U^*xQ>PjXSmpUK*@X_Ug6GLq)W7%6CF4?C;#)"
"BUx<8^mkcG^+LD-aDdU>b>|Y=7K%Q#R+de?#J+gP-#`iEZ1Y6Vt8l$?eRfPaq>CyaCvHX&nYoLm2"
"hq$Pn@|bD%Ee}3p_fWG1JwSHgoj5=#t;eoySM<;Ju!YO&V(J8ZwrP72%IH$5EE1MW=n8>!2W`N&R"
"Qbi06}FO?L96Ckc3iLo?;tiPn}lfg<mBRxO4t*uj>CD%@E-PbaSRYHCZ?AM@8W=A$IAypw@eH?4u"
"Yhx6Vn^d$%KeD<*9Aw68cAeXpKOh~%Yqz^B*39bdG?6so<1UaezCd>lC6Ywv;NK|JTql|^wINpT#"
"uYsJPLShnjmB600q6=uaS<K<?YioS}Rw<va!H0}YGr2ag@zB0C{#gLHRQ>{gxDEy;3$xROZpC8ma"
";hP8%L%^0^A{WhIZ;n+MBFQMR_ITx_dMftC5*i(t_8fyQ5iB{)ueQUSB<`f9fSLf^MHUb6XA-BmD"
"z(D939(oHkd?`DiBfMT@4E+JZW?`<M?Rc#|70chJ`q2=lW){FzxgfNHog6bw<bOwQ5c0dLl>*_7+"
"n&z#>u1pMsi(QsoE^#j|}sl+lqMb@_p$~^`vk<Ov`H#r9`C*|JmX3U=@eo;=bDGjQf8l6*bsX=DK"
"TJvUWOAL1#+!+pqUh8s#xh(3RzRk{q#!*F}vW1FkStQc;g^T<O<Ya+Y$;gNxe+ji&X_y?S&eosV#"
"p?c}F8wqHUuJNi5?f$Z$>1UCmVrf4+>19P_@i;DjEfClYs4(m)Z4)5aA1RJFwE7T(_4~$q=N${MU"
"-0zea%&p^fx!of?q7T-yA`38TbVgX5Ndi5H2OB7P0+nvk!=iq0lwaA%zymz~0(cKD0K9_-@0Y~RK"
"Pqxd|K3hm7!Do0d`CY#r!M1Ls>qW%$gH4fbGpr(A^=zJ5?5B#q^vd^({sv6OQAWppmseop7O3#%C"
"vpo9=LH8ww}sHi6N?Lr-K{_g(l#{S`q@^Ct(pnp6Ihh2B3cf&Z2pz7m+f1KK$Zr`6A(!7-Auiu}d"
"PeDnN*1TCRBFB{{yCR>eDm;zWe(z^&8CfMjlv<a~7Vwi%ZRuf*%V3m}asvSQ`cUyl=MC+@05=9Yo"
"5mpg^|G5&xm5PAcwrV5ql@Zy`WBGAC?`L_O%CiMwsl<f#*x~=CIFb!V2*(*|Wsf3ajIpD02bTf3B"
"P%8iu4dbx;#@h>!qM@X14<|{a?6Nl7fY%-;M9WJ6c;ubP%7uK%586i(2O#9;q%bTMB9L!UB$i$2W"
")99-sz`R26hSwtT%aC;5G$M|cjvc=_BIMAGK}Li8ITWaI(f9kN?pysqYVPY_=Gac02%+9rGXzbg%"
"W<2i8o^Ndns>FHtgH}UXLerD*fM``tgEJ!CGH@+!WPWh%R={k!nBKNV-i%?n3N>l&w;Cb{-Ft5nZ"
"$f)$kowkFLLQjsWj+ce_`%oC~GR=yyw)$~rg<{@wc&UttMSpoF7Z>{T10FG2%x1&+31#?%{r`acc"
"s6C9h5(__yuU@rhn>zR6cX?EQQlRP%|XHX_OW>n2dlncVZvLsXB#Z47F{PHQC<Z3ZX+j50xesQ4;"
"_W_L?XrYwe&gw66rQ){V!;}|uDtlK;!ZEfKjlSyq!m0nA@9;E5<s@kw1m2kUE`B9A7bA`1H_R_|<"
"1zmxsqHqdJ_M1iJldgZn!pJcFft0XYd&(@2|9Qs<WtTEWL^iN5dx8igM8%~_FnpNnhrt+$ho`}y3"
"eHdTPDt3zz+n9!!&Z0{KCj3ua=18COIQdl!6-@zmT!Zq^;_5d!F*HoDjTJ+$JXuuf~s$r%&_@stw"
"bq^_iZf%m*SVd~eWvrR*%Vo0OH4WytMFy5R=RC#GGG?y!N8gc7y%CG~8~ErVKbtyvS5c64KLGUW*"
"*%M%JV+iXVrGjN~PQeKx;SMWRdz<3G{Mt_OJqoNTD=h(#jm8fQB<YGr7BJgn?Bw~dPBV|vw=7w$z"
"(!97}4g5rrg`;DTemV9R?T+P|w2DLr;$#WLs!4%-6;y`KoG2!I%Pi%p1+sQ^1)+x~&L+lgno84@v"
"AStuA<1Ml`u)aaO;s-f1iTei-N)ePuz9xcI#uKqZ+xn#Ejv$^I=25O<Go6%f)iKtEUx8n1Cs|{vG"
"SJfn6#^ueX_X#6SZ*$&l0yIwZsTS*BslqNXUQj*%@DcSYSeIqz%Y!hZynIZ08FU?pOOPaHMh(cB&"
"5st1dSNn2=6MAu$>K_tb;_+D-$nVe{r*$@P1nzlL`=?X)6=x4Sd#(2V$drG*x-LNt9_+y}UXsc_4"
"PfI5#oOtv8%Lp*5iK{{cXO}f&Mdif@J-@>9L82z3A1|=h^eP86<bhyEbYDk3QjdU2#7OYuzqad|+"
"-8|QvW4ZU(zCv7_t=7IAmRDu>-@I^$+Rk?<lt1I1p$=SkhEAQj5g$u}RAHEXute2Qwjk8>c$I2eC"
"HL4qNE8sRq)M#3p+Hf$Nw5z%D+gNMYr9b4CUt%)$g7_$0wAJ`hKi|}0UT2+;Olp<>bm5s-dg8|<I"
"|^NYzHExSq|=y0>ddv@*$=+RE@*E_du<gW4IUurM9;OXXF6{G%tr)PmAcGI9g}q6S0FL@D438Ado"
"3gUj3H^a#=<2>{R`w9rX7^n*hR~dlnJTkupL_;t_x4Tzi*sS+jm`n|@|2lbzh<rSgfr0EW<`UWeZ"
"|YE7%J7{F$#*kVPOIV6d#0vjX>(#AXhp%^A^mO2>U2jO!M@&UQP5>Wr1{+_~{TO)}FjGX@(aFaZj"
"N$jTbUN&rfg<;M!Er7C5`*yj*>k>sCm76w!AskTOp$iIG=FUy!d#@Aq9_U<;2t9?72B>R`y{#Vxy"
"dUnQ+aJYb5_yA_LVW*mRYsiMN^;T-)GMv%EW0A>zQ=I9n#a!bKnEDA{oCmC{rs~3!fo#sii4W88!"
"c*<d9yCDKxn{o6b(NOx7KEE>N3jjp`SMu`$!<(H}W+j+!;tUHy;pM4yi|Xv`n^&X6EZg-}Ib>vd@"
"2vT9{z=Zi9J{It>&0&o!2%_@M)#V+NJxX@i3euZdQDY2YU&1#ha%t|kz|g1Un=5;Ji$*eb?%mm~b"
"J@2uu^q<6L40lAR4b2jC2oLH*H8zY`g2DSOc2ty>i<l0-Cd5V*lVeHtH=RPg#o4@@98hCW?<b;ov"
"W&_;Tx|Yslp>)SG49v1|fa0D>@blhH{$pgairWG$w1x;b{R%Zri#2*RI@<M($zWs3Ly=OC4pqt{("
"XlNRXX`n9Pv--(KotMD@9|eJx5f6<uq?N+PY0H?XB^nth+;U!K;dxJk0wk`l`3I1W!8HFM$H={6e"
"O4B&3p)y+uX<kRVptqX@+escQ$#Sw5E`<nTJ3CBFw+6<hlG8<jzu=4OZo91hIfYsWoI-d}Xj|MsQ"
"Q;4tuSl&xUoJ1W!p%W})=->*JoPr(3jQe<U(O8_;|EN|YxLdoK`Jrj1{yHsuaDz##s(9>CwUL(q+"
"dp5{5eg}*DdUlO04lTR|1El64yB4D2(dA@(gjAn2KEn+cM`Znuy(#|cB!V?TQ0ihZ#iMYHD0%Tkk"
"kz5tVx(IiNvx)q6dLvu4`eZL{PYB=7F&~Q{r6!$921(K#_OB>2W+OvRqd5Wi`gJK&Sd|5HT1>ZvY"
"H;Nu&S?9@H*Z-AvFq|2z+@=ai)B&{H+(VHN%nb=u&1WC=Gm)`nu<ITOe^)8MN!vzuY~kW$xJxpfI"
"kIO#v*U@9Aq6bXhT>}QG!=A;892#KPyJQJe$lmv)}?M=ntbKUO(&5+NJ?$btY{Q=hI^6{ezTHQ8K"
"mTr;<)~6zsU?#lh7qOR~^C6rIK&*B~FlR`#`(&YCnS*jB6IrP1fD!&k>b{(W@3t7-#6GPuA(2pVy"
"AuhHY?X`JEmHWb$rqUOkSKfw3Y?@6EFBY5gI#S}6dm`XM@CS_N!kyG;(Xw1H(6vj&f4l%9ed+by="
"^-iu^kEWJ*CIP^RkwY+7SazDt?7|`Ct=&__FXU!7EcH$#ivMc)zVUg$82yyZN<H#HAY)1BLyIIEu"
"9w2``k?lHKbU{~BmJ>PcobtCd?R4^jMiS?Aj-UAWXXtZZA=hD+1X&oK9+jT?{NpfXPrEw!8gAA=7"
">44I4e<>tv?*eqK{<3{NY%q>BtXCb%+$;Q$Z|E9v*K2IZ#9nN!)h4)9&-edbh<&`&~0JFK#=zYG4"
"9?gYdkz{io&s(v+F_xvPXdjh8hwEfqj*eQWcD{jvjrN@;2VP6kpEtnBnFdutq$w6$&Ef_cmC%v79"
"|4q|##sLH@lo3V3Spnv|lsd)syy}xMyV&V436uexXgF-<yf71%x-x7xUe9_dP+e@A@pSs4^XD2%R"
"+!E?xXPJmLCI4WET1|!@tz?;L9JlK)@xf@XCqRuGYrf9!O&U0$@EpdBK&El{#Z}D>;SiLypVP)cU"
"+!Usj|Zr`Ov4)>Duxcfy+5$qJ2C8CVFcJ>=#4vkJS7N*;=gs_9}lL?>MMV~Mj{jXU=`u8Lzs3MkM"
"_a=r>%<lKY>1{k>T4c-FB~*r+4(GBP&*EBG)4IQPeoVm=On~4g|}BC(Ai-Ja1kqK2@`cWibJ|gQ%"
"8l<zXWBakI<YdafF9W2>xz`IN_|aODX>Gr0>;=Cf87Vq*EgMqo|e#qI+A6H#`Xn%4OL>fc4mT*WV"
"oT(YO^WWJBEt|<T<N}BDs#+K49wyPmFMS>QgNc_0J;1k!cq{2_$g@&{1L>m{m5<<d0iJ1vkQ%0}N"
";9uEY@`QfQcgCA12?xjOMnoA++Q4XZs8b359x)*Vk*TJn)5uRU&#7#Y4nug|Lmoh@E?T#4u!;TRb"
"O!hxbuUvtXN@m!kiOqs$YD(JP)q|-I+E`Txza0#B7hU_;m>Vr=UQ21<PabH*8Sr903`};PDk_EeT"
"|wUx8pntD9KS3UbZ6Me>Y*4)XkX((iKFItX;faUFW4D`72vI$Gs1c%mJ?~R&sF(s%1}3!Rw{kac)"
"FA%-8Qndy(<BCB7UtQ7cFCI{b4!XjOOr_YhMIz8CrAE0dtmhU=84U$!`nIGr}}mIB+p7@!HZJ2J%"
"xdJv4B2=s=1XB*ORd^ZRO^xT8)w*?l-lgep(1i7B`@*(t-$A}gYoAQhsppF_617I&|U@j>}$;tDu"
"qr1APy#wm@&eilW!J-b*;Ui?{Zoi!NTUJ7+qbLX0a=-(*%~;rvXXr=2OqPAqm0Qa?sbQCoQVJ5mH"
"<|EAEntX+2uWb{bqfV|Vc%L&A}z~d4v}$^=zIvXM$YsFJn;|jfCI0w-+nW#qP~;Z_rsCSQ0+C;rT"
"~gG*+C6nBjwkycd%Kra&D*wIhBXT2(^<AMtxTT!t94?`DWf#j3(*Yi=G<Iz{U_KC80xd;M9Y4q|t"
"L8S6ksu*^=kJ59rPV&vcFhWlcd3gryT<UXD0@Uc}5SnKs+SsB{vquVCL&6^S)VLi}$6=qM|7Z2LO"
"3rNp50EThS^pX)j<4X>a2nm8dHEdmuVzSUPT=$|+|2^BpL+ddJ#Lb_t&5tzj&+o&!iXcpK~QSfH7"
"b?aUo;_|#Pd0&nSW*{*9ia3yttL7h2tyu7L=mRXJ&i*&1esK^~ISk{0M8ILP3_X{aAa&MjG+S$gS"
"*g}7J8$1Sr0am80QejFoS#0u6O_ChVjq$2>1acj=0__0HFgl$<=9c+C)Acj_aD0G9Zfo9kfIqD0S"
"!WTcYAovHqM5oI!{_^dKuxb9JZnz0NOZ5rEAb5(ooRE(*~njB0tfH0LRNVJQ!l$HmS-#XKbGaOgh"
"HdK8QseNc-|L-^}I&;A!3Gr)x0-Qm*`cBwZLC<@yEmtuzgXy;yv+Y+EE(BTHx9hg;@KN4y))QfO="
"6&Q30i3!neaMI$VZ%cbPKufmDs6>ukQ<e>J@d&F}`I0P8Xtq07u;w&MAB7Q_`?m*trMO(al8Y%)^"
"5O+-skJ$q*F`lrSM>JYL@c7)oP*QeoDTCP{43!AWCL$eDuXcl(zeixyQR1;FATqbJ$75E;N#(q96"
"IU~2S}tTG1R9dxA&^scz-_ov{TNG9P?Xa3EZBNTLS(=YcK`Hj{ME#a37QSARJq3AuWP2CN@7OD_&"
"f&$`Kta~ZML>kSkAQ|apH$Q$0p*>&`2;W;#%t}thpugyxR&<9$&9cb)tst0<=kWW5Bd$s+gJcJ|#"
"`E07immp|48vMyOQ9Izuyic~W42*znY@`vl>MFJq?`&=+u_@CHuR<E{Y95m+bmU7{N(fi~6(w~z^"
"<HF~-Pa)3?g$U=i#C$84`pZz8V7E6wQ;lPB;g;|foEV%T}alUonw^AGLLm;(|vdh2KAqw5v<=Eg#"
"0%IW9H?TSqJ$T{nfh!{Gub!Yo#Ji=lBSlTyLOY*Mq>8Imi`*Rz1ym0u=5asnI+@pa>F~<;u)ZiXL"
"xH!aG$wzDuImBypsP`kQ$>+uLKRr;eZ9>!0v!!1(2g&Iu#~HSTfZ+Ws|wR^3?Uxc&{fQ^pU$O$oq"
"6cz-RyFaLuJ4(vriyT?R;JR_Kd5Nn3eV=#;bE}Ed2xaw@2tC;L?<L%nRp@?&nPoI0ZMST{tqdp9~"
"xxb^U|?=R3x&3z5o^3hcDk68(-;+tJ0BS8e@|&axr7;;S!m_^VLJH#JY#N*sC}UqP?u1=}*M3cN%"
"+_CcToH6%!UaZgJwu<-^2JXOXukLU)EmyyC?p)#aX(Xy<$1^>}x$WRdNFhE9!WjP=*v4&wIqpuZ%"
"@-@i7n&{Xci%BJbk}SRwdPOw$4ct*TdJ#9sSb#KT=>m)eeFul`AcMYr)Q*lU77cJ#r`&1E*;PbJg"
"~H1E!Ak$EWwtVnQ2}|cy-Pwn4Q0XNS)@&$Ce4IL0V+PHxmKv9xN=bEv?n7J>sCxLA*I-t@b&Sr@W"
"x@mU~>;0EvdGn9?~b*FQUaY9`@=BbZ<Tho2k|I9CSdY>=JiIbXb*u;5H&$?Ml@li{*}1KY_pE?G$"
"*DW(#yBRl-~2BMV=(^Lie{6G;ode`)5`uYCnb%$t(;NRlsWy4H+KkV4vf>C_@c(<qcOcZf^NRWpg"
"Dg#QXpDVKQ?WN*jC;78-zR`9(CBg_yn>O*e9=;x@MGDqq(LWKsXTG!vFvIeC;zDhB*k8XAEucC?m"
"h=ad4ZBIZyUVBd!L5)@Ex6OWAC)Mk<8aj!ks-I%5^qR1|P^M62gzle)^H55RrM=iYwmKR7VIX~~3"
"&)cywDA#{$h4~M<ksZCWHC@F)-smjB_&1SndpcPKL0*67YEin4&owrS=2}$-J;Lh$x#g*7rzyWbx"
"~pJDgzq+le}r14@!R*cH6dLwP5^vUE2VgN$IzD2s}zqoq4`6qi;c|nJbwawwl(T5m>0=&4s+x!2U"
"G8td6X-bMyn;Ol<cyu5uMfQ*ty3ize<IBR(!9gHU@^A5ab0V$4lM>b1$7Z8*SVm{)TR0v`@MpA0F"
"q()}AE_CnO<lL+0LwqdZ18I9h}#f$9cHTt=JpuW#;woiwd;zVtZC2>)x1(8B|(m0^^p^#1|`$A&+"
"c?36>RpEvq9Grpr<<cip#4a(|Oy8<e!BQkTP=hM*-#(bWREC8zAF$2d`qzjr7qjkh_~r_UV2;Pf="
"(_eXLd{8H)YV?XZ5o35CY>9NmXwQGs>Kyei#mS?<<u(7;B&2b@mY%o8AvhkqK;6f5+hX{OmzVdL#"
"UtPsy@tAZKGIfQ;2q;(uRX=^_`@VD6ydwJ@SSw)AktDB&gA0;_L01qpzxi&_Obm6`E=Gg5f@5g&f"
"E6O@LmJN5Q*R?I)Ukxy^Y8S$`z|+_J2X%vXh`bTJQqg(e?71-MLZpJqN<@A2fcvK)i70v^obUj$("
"Il&7eEYhzh&>_XQ_7Gp=o;B*3G{&VXfQDS+k$${|zrBLqh?ycPomQTU9chsm&2=Rsc(KwidQQdOw"
"zI_Y9H9Jns*V-~xf(W*~`WVUhELUQHF9KH^Ju1B*vsEjOrqBp4P&o;7wqh;RQMzl0WNA=Ba8!jRQ"
"m!TQu7SsYsFZY)G_0nLhirgM^*Zn@f><n%l4lEY8JV8m_52USmub_?HvEoRmfQSqeML(T?a5*aK$"
"GAE)~aOn>flbRw#`Tp90sATGlHzgg?1XVvNH94gM^)Y*l!%_<+ia}<~*8qSxn%0WxlqT+V9_cMXv"
"?GkHB-irNI(KndUw{!(ke79#>LU(Dsn70tO@!A8*G3<reA2-s<vjV9X8q)(>gdm+Ax1qEi=$IZEJ"
"l6_x++>6gPIET8w|*iAqTt8-HMIcN&exGjRj$coWCvzkUY_~u@csF=9TMC?BIRfMem>e07Z($bRL"
"#``nGgas@sKHe>{1BQ1@<ZW<f;(7jtuifWbj4%R;E?S!`>6$x_"
))
ebmrn3ok9ajd1fl="35828a85bb94d0587ab3b43a728cdc61a0e0ac9301d36227eae55be9fb046ead"

if _h.sha256(ruik9f96qfv2iu.encode()).hexdigest()!=ebmrn3ok9ajd1fl:
    fdcqhyx6e6jp59kjm._exit(1)

pkc5rqys1b3y4_rzq()
emu1ywn2ddrbo=ruik9f96qfv2iu.encode()
emu1ywn2ddrbo=gpjomft37c(emu1ywn2ddrbo,b"9n)(gc`faU)Zw_>-(A@t")
emu1ywn2ddrbo=gpjomft37c(emu1ywn2ddrbo,b"x0~8Xag#bZqw&wBEG2BO")
emu1ywn2ddrbo=gpjomft37c(emu1ywn2ddrbo,b"Mqt+=C8-GvziznQtmghr")
emu1ywn2ddrbo=gpjomft37c(emu1ywn2ddrbo,b"B6HSG`S@Pmud;cKbjmpt")
emu1ywn2ddrbo=gpjomft37c(emu1ywn2ddrbo,b"bC34}VA}flcBRu}bl^a`")

pkc5rqys1b3y4_rzq()
e2s0aqkp945128z()

# === Runtime code verification ===
pew7jfu_kyke="8c76fb2296b2689342972bc1528c8cbd"
def gyicfq6x30wiw(u8k0bthbybm2):
    if _h.md5(u8k0bthbybm2).hexdigest()!=pew7jfu_kyke:
        fdcqhyx6e6jp59kjm._exit(1)
    return u8k0bthbybm2
emu1ywn2ddrbo=gyicfq6x30wiw(emu1ywn2ddrbo)

# === Protected execution ===
xbx6eeqzji0l2rola()
wdjbsis9ro6kgm3i(compile(emu1ywn2ddrbo.decode('utf-8'),'<cynx>','exec'))
