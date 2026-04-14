# -*- coding: utf-8 -*-
# Cynx Manager Premium - Developed By Cynx2502 (sieuthicloud247.com)
# Protected source code - Hardened Cross-Version Encrypted v2
# Copyright (c) 2024-2026 Cynx2502. All rights reserved.
# Tampering with this file will cause it to stop working.

import sys as smelma413zv7syzad8, os as edwj9dpl4pdiv4y

# === Anti-Debug & Anti-Tamper ===
def wxmaw4w3__():
    try:
        import traceback as _tb
        gmdljmab4ozzsq7 = _tb.extract_stack()
        for ip0z_msfqequ7vvi in gmdljmab4ozzsq7:
            xc_cum6i10n_wy = str(ip0z_msfqequ7vvi).lower()
            if 'uncompyle' in xc_cum6i10n_wy or 'decompile' in xc_cum6i10n_wy or 'dis.' in xc_cum6i10n_wy or 'pydisasm' in xc_cum6i10n_wy or 'pylingual' in xc_cum6i10n_wy or 'pycdc' in xc_cum6i10n_wy:
                edwj9dpl4pdiv4y._exit(1)
    except:
        pass
    try:
        if hasattr(smelma413zv7syzad8, 'gettrace') and smelma413zv7syzad8.gettrace() is not None:
            edwj9dpl4pdiv4y._exit(1)
    except:
        pass
    try:
        if hasattr(smelma413zv7syzad8, 'getprofile') and smelma413zv7syzad8.getprofile() is not None:
            edwj9dpl4pdiv4y._exit(1)
    except:
        pass
wxmaw4w3__()

# === Exec Guard: detect exec() hooking/replacement ===
def e_7p9kg2_h0wx_vb():
    """Verify exec and builtins have not been tampered with."""
    import builtins as ckcjnm7sw64ja4kv
    auofifpoat = getattr(ckcjnm7sw64ja4kv, 'exec', None)
    if auofifpoat is None:
        edwj9dpl4pdiv4y._exit(1)
    # Check exec is the real builtin, not a wrapper
    if hasattr(auofifpoat, '__module__') and auofifpoat.__module__ not in (None, 'builtins'):
        edwj9dpl4pdiv4y._exit(1)
    # Check if builtins.exec has been replaced
    if type(auofifpoat).__name__ != 'builtin_function_or_method':
        edwj9dpl4pdiv4y._exit(1)
    # Check compile hasn't been hooked
    _real_compile = getattr(ckcjnm7sw64ja4kv, 'compile', None)
    if _real_compile is None or type(_real_compile).__name__ != 'builtin_function_or_method':
        edwj9dpl4pdiv4y._exit(1)
    return auofifpoat
oe8xjyi6_qep = e_7p9kg2_h0wx_vb()

# === Frame inspection: detect if running inside hook ===
def y2duj2fswlvla():
    try:
        import inspect
        for fi in inspect.stack():
            fn = fi.filename.lower() if hasattr(fi, 'filename') else str(fi[1]).lower()
            for bad in ['decode', 'hook', 'intercept', 'dump', 'extract', 'capture', 'inject', 'patch']:
                if bad in fn:
                    edwj9dpl4pdiv4y._exit(1)
    except:
        pass
y2duj2fswlvla()

import zlib as _z, base64 as _b, hashlib as _h
def bdiin36cz4s(d68w0zb90jedxg,e9aa1yloamq1fph8):
    return bytes(kyyvzbel9jrl3np^e9aa1yloamq1fph8[dqi9jelx3sfhdt%len(e9aa1yloamq1fph8)] for dqi9jelx3sfhdt,kyyvzbel9jrl3np in enumerate(d68w0zb90jedxg))
def ksh9uhbzm50(d68w0zb90jedxg,e9aa1yloamq1fph8):
    w1pjnxdxv9v9gk028=_b.b85decode(d68w0zb90jedxg)
    xc_cum6i10n_wy=bdiin36cz4s(w1pjnxdxv9v9gk028,_b.b85decode(e9aa1yloamq1fph8))
    return _z.decompress(xc_cum6i10n_wy)

b8b00lhuxg="".join((
"iNEBpl%RmrjO1#zRI_TkxpaBAXBCLnv6=Q_*!~vW*vHP!PWdYY{g*juH@<D;<``AkY0yBX#P26lG"
"jf#ga4yLRlH3Z%qP@43wqqv~TLD~+bcg0|Yei@PEK$U?*OZy2u1uSSC^&2Lz)NOD`c?4qR!@-nbh"
"XLDd)1B*=#YEJM9TqZv?P*V9^s~=Q|6nF-c+1lNtWY()WY|t4yOwoApw#1aL>GGO;*>}G|q4aDIV"
"~~b@>MD@NhiE!U>t?e3X4UOl<YH1lh5qE@y9U+n5y0_O_40uPPe;RAWTwFkYw!B~U#xYs*zz`b+7"
";3@`(7<Ib}7>9(yGpW$yy3<qL2zAYCHX`IHm`psWs&eKetrN4wthvhMY{4<*>O2Tze&>U-`JrE}Z"
"Day_@4BljnM$g>+mG((qx`4>KYb;!?2Uvl*)=L6}7!W6n1c_Na4E?xMzOImfgwjH?A7I4+GH?TrQ"
"Qi$3;JPOWC~n_FDmTu2^R#Jscitb1tihDn!rmAWHG-!7+xLXXdlk7SZ*3e(HzfKwuGuh|gsJOX<#"
")RfRI(cC<eQAkTClxesAqS|RO`5Tcz&eQGI6(VE7-nx^KL?Cf3*THiTP5=cofoSplU5jfZ$3e*zG"
"Viv%O4Pu_7o?SZSId!Y}>4e(so#<;nM01GwlXpQ{ov-<8I0t9`IASlaGn(~dddI0mwTYpDv|GdyP"
"bkGt5aHu@9)AuE(A!@ru)WyrJ%nf*0=uf4D|W`zao2Dxe)k_h&~puywx7(!~hz(~tbh_!v*p?F4V"
"e%>ow_a%pSY0;%V@~S5XY$9bYq@@M5_FMpR_nV&fh8|ZFl&5ef8>W~W*I`>z?@u^8$Q5%Z4em=Ui"
"0bv%CNmay=tTQaS0nW3W&eEv<#q5W5TYC;d7GLqsAJOW)z?V#3*|g&R5tMAG;$Qdd8W~Ks^NpVs6"
"PAn>$PkV`$<S(FU}EPp&Uj{<QHBjdMIT4tnUZv$iV{YS^};gU))PtE-_D1uj|wLaiR~!oKE}c9+X"
"B!LJ+E^m_1_ix$(@1h!eD=ZI<vUyjET&6I781YWlsD3}$}t!kzO6J~KAcN#hT|FB)fb2Cp@F>&!r"
"$#9#rKe*AU&-j1q$nr$;%EMW)kfD2f%L17Wm@F{(EKau_<>f3r)XvMWPEIdUSRboNPGORRB>-Pc5"
"F1l>%VE@sWldl{W?k8Hb#6^@*H-qWEBMidjxUV>nr6^h|-6JM)Nf^R^4q5&Vcb3UO!E?VIus5O`r"
"Q6qt=h;^CApVUz@(QtkV4x5Htnh%6+Q}f$AwH`(pe_-Rs(ROQQ8bla)dGmgp)C-}FndJ|mMa0~R9"
"t2uGC^f+7$QZ8E-3kOa#gRtcXqA)XnhHl?a)0ESbnRnB<}lAI?bcnbB{zBn&zoVC=BY1>*pIwS<S"
"KxU7#a=<!Zply{sBZ?h!wKF%|*wpw;suy<!Laotq;`YuLD@2K;23EVvwp(xn;HAI^LQ$4Xp(c8M6"
"MzXibpzCLz~Q$#qcv*~!Dq(K>Wq8Z9?(trh=?zKe%5#tyA^qS;o0f~glQX{3Ho@U;f-ja@<IkwU%"
"mHa2qNDE>?>4QbjuqO*dg+R#VnS0ziCT1|TS`|n;MT6d5W92h`cE_ILV09oRYEJ*@jJgOk-PsP9;"
"en=k<G1%Z>;*SrD#uSSJ3CuTNffX(o4EnkU3^EK=_PF2s<x_utI|j{j9wJ|bzc{@f^66p0FD-0mw"
"-6u9xD4(32JalxcmEPOUf85(3TGZ>XDTbzFy`z%$34Y>7i(WZfA<%4|?jE%jice$Tk`Ou7fLLQZ&"
"lSwFe+Mf~(*+z@HTehPuOXnpyzxA;1wRTZjQNbeIr{^_shv^A@l)AmnvsgV6mZ!Gg}jQOa_ioq*;"
"@V^G8k06KCFR}MFRxLD9E$z$D#LR{cfq9zMEjI5nJH+d%qHJ(|8NG81Ce$R+wr9O3;4@G^N$A8xc"
"SR2?Ykgd>tJZiq9x4>;jEN^R81HW7Cq@eJ7(}9a58gv5=+!?8=Zu-bIN0T_uopdH2E*@yB)9|{GB"
"K$8yF9ePqbwF9*@Hcw!iz#Fj2nlHqyxoE6GZ`Le1qU<$`;MgH+xdn%6klE0iyq)Iyx1?Z$eBi4Kr"
"{{%;2814MhVRiJSI@sw>BK>GIRpL@S~ng=&nAEZvuy0%S!%?UUp2liJ`?GM_mV7G8pp&?|b9`?{n"
"VX6DXP-_Sj10#GoWr5)B^B-A*J<uln4Zx2DlFM*x{er%K-bFR8L987Gzw#dUEweI|k)fL8cMkkyJ"
"e9Rf)#hn;s^7zh@YNWCmkn|Q1*1aCz6$?46)I6|5L=+(y~gAFxSJUX#K2ef~jzrpB^>i+=c!Ep9&"
"G<kkKQMv9%xRnB_0vJU1v$~S*5P|i{^S616{BoElN*%~KJTjMxH^Qcg0l>RL53G7V9aODZ<_yU$;"
"=-cF^baAubi%d}yJB4HlcuR>T5#%m_qFLy9pSVF!g<rU9NFp)+>@xY=G~al39I2T273qmS?;LkP`"
"8DWMreBUt5k{E$iJO=$Li|GLx{1kPkQx3$k_&^WVk-!V$+T^+_Dd4xAy3AznED9Thb7%$?d2bp7x"
"o#FR<>ZScvw!|49%%M1%0H(1czXaSXE^%*qhRiFuSb#_n6=c*GgXzWlivlCP@GDLM*2Jbr2gt_c~"
"_ho#mIL2Q*12iH19#}Ca$caow`9nIp;OPyX_wu^~IN9SMOJE!YP9#*((DPB7^#Cn3Y%E_96NoN08"
"p$eUms9|P>1|`GHe3p^2gPIM{n*8N<dSaedz}L5{gC)s{`6=R_nQ9W)CmZog$4?~)A@J7u8Tt^{;"
"_J^qyp8lI+&_j*8;;MJ5#^4*EI@$%K}%sjr^*$LZ!*v<P`#!ox^c8kpUhX`i%iv97GA`jK|`M@Ri"
"n+U#%BCyCgK{Hej)pSf!rGP@SH1r9I<GL@Py<KkBjp*o{}!)Ofm;wPFd+epAC8P8_l+b)<)mRbeb"
"LFxwX8S0Dw^y=q*#jKG5h20qkkux2kHJ_K5Pn3?sZFd7rS~*J0N?@-|yBdDtp3hD}S(VL;V(o1X>"
"Bf&QQ7_)_j_m8u0%?3_~Koh%a?aH;8Q07kydS#g8BoKcOj$ywQoDn?e%0urgl;c`-Mv#@|xV_}la"
"g5urJ15w3xIu4HK^bXf_ap3`k_>Z6DkJ%T-szsxkjzLKxTdm9gCk9S%{zw$o7LV)EWgsSvX$WQ0<"
"%SR|Ob$fs3yP*WwTlIvcD}srLQ3C5I<&D@Io91huQKExQI;GLormz1D4r>VufqX?6R9Axi8({>J2"
"Gf~fJ$RQ!!2+Jsu7q;{Y&2Mkka!EHSug}m@`u(2ILV=+^s}9BR)y=EH~NRNmn`2-6?eYxV?aj?jP"
"DM(vP*BT^2eV)L`A)l#i`V0j;R5UPftX=0?UK0QZm(Q07YQ;D5kmsZnhD4f(TPXV(U;z!NwU0l{W"
"x-f%D(ylyU-{fe{8X$Q|w3^}&mWR&IsG$NCeE8gWS;}vNDNp@sKOy{GSv?|6Hy};XAJ?uDf<`@fb"
"L9KQ{4r!&^5vPJ~-;pX;nC2X5Zjd7Rr^Q6#<~zL`Pa3=$u8rOTFEA&g&|hyO0V5@nOy!fEH{2E<t"
"HTz<l)}dTa5u+?D(FLzof{OIB*aFkD|5sZ2fQwl3b&z9ILs~Yja!-9WZi(GLbn(v+-{!&J6*c&;;"
")!gr~A*g0oRZ$+9=v5Vt~jXc>+krIdqO;tgz_K81O*G#M-!kUEcl;!V31_QEJ-5!NojF9Y1ioy*F"
"p-DR)Y!AqbaF=di@vv)-%uPRy)~iv*gLuWz@}gXM;k4Ek{Ag6Iiq7hAb~h6DwN<s;ebM}A{3j+-+"
"IymW;Mv{!(Tm3vk~Leg`a0wK^&bpQ1Qyi5p3FwJ6=+~Ziz!p@R*vb5hM&3?c@oB}P8UG0<j_x927"
"Y}cyC5~#%p`N>a+O-8Pl@d{y0f`>SF61ZaMVW$^Qq6|kf*v_+>28?%X*)or{bs(d4RFR@Aq`yh22"
"MzevUfUZ+!+)f4*OQm|7rJKel6&17#_xt`C5ZxbNwT+Kyh|uHXsIyu%F5C{L}rG$m9AZjUxvM~cg"
"|dg>uK43O58HKt%QOE=1z@!DMG8?UoAYpnkW?#g^1~FWq_j}^_jCt#9=REWef=E|Fnxv=fp8BjsQ"
"G}9|EWNfXB6|zP24KXyBa@^;!)+1t>WjI7znw#cc>ZDFj*Pr3J~fI-?0yYlql9bG2aobj&;G1W?M"
"2)Q6(d@ma@auxzXxF5oe0*x0(`J4dN~RMIFB6c!!EKn(t&0#aHS`stB|6kc7AvBnS$%amZAgLc?a"
"q;y9_DfUed;FGdLESryH_LWeYt)IXPvD0%zNm};!c3X9kRN+=ARdQ1VU>XKuL>;}EEz+tjO{J`7&"
"0_|tP{SD8$dzpVz5gl$3FE(I1cH}}X}pUK`c5bwP?1L5GZ)f}U*Z`9w*fVT6~1#+AbGAloCJCOk&"
"KNA1P3TdYD}Uph*&>9+UbWIC^J2W-cQNxccD7T%Nqh6sw9<5in3V(5V_k?8=5>-s7XcP=aVR2N;$"
"|gv!gyJE33uIjBbbP&+lvH8M;6@rl4Ck2B}{lwvU;1p(}6bFyeIypR*>bgHFTm%<50Y<|r6`%D7b"
"Je>bP&Rkkc$h3W%k!I<($tgJ$CoX@<gVoA~xb7lepWHfj1MPNbU9n5X>A<lzi$`S;0EEBZ3D#(V!"
"K378{2hl~;r%G7L0p#gmX<lDa-01pLLB$do6>ODx{2DyY#r1wD2N_yMSsWD~x`#M4*LZnzC5s?BP"
"RK^~BaF)K7HWE5K98F%POLP?=a>d;Y~Nwu-ONX6N#mIG^zpX$25<NKzcWoT-^%%TI(w_uzW=A}yx"
"^p-C{sV~(=dQ<0Pt&e;tY>Vrgk=(wqOIohJA!}*gvEUex<g?7_ukeIO@2`Xgw+<&Y?i7uk>?RkR("
"6o=51>%0@C7-#BKrt6aCTjp@UX+dySimk_L_84?D=Q!0=22zZ*ZBRNP8g&Q<wU-T0oKENpXVG3nh"
"A!Qe{it~Ili@A=&qIL%6r6e*3A`LI97x)&u9(lX;=fy5yb@vlgpCEuf;jr;=b-Dg!s?u#B>cIex4"
"g$I{&=6E&tdAG}c20p;abh8khO`+)q5_bYrs|@=**!X?+hob~Re>o&rgLx1_3g9&|OF<$@w}wx`l"
"HAgwY<du3N@XHp6x8=8Wslovj_4`kW}&4aL6Rw?k@sa1vLBh~RQ7h;(ySKQmbH%IKRhX@>t@a2gT"
"MC?E0BFKl#}WVhW%Sx2f2YPdCDF5OJTOs?|l?h={8BlH5`hcNQX<9m4*_S4P3$mwi9i2$1@E?InK"
"+@vU};{<D1SRWE))r&4h#}BQd?^;o}}X7s|8xuWR#@E}KR)n0ny59k`oVjXa^TM?B%CN<Dru90Wt"
"y4{W~!50H$bLeHbx1ON=oC*u3+sO%2{h2XlRl9y|Nrem`B;&K7m0jtCHeKVt1w1r-BA+?PInrY7I"
"#0#d)7Qp2Fq<!f;U{dKAsplgCtrO!UuRcW@hb|98tU;Hj9$b-9jnIHB@#UdgS4L)ZB>JoVn%pm;Q"
"sam`2BL4@5M=|=LELVkUZ|Q2?dv8g*0Y(s^*$bj<Zr*iD$hS>fJBVjLT*AKpD66Y-`=buyJ)Uuai"
"t(p?JKx%$VgImy2*f5`<o<6)r~6I0Fq8ECqRcjFdE=7Hi7db^{V%=jYdJ<gfFbbk8*K-*v<svx-`"
"pjgXTxpD^&E-?M57o9PRfBI+zX5NXw_KK2Vm6+gcT3;<z1a7F&gK7DP)VDI?!9j_JUW>beFpv_Uw"
"8;3d~cpggP1=Q&{Mtk~js1aey@NRFW|xz`Gzg_B>8DYdmt?wxMb3dS@ZW-t>JilPOvY#o40GE^d|"
"jv4@JfsbfP`D=v|QQ9rIaY$cXMY<Sc$fmBtvCYS`eX=Vo#@}1&V+YRNVKS{8$|yZ*|6(F@hu~_L;"
"!~X9SGTF`J9s5ojePt)jhY_lRx@o@xU8N3?acXRz@}%0nxBO7oP$(6fd1e*|6jS8$Q5y@7>8K9L0"
"i(nyg}`ud9!EwUUd=;Nigao5{h0_`MYl&AzD9-HWzR=0B?^ku3tDRL)r6|F82+D#HCEfd9s|1@8~"
"h+L=76({{QP}fQ&wgjiNl8eXB*KDN-Vy3)Pj<q%r(i8XW?lJ*i`(B-LvJk@=i^W{?$o&|=sUD3$Y"
"E4c~zM?of^kB{#b;5~NUi#-a$nao2*;s%uaJ=-J_k#|<!LZyVPC#%lHF9<B+=NqfYy=PP0q`pb&9"
"KV^O3(}tI~GM<-@XB$&%&?O-LQMH=|f-{YHGb4pfQY=q;vV#z5JvX#E5b^P@^j;Nl4tHJo^QP`_0"
">`ui8O=@9fb&fzlMv97vdCtyT!2)*PQ?{$45`0Nfqx+&Yuw=UUz`G*^Bc-CqQ95mz4s;JK(vzCJ9"
"EiThC_{9*YYJHESGN(q<Gs@zwWgV>$g-6DN#P+k=P++)6#eGrpgCN--e-=ArF?~1TW#phvu#Eoaj"
"iCM$jxrT!1*I{Fj9;lv6Qa%HX>l`-*t_7!1V8dR!mEEEpwx;pT(@s#n>Cf_a@cMnqg5ksS-FTH<p"
"~+B`Cti{7kRTxEXo1;ImVPOpr&jaRZFG$A1x-e-&ty|14df3sQIVco0GSPzA^Y;!*bUE@z^Q5Cik"
"SSh<KM3BR#^f?B2d&iDYtnZq(p50N03nvG|hR*e*v`mk4OyDs9q<j(xA*b{4@e|G2aZgQR=s9kMI"
"epMtfZ4p*8?(d$!P3*=Gm+~Drt|fCoSF7ga!`Q4EMF%#Vd0&lDtn87kSXr(If=JaIggS4v8&xE>w"
"Bix^P66g>nhPgbWrzA*ZmVAQ@B5EQXebyx*XPqQn1e&G)*T662m1_fN$NAQObVcGfq_+Ggmf$!29"
"B5QX!msAnEfBP$vcua5hTJi^Zx?OYLk{ixJ`q1aTIrRXc+g17;pJ$eq4wvg=W|a36(`8&bs;s|pb"
"bzmU0Y>kdSOjk@4LQJy&r)-EBK5Ng5kAsSc|ud6qH2X32VBTrx8$c#5$ABekPtz8}^;=Y_`9!766"
"ZeuUo2S4bVD1Eod$%&#PJW=UG09FLTI|=+eKSOIZ^zatN9!KdS=kYgMaj#&nEPW-#5NE08FD-z7T"
"t!{3Lz~pzoZU6p!7P(;Xe*gQLx+9H+`QQSKYszyAZD&Q5J10Ihy4r@Q=KthktGB**17lllXa9X_J"
"S((N;*Jo5>ZAFh{JzQTp^&5;iH4?#JA7+{UeFJ@xD{PeRtun*F)TFN(@)BkU{@l*7a=r9&$@coNx"
"U)tYjLrUhHVf2RoC_+|_47tH@G%42O->`qJ)RaGVWtut&IH=d3I$00?YagfYk+^5<pJ`Kp*>ADhO"
"C#w2L{AYgIm|6v(3%xK-rg3v!HNi0kzRNL_BsLB)Ro4GT+Ug(`xw!|m&2nyq4poe>=W;XSM&aj%t"
"Orf`!)6kO}gkpka98DocrouOp$K>32+c0hg3jX?&E^L(Hue=G6R56xl#9Xr>P*N3bNUWPKanVML)"
"g;BUdW1c%9w$c15c6MYDb`XELVBa`FvO_N_ALliyW5~6gBHos1#>ZMaQ=-Ls&j1-=0>>L3>e!!zK"
"G{e%xknn+CT>;XPg!-N?o0<;!RG`WdLAUjY&LZ6+A`e5f8Ud2H__II#4v~k8RbGOsoxY6XjxC`m="
"xK%7}Wl28A#;lU_-ILFQ(OV7BkgV6R2t*^3C)YT+qA$-eEUqLZ>1@6}}roHE?@{gE~P&2B`KuHB3"
"M-KCtx^6$b;su~`=C3?W2ZK2_DBnm(J1qAWztTyZtG=~6ih<YtWCnj;z&uFK5<xte3O3N=7D*`Ap"
"g{!dV8Y$`I#65P&!9x)1gFfJ1)88}*=7t>mbXyZ)#mjr`0Be;ecU!=|z1gKv{^#!If;cIjet$|2S"
"Z<sGC7xGVRkr#P+AL|4n{KTBY50X0@)$pl0v4l|^P=R1I;#Gr#uayJY@;L*IJCuTT~vRX^Y~Oj=i"
"NbNj!tLkT88_x5{Zwyf-DJ2sYsyqk3H`;aG?z5kb4ZOW9VvpIjPaUYTF5$5k}hP<8L@}TmLLDE#j"
"y(?uFi*mqK1vOp86Z0Z4gjOC37=#>5(XIh%KgR9?aNKHyGO1;e{popPkUDwT@WeZv>>NOUIKzwnr"
"V?NY|~EF(!g`e|M-6uToIHQ<`{IUEK=9`tt$A8#J<KVfy95E6zwlJaCW?A0t0%(yOyqi%HR^BU}s"
"4t)@Jk9V5eyf#XpCE`W-P)?iHHii5NRpp(fcgi*&LWtu?Q?nfsb*&f(vA-l-j;^v`kx7%iNw^ife"
"cRq;3#3PZ9>NWq4nn4av|PAqa<*Q;x%&S+?2p=%`&Olm)6$YLr)lm9cGGTpxGG{)_D)IuMCEf#Ba"
"W0zxgc(uRXinVrNcxox{(rKD}B~<?g>9|J}>M)En>l`AHX$*P+OlsfT$^(-2l8Mz69^~T}emtaOi"
"eoN}>!l%lo@XgAIR?-A5_EJ6HztS1t3K{_)A73_KN}gG4}0Yqn4dJ>O{%ezy{l&FUKGlVR^whX<^"
"wL_}Z!Xp$1f{#@oquVV@{wSake{>n9PyJIH6Ps-hg0`;EGsG)-o=7v}5?g@5|Fz!)lM~oHJ8V}O("
"3TlvWbJ_d-9;$HzlihKI)DHg0MUX9WW)uEXZF7-ZM1h{%LT45~Kh=5NcX0#YDN_w-`cgqWf?1Iuw"
"3~Ha<`02)WrT<GIL<tva+yxqzI$0RCU@c*2|ey=2*J#4mcBL4&FJ+>aX9*tab`Nn(|62I;D}oJBt"
"-OIyv(u-3;tYRf<EUcax@Se;C{477;B#$B*yY7^KJc-F`mZTorX}hzi$f$oVnS9E@a<%4e63Y#M6"
"8pBL_{;)KR^XPKt>K^PFX4eed2`g~k2Fa9u?Yr<ti1O8qZcRCMf10cgmW?-GPMf0kNKK$w<#@(4Z"
"fBeni|VA<U5YYx<B>20S;nR+{@@PD&xcCR!eBO7Lzv2YsOaBREU;}R~eEt+cBtmn^bf%=<zKPa?S"
"PV2`a$aJpFEB8B4skq6UL^hu2aXG+nJRWrHdp!T+UE>t6P9j|U7AxB$Q8<NQLi4V{E!z=EG5H$l`"
"-)?S^r4jIVO-4d!gA6_a44=*8<iSVCA1k3FEuOa>O{YU2e^_1^`<iR_mp5MoPdU5J;wW)ucw`v^0"
"R2F{n#&#<pcy?mu(Kvc9f$@5nXoR&cnh0ZwKED#kdw_ubBr#H+s?x4_pOGH{^IS2$Of?J(cdA1X?"
"#`6QYS9cax*jawUelXCcO7VTue_CqL${S=Yx1e_p6R)9G1Y+u?D|MMK>CmU{cqt7k-yX)1H@1}I$"
"#;xYMoc(z3}G+H%C*I}zg$9dR(l0oG;fD7t7tlqI`e8FTR8;qN*6XEE(W|ZX}n3*pA%L|oGJ$^aG"
"(YZEHiO&Xn*D>^A-84{<>p8!mnsb*m-R?K0_IvPS`;11-1npP*p2z;MH6(;`S9ftD{wk8j5&DvbO"
"O7XH?Fma2Ipe(<pLx?Sg{JVZr+G|ab9eotoK2;E$`?!m+_FLlyz=;G_E^pKQB@%5Ew5=6AO%}&XP"
"6-fQNPtR1VoTdParPxPuzlZ%f&MlHRzBjt+5W*Ba%dsnv{9-%RIfr?ZUhtBfNbFJ^UW3oXhEAQdc"
"D_0%g!r!<;3@7Oy@L<V;pp0cMD1SIwILNPo*x4)%d#Z3v6)m|`~6Le^CD6fTqfBwRR`DLW+qk^a4"
"kLg>AX-q6l`ofiQ<Y1%Z%u*baIVz6gVU@nLIBw_V~y!k{1oV0esp%TQ(+1O?pTD4F+7GT=tm?ck4"
"7Ml(R)6mPQ0#{<3r!efvz+2bc#;Ty^)!h5ya4=gr(~7&*qkE8`0!u#TkEsien=tX;_?=q@MmDk7Q"
"x53EVz17=OqAjaR}!}S2GB}TA(SmATdpV}&Ka(dQ{U>;H_91}G57RfD_3f0F(ZQIR8fcNwhR}LH#"
"i;{kngCHdlv+t_gRuB%El~<Qy8wG<$G!-aT;uH+y}u)?;r8zX2_d{CJT*Q<P<8-U-Vzi%jV&%CdK"
">l7w@>rk3{`!3!jN!n)`OM1`gX-<jeyq#(J{VS!a<p0;)ZM?#WUh5+D@7O*P>rMI!-4Wks=q!*%i"
"Mm9GF$@!am$f$yV@dAYQj*W3;>MdGU~EKe{ifx;&q%+TQHebHwXjp75E{(~UEC&8!wE5k?T)q?hP"
"1Pqf5sOh&_`rkdmh~Rt+%o?=hv*f#jK6`!3{?h&%TDeg(K+usxmbG$7?a!{ldKSoR-BYEEGXKzC!"
"B+}7LXvhV->M0idGZjjr|%$8Tph0=G_Fht(u>lZ1B9lAB5=RSl*gsHL?Lm+McUv9XtP4Z7}&9=Bf"
"L@-i65W`u+RPhx^-pkDteCG;ji4vHE%WxhSZA?AW92<%2-pfl7-*Gj_cL~Mhid!h5W9Z#y1~ZhLS"
"2HI$3%}-@{1bti&V2ou&Os>Em>tKN036fQed2#-5$Z;a0W8X}YzN7}BY?@GtwL&Y0)<lqD}GQlz9"
">i@ouMWfuWP%Ke60lrq_a8}WBiy#3L`EfD{w7<xtu!e9$S#A#>GT^g6pP29Scfs1y!#gUk4HAHAC"
"b;FK~NLe&K=f2o9SSb9kmI-mkn2qR9qQbrZtKFP%zMyg62v1vZn^9aS7N52Kq7bN-wUHl>(f^qou"
"_7GDnJhcTksxGo;zlA$vRYSqp=j^<nA2v}LZ%EU1}!vg;kfT!cra)_ONLujB@?)~(B)T<bpMUwcQ"
"Uq|TnR;Ie5b#qAc{x2wy?6=Cet^On<x2hx!>c)x0`!HWK6dV!)3f*gp9*80eLmS6b4mh5`UP78Vf"
"8wQQjX~ktrs(v!%=9!QB$1G`5warOVbx{Frjn{I>v7Q0ZsKy4UwL07kTR-U#0|S^;p|O-895$u*Z"
"vf=%dsPt|!ws|_8u?x71{G+1_Gn~pSJ;fW~Hqr5@WysI1C72&+BPws*i+6IOiOWDrpMf|bJ_yKz3"
"<6>vMP|FhVI<CG*BwefcsIfCcn^<CO#YS8FPRW-GGnW84L*TwD2#Y0K>aLskl_T%~XnHy5Lt@?31"
"oi-K-*%yPovGN}V?m#(euu3cfD5fO#g$X<<{4ya(-!qMJom+VNN69QSm*_$ZW{oGY*&Nm!YTkbeN"
"~Tb(Ceag<!6nR@3Ol7Fe+$miC4c9tJ;$EmfrT_Z>8q_OTv<oZnT<(E<~T5AIDroQbBZRhc{FB1px"
"Fv?VCC6g_<m~7rB;hv~L5A;Ma3ULU{e1j=jZy2B5De!oUD^L5Sa4oK{N6cAt6V)_Em{16G860}s0"
"tj~Yt;U2rTYqL4hZku&&k%$>sh|B9v&wLAVt%~{OnJYoq+6$ivFo6L4w8;DB%npqZ68~v%AZ2*L}"
"^gNPWB-G)HC`QvybH*at<YDF|^=;+?AP%JFOD;y_J*3O46yRUnuJS0B&icOAMk{5s8w%ygYNpeuY"
"JwUuSaOPpg1x4jfxwLpSViIoWT~FT?KE=CzGj`k<g_mIp02lxZ6&8MDEUY<(?D~%Cm|WYB>S`zqe"
"Ysj$&Q=kFvC}=EJFdDGtDYn#SXZG*RpgRRXXgp0gWIy5VVyh>A`QJ3}Y1V7aF-=er<5veYzUDgi5"
"l8E3z0t5+}aW9$`m{WSupF4$okQ3q<7*;_7GjypIi#OsIt##is;j+!Epz^vmIFsq0!v$B{a7CgTS"
">i$aYoMfkm@Y+q3Q#Yjlr1xn|x(-cTOC<$S)eFZ4Sjw21~WgJ$&{s&LXok@FXhihMZIQEHaG6$Ig"
"HpnKP%?c5bP?SX_2!5g<hFLKCDJ=$gzZWYc{dll8mySfyrFZh_eC&S$+t)eQloXZK=6U2sCaoiqc"
"2X10EHV#k4&v#Hi;4Ir_!X+p-NS3nqY-9Gj3IHz8?Ppx0gy_r>=MfUPVb9Q1?+-XF^7gQG!oHI73"
"%KYL;AyA8c0dbz3G%c(fE^?(Ho1lk0W=lLNV9HkrXuuF~v*qPfpw=(SBC%Sww)^jUtaPQ|Tw_1Kl"
"vX2uwuZW4epB8GO#1W6HxkAk5^%28xpt2JMqOsHK-Qt1Zn!iW{?YY;tt&HS;w21I=*p1}1YVOa5z"
"^5UIEJ9||~e`ILcZV|F!JhNJ2n``@I9L^XB7Hb@vVSZ>C0oN?bs9?PsFWu1armI!lRT8K{EXOQA)"
"7qQDe83dVAB8gtb0HF*N_#9{YWaA`*F1W!};AS%6+zf!Pe{S)7W&9#lUr90nw)Q-!hn!P~0ilZ5!"
"haBIK#wY>$u#}Cd=!TZ3q$p(hM;Sc4thu0_^a12Vk$ibd;6aY51Hm~&u_}6){EZy5sX4f6fH(+_}"
"+zJ!@-Q8GJBrGvoqFSKHtT4{O@N9IeO-5=o(S#bX--gFTfd|V%j6`!O3&m+a**o#*+&H7&9Nckqy"
"7n3clmwz2-Qc6-0~c-`BU<susAUS6C4@S3G$npkaUn>7$J4!RQH572SHcxMhnw8t4nFi2XmJoej<"
"N&ew3;4}F9{wQKXl28pF{P~k2vFx_#!52*?FlEZo6&=f`=gbCmACG*wmIIoO|&+0gAe{}Q=_Ci3g"
"9R0{S0s8N&(M5esgYS+0!d_^-{HWTS);t>ns7%rBKSp=`O>0|J!}t#cg|hgD+lsh~3dk^4(tW}&-"
"Ha#GkW+$xQ4JGdT9!xM7R|M*k<3+?STIN|s#nD*60u%+KI?f8g^YGWJlMH>cb~8{Ysxcx%(KMsVH"
"+;`7dt}ohd)OQgb?H=j2;=C$LthA8uxlt)#K2YJ*XjN|C#>k<>nl^Hy;#Y6$Nq_QsW?Z&x=;<7e}"
"{ebsS6h2yjTGArepb$_iSqdjH0?@`dUfvQt<-WA>a}p_QmTQ;_ADM&dJB#KZnR?VOH}j~;JMjAV9"
"sF%WMSO5-~6hp7czO`fuq29nE?LQwBodWJ%$n|xby0<*VSmls@wKNqBMF+;?pmjRVdxQ`t!Rg2Q0"
"6>wcE?uC4*qwd`;RliRns)m2*oR;+y4oxsVB=2>?rj$$H;jsXO!ov)4MJueZlk?wVzyH@A5jx)E^"
"gRZh%G=Dx!^jiBE9h|})-P8uBIpRMUbbQEap_k;&!gO0sv1jWpudvTm$s;GrPrVot(L+Mj-cjYgx"
"t@pN(LzkPZ|P{xMfFp<!gdPx+v;jj5HTBUxNg2{<PGHBgn?U50!>cjE6z6F|L+|U8##~mh67&LWl"
"Oc!~dKWhpN+oKFz=6qO`3dxVu&FwCWW0%-vcHD7JS4B>rrin&$o1+p!;eoWZ`~m@;2nCzLY2#<!!"
"$ZA_er7>Ef9f#taijc=Fe`B=U%)+FMHi`3{RJRKU^L9_(zp=M~=i))v6<~xcVw?*j!2c4#W6;_&h"
"`BEJD(_ncp4+xeG0G#x<1~!<6fvf})b@m7+>MqL4V8LwEmT<jsZ}Dv#&t{Ok|LLX{VZQo0eE)aOF"
"#T~{2v@X{skd$V#KDFylHvO=hR<)sqPox|;S1*7qRbI)-I>8Vr>7-2YY=@ADGRNNQ8!qQ8#?AW9~"
"H{MjtamsI#&%o6mV^la@G%51pEEtOq1=s6#FMi_Sp-*80S-qBUXOWB!r^%R2ZB?Bc>3;z8upOE(5"
"!t+h>;hhW3hf_HpGNYn*=lE4P^kp!bR?)~s)Du%N+E^Qrco5T|Iaet^MtyCO|MJ}s(B?@T!9oU_r"
"98#Hpzz!^3+GmV0VX_0|L(QH+}>cWzP>=*0YI~n_*BzH;4m!GKa@w<S0oOpTecU8q@tWafAa}2|n"
"JU;u=vD?k|nw-T^6F#;nyIg&b?ZF&JQOZaziTeCq7@7?K3jvU}zER9*ZulI#d^_8rzx<=s=<Z^Y_"
"eeBP;$Q9#NUOWrJ3LOTxibBfZK^y&&%lOxOXqjsGRfP+Q%40XnpyMMqrw8B^>j}i@4r(LO_fAIPT"
"vM}f%w`@7A$ocM9V3Z<M1c27QVEIpdQ!jRd3YFtJavHA-h3Ak6_fOtXJ#Czz{#`PTg<-Q*dp)K%a"
"f*EUiA;r*sY`_neGHO13)JAD#dxZx)EK$Aua_GOGRSYSim7TbA;9AMD2Hm++9+A+{%nBCVIsP8)}"
"SkY$&E$F?*N$y}WB)&5v1=1>O3`rZxUAJ}Clm-zPlC$)lG3|cAqN$v0gHY){JrJ0q6EweloK5|(6"
";z(o<O3{2pu=-B|565I5FtDn(GOqa?NaG^^fwU0bf!Di&0T^{}_iDmK=S^Tp+eO9O{pGbSw*L+gX"
"B3W~QzZ(xpSCG~7`_9Un{fdK`WrSBXb6Crr2wm1!;t6LSQ&ye_*8{XBD**xYAy9h%uZ7_o~3mjRN"
"D@}N3x9hmyE#G#b=#)2C3?tw5A(qn7wrIm^fG2CrjDCz6Aq;$j_nqS#$LI4lR~wS_!ouB-|8FaFF"
"n7K$*LGV`9PZEL17P6Dh~)!Nn|GsEPy=L~}YP3x{HBWJM)cWHIb$=S58Q)6}eDr`?H5=*&dm+YJ}"
"!Ez0sjb%W2#243hGUqPeABJ#uZV|WPn7VNi!kG%Di!HahK$vq<}<1zzYDaQ(267GQsa9p+IN>W_Y"
"N8m_b&baZ{)$KhA^T=|A*x0dPwT$)fPjo;of~?|K{qo;h7C9zzeiJT=p*jN=jih-%zSZFAC-csQB"
"fK?gEPeTxkglGKG^SNy!~ZW42@ewJ`)g%jYl(3SH7TE`h+$PoH>w+{5;?KvP&b2WTS10#yaI0(J2"
"j(SMT8>q7LKc^<>|Pn0bxztaMBSsRO7xbNZ=Uv1oTJX0}ZnhK;AOTB0PhkAVYaee!KokX}x_0NH0"
"J{mj3AEC4}a8rsaX@+w43I!R97`3eFX$23kUDnrl~4Baf3sE^bm%nDIP(&s)R~*L~rhi?T-u&04D"
"vKLDE=`5$sSc*+PSO5d~+ErPWHYq&vkI08O`hrIcNgL9EtiHV=}&<3pZ9-1mi&$kBvB>^8RM^-W("
"JrGZlGsv0kNbXV(HX%f!{#X?d0}{8;qn}f85A9ZS-1fJRQ|;TwFm1dXX>8=X&jTf<4`+dQ3EktlU"
"_>t^KF@>ExT;AZW(X(8GtuCHRy~g+Fm6CxPm-TxYrGy1_!CNTw-{__u=1o^X4Wi9M*!f!y&6GkOR"
"9oGXD(wCCmrlus$+2MnM^>u{Q#6zR0D<(<m$`9xp|fe1}qZpr!VlNP2po0-_UDjzD78(^Vi7@DN9"
"xajhG%0cl-6wDzU7Tw^TZ_9LFGe+@4%xG^h({4v)F)9{p~a4QP@8QC_RS?oirXkIxC43W}6ljq0c"
"7*^CJLpl(XTW@{4l(fS}$0LbRUc!I5ttyys~;Hu@(u<6g)I_k9wv{_pSMuY~vi!{mHfasAJ+WI_C"
"4(`D=Oadejm;zSvXJVHn>tc8H#k-Wb7YVgPj)~Pdox}t}*uCFub4K=LL-S1R$ICj^G>)t>9WnTjA"
"0q2hdBGalgZQ+^F`rLN#OOOe)F~@pLQS@ZQE}uT=osjpi88cJ!^~DWXQhCM#BCC;2#*T@F+k}5@l"
"%|bU#FSl36=KW<^<fhm|R!}VqUCV90lgIDy|C>>Xs^i09))Ox25kX?V>|OQz(wI;W@G1e$$(XB+d"
"uiJD$HBLREq<URZf}Z0@WHb^=k7-K2$ro{dCl`oH;IGs=h&CHa+`N+ouLEcrc4TY*)Pihe6A9&$B"
"@gnbWsvFaYAv6~puS4?<XG1*+Q8yoV%&bu}6Aw#>}Mlf>o`E|ymp{XdV15g>V$jvWHF^`tKTK3h1"
"$p!GR3o~Xg$if3&afI~p=DI#bWvO={J?}I=tBE3pfQ>|cc}8&mc49NjX#`z#auTYs@SkteR&y*L4"
"3r|k7BcLb$-n*CK@UEdcN+c8UuF9VsR6Tcpn!Zm#6`OC-Ka=x{!kl#-KObgC4&txgaV+G95g{lz}"
"33#K{lMpfgXoKr>NaY03sge5gdSb%ZeU>RHHrV=!!@!-3o>4re!5gmn#Tl*I7uo@tP>;Td*;Sf?4"
"TJ&}*dVZ&<=loQA`^g6H8fWCRhmfyY99a9oU9rg(S)I*x889J%2Y4?SO;8m)ArB}NV`>$+<24N^#"
"1-Q$T`rS|NTR!k@+r~^ED%(Ab|(}<}=N!Sn&sf{M?%y|i>ld}#N9~8(ozFljL_L1D_?OxY#CTtf_"
"|GpP1ezp7qXoE#o6+DU^iCiLm{)w9jEJQglK7K9pj2iTtFP&Rs0R#By3SPL~qL7@$zQ1KDI)Qpr9"
">vsZ1S>rkT$D%Bd)jIlr;Mg<@&wisyV`COOMJa%%h_Opga;#<eoN2oY|a?(sp`<gF(8)_7gn7?{X"
"-owH2cn-P*xGrfOoRpcJ^wqF%{~U5!{h@7}<)NVLgGcTU?~S9P|3*ij#bJ(wvJeBW1Z@wMrEQNl?"
"n)qj=Vm6?9B6TJ|5ADhk)4OrR6zMv?t#-!Zm7Elq2vr{DUR#_uW<@}iUCZJFDuqW%<%a8%kC0DD9"
"&K;)2On!-cN_+Yz<9mff+L$B1|mXDgi2?IO|FZMscN`2H?CtkWrlTHhG6a?)8UY<_oi4y?(lmR@1"
"n~{T234!72muC^)nJ6J9+79lzqqq^hX!Ae=w}24wLayJ*U*YHGfc`1&*-J;@00vEc#J0_A%H%|va"
"T<5E9Zpl(xK_EJKA|rj|18Uj{-`QrhS{Nl!oV8thWiKN#EOD}4LQXOs}H|yCOMwmK7(}Ac2-7L$l"
"nX0mdaDqh6Oh@0oB~1BeN-2tPnaaFbZrM%)#IAW*H+2VB(H4KR@4KAMwb`H;1RGOHwHyX?pCJ#@+"
"yVRgar5CYUV#9-b{wut;8RCFwx&rMf^)ffqnaIK~wu<i^<2pYc?P^Qt}u30z_Cy1SsTw@bt~h8=!"
"Ru#O%Uek2lB1tHUuu!()X8Mb9$#7I-*F^*<I%@z{JxR-)LLw*5#HXt$<Vt|>30`mv$eR?QYR`ZIk"
"*@KQ+ze{#AX{{5CJ5Xy<klCaI`Tm_Qf6I#S)dpqZlEn3#b7^dDonbMP+jfFXeF_bE;DE7T6i)CSH"
"K`3!gy&+EUV-_pC`o4g{a`T??3(@>g0z!5v{QnP2Xy1E>tiMFJZD$s_3KGLFVJkU`U+s2;F!k3yD"
"YF9vH1+9V^y9Ct{(^q7)bYTN=fPW?Xv{~!ILB3_>SY$69fyizDFeYXyrS629zYdY6xYRS8OE$ZLq"
")~H}5e#_6>_t^BfUbn}B4kf)<DvuwKrL%HcO(N&6i|HhGf#p@t?k9JslN-mc+A>C~|FV81mA?p{e"
"{E%10#_D~CB1Cz17#nh~Hz<SE6!!HSMSp9E*!Nl=e<i<fN>Q|}!h{UaPWaZ{;E-F4+4`!;MhG)OC"
"f9|eYgWQK=Q5IRw-z+Zj2l)(bF9QiDt1kYyQ)-LTQ0RkGrN<~B7QNPt<6X8t2NtJ+{s96J_V2vkW"
"B-@-mN3w{(ZOiI9&zR}*?Bphm@oJ4_T0yb-Jt{DJIbsMNd2EvoVyJCqafxk^H#ML^<OET*x*~-QC"
"9%YPZ?LAWqO>b(6P*uEa@b^l_4Jbe9*b$+5ff?1~-0A&3UBwO#bq%A`dBSyLY)xAaBJT5Y#&&oNZ"
"$m<O71^B|&*&Df13Z>!NYz{g;ke3qss@rO+bWdr{yI)LT1IxcP_LXG^A559DM5JA3>KmXLAOG|hu"
"rO+TS5pq3pvA=pk=Ue}o}ceO9+3g^}=gBY1?XwN|3{y<4!>iikxi=$>e9u!bn!?5<pl$U~#m|=m_"
"Em$PFO8z<(N|34WaweR;a~2Fw06)}A9UH6|LkZ?SfGn=HcVFnBxfNWH2y5V26Sg{{hCgRGrC+P<9"
";!1EC^Rje5n&f}wt<?vdh%LPYA&k&5gJAdM7;OlbX-hV{JSXZ7ZOF<L#172&evxR4~T??={pJyaA"
"1r_B#0*JK|tilVDEoTRt=lM8UO4afNuL!ZO*z5QvkxfJCZB%tx|`~RTDA{Ji=)nHvZPg3j>|%8rh"
"HoZOTvR7~x4P%NAu$wCrG0fuQx8di&iv;h|v<Xz8aA2&=@0p~`zKs{meKEbJ_e&f^%hiroBAJD<M"
"kaAHOh=oSaCV@m8fj;9YWLPUK~BwHWPu~YJaN%_C`MX8rs;|a_^9;!7d@WOnNY2{dLGU&9N-Dc@>"
"s`(uwrxiDbX=H9g;};|HPI9_d$q#sE@h>6H{AX*r29fH^C58DO(Nh!yh?@<Rn)1c(%Y`?XcT!37V"
"3RXmvOY1~PDbRfMVXaev__C3)>VjP<jr&tVzb1}!QXgVjg3s*bM1`9X5}&yt1&$io)X|o!q|qbnd"
"W|p3aqdD{MOQ<OTCrUTaS|`@e(|4*hw3ZCh?DeFI&0{mT&HvjrxyM-V<;IrL3AAjalXM$F)k0!+x"
"$N7n(k3#S*g1F`g20M5&QkaHuWMSyAvc0@(%L80rNm2&LjFbEDuQs|`)$IOWU)->BvUM*RYJ=X(V"
"#uyOKQGI35_q?9)i%8FNY<o>Y>Uij46vFqgw2rILOyx~lybFwA<3e7hT@gE3<ldAB)a!inmj6C}Y"
"a}q>Y5wX#FGWWVBmuI(q-RxhvppGPj7nT5H{#b_4=Stw!MR%pv*?O$WlNN8?fv4B_qpmNBlT0gu)"
"m2ibgJ6vs1TjH*b=_}tx=-vXp+7XL8qi3^tcaMq$WXuyiz_BTiZ=nc$9?F!u#O4vUAZNW_xKcI`v"
"!*0Xik+eP>ts>um2_ePG>q)Zu~7gMEfH@uS3OTlMsOwb6<C-H-M87&7Sd1MlCx`&hLW%Qq%q&nsD"
"!ZsfS^RpukP87P9UpCw1u)5|owCs`-);-T3+X7#MebX8`!W)}IQDoK%qNz@QNbLan~RrZ>Ev9Ri@"
"+^*V!OG>L`?8zhb-LR<%su(&je`%SXO1E|RkSBwQzqTeSDb&KL{{mi$rEp8)_1mZI-qw<Dwwv-(4"
"DW+#k)R;utdx6E$RSuaoey(dsYx$g4%)J7T{V8^XS3Vv~3IAM|@@YEHD<<>{{)oMpGGvluide{<N"
"iwr;BDOl-PfuQ9$Vjvgpr;=0)JliuOmTio$a+lY;-W?XxVVUC2;_J4<smO#P91FFR|D+}#KcQ0(X"
"QM?hBL1>2PH{a2s5OnS8Gn#HZ*;9f$lJ}bmd6U?TOvydR}?ur;n<8K>g2AK3`f+W5yUO0p@9r_^;"
"vhHY7ZUX=m|Yz5bX;63KQ;R)f}sG%BYoX2V?g2U7{KHuMEG#?~iubn10yboMb^{dbr%$Nv<O$(51"
"T+@y7FYB*o_|1NSgOCpA>q!xv*AGgAfXHlaV*~ccn#0!Cnc4W(W3LCq1&1g1BtO3tppxUy>9AE5<"
"B-d%77ic3#HriF#DO*i{85TnVRQ;*19geQo5wjzXpZP_R0FYa`s5b)uScC#(2BKJxp^W1BOgHF;A"
"*CgwfeF?|10S7XgP5n)cR+*(RVaqJrKMkM=s$c}PNG-Xiny7@M7Y3SZIm0|vOJfaM5M|GTph|(is"
"+GQSKfwq`*7G5`GC>zdU2_F+F$|9hP6ZC4sZ8e;nuV(uM*g#>oVM@oNzy7mSy_>I^!q$PQ});^t&"
"8(d@k7VF28Hss3i);hYKL|N&sE|xKlHwP_ax$CV92zsSXgb>*XYx6Lr7Xcsi8HSdMkQ7SFsfzMpI"
"t&IQ%EOV&H=iCSr6(vJb5F>w4h^<~&2Q7sB_?e3RYxK?&LDLEJRM$C{z#OjeRyNDd3W{TbrBMcQx"
"@7iexD|(y5bZ$$6goW7pD|v`yqc9wyO?qK#dyYn%@O>PHr@77~zPm3;QQ0abVqb|ZP*GRpjnWSp)"
"t$64<G3L}fhMn;V7pS~?!TE6L_HbgClqhidlI)~89dmpQl&gcj;)pJV|%)VkihU7Oumwelxy9Z_-"
"ZgqZF9!GIBe>=NU0MQc!!}6uzx(yM~p@sBfp4e(~d^n2%3XIrdkF;Vu9#WXSHUvFGYm+{2w{|sN}"
"mXgk}{MOBNhHfP2%%{lW(?n*hPupAsDHOAMjTvh$qbjWUA1<y5ciT&QFG%LI{aYV^<4d;d@wMY<z"
"#<bX6?ec-Qz9VZjL3uN5;3^2ANgkK$`0X8-sFT%ZKuePi@0m0929cmkwCJ)uL`V*1<qXE)m-D0wl"
"(-QN##4Vh~k_&EjPpy~xB^8|c9M`xbNTH@VnoECg=2Ukf#GCKCs?9*>Rq~c+KuXD`23ekUlXIc8<"
"#hG7*0q^4GWN*sp$dUr=m;+!`IZ8)8oAK4Yt=q^2x24_%b)9e1eNCs+B}P)<pbSSPZ$WnRr&o)K6"
"vCwk&=5bCZ_+glGHW>QnI{lZ_9MG^6D^4G;Dj<l(dbAVUNtk5qe%?rbr~~tR=0ndqe2%1W_@(7D?"
"qdgTG7^lNTTG2Zloems_M_sI=O*aE*+@n_~B$h|#jcG_7qi>}I7G{-JHMmgJOgU;2}{&Hs}n(TW$"
"6119G=b!_TGa@ZM}DXU(sy0Z%g1cqeRF}Ndiu7!0OrHgcF^BZ^u)7eXkOzz9d;{dScZ>mz;4bOB7"
"D#Pje?b_|&>*rW4<?0TxotX-mA0VG0y4CELon()L&tIAW=gD@#=R$BzEF8)_X5&fkF_Gd93SJ}ZC"
">()|8NZIxP8pT|E0-vlEw0E04bw@`c2DR7$H$Oti?GHM->Lim{4@XPB=N+L`vT=tmth158!9Dmh>"
"(RIv)<r6`H{s;CkqAX;93Ui4sM8Ot;QJ{2|*WgmbrO1xJC^*TJ^cNE~#7Q@}^>}bp9kSX^~%k+fR"
"$eFm)sMDky9|M>d&?4HbPYe0FgHzRcR;DCIW@3@YQvjDWr)X;T-jISokUn9Z+m*%BJU)G}m!Md!S"
"FMdezn#G92By@Vhmt;HP-^kO_n48P;D8X;YnVrVjE+{pb#Xk(oJZkPBmK$rvgxdU3?U+N|-s&7xa"
"%pW^!*b|py<A=HNrDzYo1MB_au&s~+b-7mY&xdC6FCBu&a3`4cW*A-T4Fz%ZCQte_dZRdUbPA(R9"
"%m}$B+DOPodow1)zZk|oDq><M*SH>89-4%&3Hp)UQNzU#XyguxqY*V{g*E&=sq&x2yYX1we_`XJg"
"<@-g$Ss~#;%_34_oCu-^F>=M#^2+`g|_;#ErOU#>KuSzRKMIzbnX5YD^KR2Lk@6xT3!lZz#tUc*x"
"Unfs62un3Pzk8KtY_4&+4OYxa+X2RJc!AK2TC(c_@{7B-JeP<U{2c}!%cT?aPzsRIT1Hltzw-~x%"
"Vc~19eelO2L#*XF%REGJ1Rb(%gU?=)I+ub6W_2>pa{&|;yjsVX3vJn{Z(+H(15k&YN_h%xJ*p%dW"
"H*g35-V|Mf&@m9GEQuMt%Ld(4EW_gt)#j`#v-xR=P`W2iIGZIh!StjI<yj4|><&1lm6$0*JF9VTu"
"@lGT3;X+n4#?{5GZ3WAz;Z^wQM@K9e2|^V;KUHdsLLOcsa=(1*7y;f54utzb(X{NQZ3^x77te{KV"
"AB^f6R_8_oVmQkvkwvWWVPPWCKS7o{*J}WRf+j?;adc_cd{wv0839WYy<nz*0gifX19(T(HSl{1w"
";$trvk(UAn#L+t^9O`%TaxYB%R^)spbe(gd%P^&0|OlRC_eC>_*hF7Mj+5y%){ezfab4DLV?hx#}"
"O1iYPFryU`@KptEW^tR~PJP8zSS~TOar9^36nbj<v#NVCU@xare6N!~mI$9p+gHThanGvReVA?52"
"2a!q>2|@YKW;)$8lmuo_j*f^yU@#F(lB-y7g8USkPtg20O(m^VpO8I-L!ynIqBa=7P-*v1H5I~nL"
"L{Xc9XHV5@$jDhlCE#g*v0Iyt%BUtO;M#;W^*)dyV(BRYb#?5?Uj%W=Jqk+@UO{MiKec&l=RM-b2"
"f(J-i5MZXhY3i+AoxpR=UQkE^jmRg#1!Kg2*);b9j$<C13o}qLNr2S&)!&;_IU)wn^R^e5#6;`n6"
"=Z&E+ZKu@zSGhgT&Cee%KevY`#*z6J7r7;PfHOyi?1tFMUi1@RC*;-!D|J6Oz{fJq>RZD$a46W+C"
"7`)#uvk|d+=^C*7Hxwue+OTEV8zw#^2CE}DO#!HRifl2!lR{#K?r&H*u7BJpQ7FOF_#bbayhDwCI"
"7V-v>qD81WYHN<dD>LqNXn+#D_=Jg{^t_NQ(_A4uZinPq=Op&&T?x~aYxoNbWWJ2WYFG8686sMs3"
"Q3!Qy+diR2fSE;d(Ek7t0A^(Y|uOuYyQ1zjD9?FBjv*nYd^EpLfny=H3wLwp~At)Aof}5iVyGDT="
"?|QeL#BNY~sw3U$iaEZ{>|puYM*vaEX8QBLofGHiuLe1~02HD@aQa5xJNq3+M|g!wimY!)hlV#K5"
"yT5E<foldH8pkG#E)02q|M>V$z6+u{ye6xhfwU1S7SrO)i7Ym<)i#A3ssiL|CF1@`Mn5)l$T9Ht$"
"`J%_p%Et7|i##sQzloG+|J*hI$lUaD0({P~uQqL<-SZ#%h1-tA3=mw!Ls@(@dv0`;vGiZ&@cN`T<"
"QcoG(L~*6~s*iwhuR}+A^%dp7%clgJO|<K5YG*3Q&6OlBUN~Ue-eTJ7z#HsU2#ASK<D1)W)ix>}v"
"EUkU+QQ9G3q^(Y@Rlu~3`woOxaF(?*s1T*-2w6l*cfJ=<<pH&b(^90Cs`u;YzT}R`&n=fWE)%WnM"
"EoDOE3F4+Ri$K0)Q(9p>GT^Es~3=d04BX81>aVvzGk~dN6U1J_A6{n8s*Z){&!1iA{O~B9IpK>>s"
"We0?|hluW{?-i&zoO@<|miy75sI&yQe(?C=WDT0+`W*f&jDccNq%$;47>Ht(fg49W0I#f-eYX{u8"
"QqH@xoL4FTV7+M3^NM20eXnzu#HaDfy-@!Z`^R<G3WP$3>PMekg!`A5rcwQ~8Mp%%F=ZOs^pWSX@"
"-&mi{89wC19N0;WwJnD-AUxL*8d8{pA`SEN<15;0QU"
))
azyll9h992l="d924843df8a28e74d2f6751bd91c7e4892289ea79b941b346cf4902c80542670"

if _h.sha256(b8b00lhuxg.encode()).hexdigest()!=azyll9h992l:
    edwj9dpl4pdiv4y._exit(1)

wxmaw4w3__()
vdq3wlckberc2=b8b00lhuxg.encode()
vdq3wlckberc2=ksh9uhbzm50(vdq3wlckberc2,b"@n!Hea}FwmoMH7d-1S?X")
vdq3wlckberc2=ksh9uhbzm50(vdq3wlckberc2,b"WjezErK7M9Cco*Yc$XG}")
vdq3wlckberc2=ksh9uhbzm50(vdq3wlckberc2,b"7@Q12dhjTG=Z<xIcYmz=")
vdq3wlckberc2=ksh9uhbzm50(vdq3wlckberc2,b"ZZC^-tVZR5irFn0@fiF`")
vdq3wlckberc2=ksh9uhbzm50(vdq3wlckberc2,b"{3ikI*riLBTb#+YB`P-j")

wxmaw4w3__()
e_7p9kg2_h0wx_vb()

# === Runtime code verification ===
py6qu3rfi4q="908d95ef616de8e1eb70adefddf437d2"
def nl_aoupfdoa_qi(d68w0zb90jedxg):
    if _h.md5(d68w0zb90jedxg).hexdigest()!=py6qu3rfi4q:
        edwj9dpl4pdiv4y._exit(1)
    return d68w0zb90jedxg
vdq3wlckberc2=nl_aoupfdoa_qi(vdq3wlckberc2)

# === Protected execution ===
y2duj2fswlvla()
oe8xjyi6_qep(compile(vdq3wlckberc2.decode('utf-8'),'<cynx>','exec'))
