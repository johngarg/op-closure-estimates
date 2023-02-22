ProtonDecayProcesses::usage = "Processes allowed at dimension 6 and dimension
7.";
ProtonDecayProcessesDim6::usage = "Processes allowed at dimension 6.";
ProtonDecayProcessesDim7::usage = "Processes allowed at dimension 7.";
ProtonDecayProcessesDim6 =
{ "p->K+nue~"
, "n->K0nue~"
, "p->K0e+"
, "p->pi+nue~"
, "n->pi0nue~"
, "n->eta0nue~"
, "p->pi0e+"
, "p->eta0e+"
, "n->pi-e+"
};
ProtonDecayProcessesDim7 =
{ "n->pi+e-"
, "n->K+e-"
, "n->pi0nue"
, "n->eta0nue"
, "n->K0nue"
, "p->pi+nue"
, "p->K+nue"
};

ProtonDecayProcesses = Join[ProtonDecayProcessesDim6, ProtonDecayProcessesDim7];

GF  = 1.1663787 * 10^(-5);
VEV = 1/Sqrt[2*Sqrt[2]*GF]; (* Added sqrt 2 *)
CKM\[Lambda] = 0.22500;
CKMA = 0.826;
CKM\[Rho] = 0.159;
CKM\[Eta] = 0.348;
\[Alpha]em = 1/127.951; (* at M_Z [PDG] *)
sin\[Theta]wSquared = 0.23122 (* at M_Z [PDG] *)

NumericValues::usage = "Replacement rules for numerical values.";
NumericValues =
{ M["N"] -> 0.94
, M["p"] -> 0.93827208816
, M["n"] -> 0.9395654205
, M["K"] -> 0.495
, M["K0"] -> 0.497611
, M["K+"] -> 0.493677
, M["K-"] -> 0.493677
, M["\[CapitalSigma]0"] -> 1.2
, M["\[Pi]0"] -> 0.1349768
, M["\[Pi]+"] -> 0.13957039
, M["\[Pi]-"] -> 0.13957039
, M["\[Eta]0"] -> 0.547862
, M["pi0"] -> 0.1349768
, M["pi+"] -> 0.13957039
, M["pi-"] -> 0.13957039
, M["eta0"] -> 0.547862
, M["f\[Pi]"] -> 0.1302
, Coeff["D"] -> 0.80    (* 0806.1031 *)
, Coeff["F"] -> 0.47    (* 0806.1031 *)
, M["\[Alpha]"] -> (Abs[-0.0112])^(1/3) (* 0806.1031 *)
, M["\[Beta]"] -> (0.0120)^(1/3) (* 0806.1031 *)
, v -> VEV
(* RUNNING MASSES AT m_t taken from 2009.04851 (see also 0712.1419) *)
, yu[1] -> 1.18  * 10^(-3) / VEV
, yu[2] -> 0.594  / VEV
, yu[3] -> 161.98 / VEV
, yd[1] -> 2.56  * 10^(-3) / VEV
, yd[2] -> 50.90  * 10^(-3) / VEV
, yd[3] -> 2.702 / VEV
, yl[1] -> 0.48583  * 10^(-6) / VEV
, yl[2] -> 102.347 * 10^(-3) / VEV
, yl[3] -> 1.73850 / VEV
, ye[1] -> 0.48583  * 10^(-6) / VEV
, ye[2] -> 102.347 * 10^(-3) / VEV
, ye[3] -> 1.73850 / VEV
, M["\[Nu]"] -> 0.05 * 10^(-9)
, g -> Sqrt[4*\[Pi] * \[Alpha]em/sin\[Theta]wSquared ]
, CKM[1,2] -> CKM\[Lambda]
, CKM[2,1] -> -CKM\[Lambda]
, CKM[3,2] -> -CKMA * CKM\[Lambda]^2
, CKM[3,1] -> CKMA * CKM\[Lambda]^3*(1-CKM\[Rho] - I *CKM\[Eta])
, CKM[1,3] -> CKMA*CKM\[Lambda]^3 *(CKM\[Rho] - I *CKM\[Eta])
, CKM[1,1] ->  1-0.5*CKM\[Lambda]^2
, CKM[2,2] -> 1-0.5*CKM\[Lambda]^2
, CKM[3,3] -> 1
};


ProcessToWETTable =
   <| "p->pi+nue~" -> {G["^S,LL_udd"][1,1,1,1] + G["^S,RL_dud"][1,1,1,1]}
    , "n->pi0nue~" -> {G["^S,LL_udd"][1,1,1,1] + G["^S,RL_dud"][1,1,1,1]}
    , "n->eta0nue~" -> {G["^S,LL_udd"][1,1,1,1] + G["^S,RL_dud"][1,1,1,1]}

    , "p->K+nue~" -> {G["^S,LL_udd"][1,2,1,1] + G["^S,RL_dud"][2,1,1,1] + G["^S,RL_dud"][1,1,2,1] + G["^S,RL_ddu"][2,1,1,1]}
    , "n->K0nue~" -> {G["^S,LL_udd"][1,2,1,1] + G["^S,RL_dud"][2,1,1,1] + G["^S,RL_dud"][1,1,2,1] + G["^S,RL_ddu"][2,1,1,1]}

    , "p->pi0e+" -> {G["^S,LL_duu"][1,1,1,1] + G["^S,RL_duu"][1,1,1,1], G["^S,LR_duu"][1,1,1,1] + G["^S,RR_duu"][1,1,1,1]}
    , "p->eta0e+" -> {G["^S,LL_duu"][1,1,1,1] + G["^S,RL_duu"][1,1,1,1], G["^S,LR_duu"][1,1,1,1] + G["^S,RR_duu"][1,1,1,1]}
    , "n->pi-e+" -> {G["^S,LL_duu"][1,1,1,1] + G["^S,RL_duu"][1,1,1,1], G["^S,LR_duu"][1,1,1,1] + G["^S,RR_duu"][1,1,1,1]}

    , "p->K0e+" -> {G["^S,LL_duu"][2,1,1,1] + G["^S,RL_duu"][2,1,1,1], G["^S,LR_duu"][2,1,1,1] + G["^S,RR_duu"][2,1,1,1]}
    , "n->K-e+" -> {G["^S,LL_duu"][2,1,1,1] + G["^S,RL_duu"][2,1,1,1], G["^S,LR_duu"][2,1,1,1] + G["^S,RR_duu"][2,1,1,1]}

    (* Delta B = - Delta L = 1 *)
    , "p->pi+nue" -> {G["^S,LR_udd"][1,1,1,1] + G["^S,RR_udd"][1,1,1,1]}
    , "n->pi0nue" -> {G["^S,LR_udd"][1,1,1,1] + G["^S,RR_udd"][1,1,1,1]}
    , "n->eta0nue" -> {G["^S,LR_udd"][1,1,1,1] + G["^S,RR_udd"][1,1,1,1]}

    , "p->K+nue" -> {G["^S,LR_udd"][1,2,1,1] + G["^S,LR_udd"][1,1,1,2] + G["^S,LR_ddu"][1,2,1,1] + G["^S,RR_udd"][1,2,1,1]}
    , "n->K0nue" -> {G["^S,LR_udd"][1,2,1,1] + G["^S,LR_udd"][1,1,1,2] + G["^S,LR_ddu"][1,2,1,1] + G["^S,RR_udd"][1,2,1,1]}

    , "n->K+e-" -> {G["^S,LL_ddd"][2,1,1,1] + G["^S,RL_ddd"][2,1,1,1], G["^S,LR_ddd"][2,1,1,1] + G["^S,RR_ddd"][2,1,1,1]}
    , "n->pi+e-" -> {} (* Operator vanishes! *)
|>;

ExtractBaryonMesonLepton::usage = "Takes a process string and returns baryon,
meson and lepton as strings.";
ExtractBaryonMesonLepton::InvalidProcess = "Process invalid.";
ExtractBaryonMesonLepton[proc_String] :=
  Block[
    {baryon, meson, mesonPlusExtra, rst}
  ,
    If[! MemberQ[Keys[ProcessToWETTable], proc]
     , Message[ExtractBaryonMesonLepton::InvalidProcess]
     , Nothing
    ];

    {baryon, rst} = StringSplit[proc, "->"];

    mesonPlusExtra = StringSplit[rst, x : "+" | "-" | "0" :> x];

    { baryon
    , StringJoin @ mesonPlusExtra[[;; 2]]
    , StringJoin @ mesonPlusExtra[[3 ;;]]
    }
  ];


MatrixElement::usage = "An intermediate function to construct hadronic matrix
elements for use with LatticeNucleonDecayExpression.";
MatrixElement[meson_String, G[x_String][f__], baryon_String] := G["~"<>x][f] AngleBracket[meson, Op[x][f], baryon];
MatrixElement[meson_String, Plus[x__], baryon_String] := Table[MatrixElement[meson, i, baryon], {i, List @@ x}];


(* Sp head is used to implement simplification rules that take hadronic matrix
elements to a form whose numerical value is known. *)

Sp /: AngleBracket[m_, Sp[d_, "u", X_, q_, Y_], "p"] := -AngleBracket[m, Sp["u", d, X, q, Y], "p"];

Sp /: AngleBracket[m_, Sp[q1_, "d", X_, q_, Y_], "n"] := -AngleBracket[m, Sp["d", q1, X, q, Y], "n"];
Sp /: AngleBracket[m_, Sp["s", "u", X_, q_, Y_], "n"] := -AngleBracket[m, Sp["u", "s", X, q, Y], "n"];

Sp /: AngleBracket["pi0", Sp["u", "d", X_, "u", "L"], "p"] := Sqrt[2] AngleBracket["pi+", Sp["u", "d", X, "d", "L"], "p"];
Sp /: AngleBracket["pi0", Sp["u", "d", X_, "u", "R"], "p"] := Sqrt[2] AngleBracket["pi+", Sp["u", "d", X, "d", "R"], "p"];

(* Always try and write the third quark as right handed if proton *)
Sp /: AngleBracket[m_, Sp[q1_, q2_, "R", q3_, "L"], "p"] := AngleBracket[m, Sp[q1, q2, "L", q3, "R"], "p"];
Sp /: AngleBracket[m_, Sp[q1_, q2_, "R", q3_, "R"], "p"] := AngleBracket[m, Sp[q1, q2, "L", q3, "L"], "p"];

(* Always try and write the third quark as left handed if neutron *)
Sp /: AngleBracket[m_, Sp[q1_, q2_, "L", q3_, "R"], "n"] := AngleBracket[m, Sp[q1, q2, "R", q3, "L"], "n"];

(* Neutron decays, eqs 13-19 of  *)
Sp /: AngleBracket["pi0", Sp["d", "u", X_, "d", Y_], "n"] := AngleBracket["pi0", Sp["u", "d", X, "u", Y], "p"];
Sp /: AngleBracket["pi-", Sp["d", "u", X_, "u", Y_], "n"] := -AngleBracket["pi+", Sp["u", "d", X, "d", Y], "p"];
Sp /: AngleBracket["K+", Sp["d", "s", X_, "d", Y_], "n"] := -AngleBracket["K0", Sp["u", "s", X, "u", Y], "p"];
Sp /: AngleBracket["K0", Sp["d", "s", X_, "u", Y_], "n"] := -AngleBracket["K+", Sp["u", "s", X, "d", Y], "p"];
Sp /: AngleBracket["K0", Sp["d", "u", X_, "s", Y_], "n"] := -AngleBracket["K+", Sp["u", "d", X, "s", Y], "p"];
Sp /: AngleBracket["K0", Sp["u", "s", X_, "d", Y_], "n"] := -AngleBracket["K+", Sp["d", "s", X, "u", Y], "p"];
Sp /: AngleBracket["eta0", Sp["d", "u", X_, "d", Y_], "n"] := -AngleBracket["eta0", Sp["u", "d", X, "u", Y], "p"];

PackageExport["Sp"]


MatElemReplacements::usage = "Replaces the Op expression with a new Sp
expression, representing the guts of the hadronic matrix elements. This is only
used to apply simplification rules to. These rules reduces the matrix elements
to the subset whose numerical values are given in table VIII of 2111.01608 (and
1705.01338 for the eta decays).";
MatElemReplacements =
{ Op["^S,LL_udd"][1, 1, 1, 1] -> Sp["u", "d", "L", "d", "L"]
, Op["^S,LL_udd"][1, 2, 1, 1] -> Sp["u", "s", "L", "d", "L"]
, Op["^S,LL_udd"][1, 1, 2, 1] -> Sp["u", "d", "L", "s", "L"]

, Op["^S,LL_duu"][1, 1, 1, 1] -> Sp["d", "u", "L", "u", "L"]
, Op["^S,LL_duu"][2, 1, 1, 1] -> Sp["s", "u", "L", "u", "L"]

, Op["^S,LR_duu"][1, 1, 1, 1] -> Sp["d", "u", "L", "u", "R"]
, Op["^S,LR_duu"][2, 1, 1, 1] -> Sp["s", "u", "L", "u", "R"]

, Op["^S,RL_duu"][1, 1, 1, 1] -> Sp["d", "u", "R", "u", "L"]
, Op["^S,RL_duu"][2, 1, 1, 1] -> Sp["s", "u", "R", "u", "L"]

, Op["^S,RL_dud"][1, 1, 1, 1] -> Sp["d", "u", "R", "d", "L"]
, Op["^S,RL_dud"][2, 1, 1, 1] -> Sp["s", "u", "R", "d", "L"]
, Op["^S,RL_dud"][1, 1, 2, 1] -> Sp["d", "u", "R", "s", "L"]

, Op["^S,RL_ddu"][1, 2, 1, 1] -> Sp["d", "s", "R", "u", "L"]

, Op["^S,RR_duu"][1, 1, 1, 1] -> Sp["d", "u", "R", "u", "R"]
, Op["^S,RR_duu"][2, 1, 1, 1] -> Sp["s", "u", "R", "u", "R"]

(* Delta B = - Delta L = 1 *)

, Op["^S,LL_ddd"][1, 2, 1, 1] -> Sp["d", "s", "L", "d", "L"]

, Op["^S,LR_udd"][1, 1, 1, 1] -> Sp["u", "d", "L", "d", "R"]
, Op["^S,LR_udd"][1, 2, 1, 1] -> Sp["u", "s", "L", "d", "R"]
, Op["^S,LR_udd"][1, 1, 1, 2] -> Sp["u", "d", "L", "s", "R"]

, Op["^S,LR_ddu"][1, 2, 1, 1] -> Sp["d", "s", "L", "u", "R"]

, Op["^S,LR_ddd"][1, 2, 1, 1] -> Sp["d", "s", "L", "d", "R"]

, Op["^S,RL_ddd"][1, 2, 1, 1] -> Sp["d", "s", "R", "d", "L"]

, Op["^S,RR_udd"][1, 1, 1, 1] -> Sp["u", "d", "R", "d", "R"]
, Op["^S,RR_udd"][1, 2, 1, 1] -> Sp["u", "s", "R", "d", "R"]
, Op["^S,RR_udd"][1, 1, 1, 2] -> Sp["u", "d", "R", "s", "R"]

, Op["^S,RR_ddd"][1, 2, 1, 1] -> Sp["d", "s", "R", "d", "R"]
};
PackageExport["MatElemReplacements"]

LatticeReplacements =
{ AngleBracket["pi+", Sp["u", "d", "L", "d", "L"], "p"] -> 0.151 (* From 2111.01608 *)
, AngleBracket["pi+", Sp["u", "d", "L", "d", "R"], "p"] -> -0.159
, AngleBracket["K0", Sp["u", "s", "L", "u", "L"], "p"] -> 0.0430
, AngleBracket["K0", Sp["u", "s", "L", "u", "R"], "p"] -> 0.0854
, AngleBracket["K+", Sp["u", "s", "L", "d", "L"], "p"] -> 0.0284
, AngleBracket["K+", Sp["u", "s", "L", "d", "R"], "p"] -> -0.0398
, AngleBracket["K+", Sp["u", "d", "L", "s", "L"], "p"] -> 0.1006
, AngleBracket["K+", Sp["u", "d", "L", "s", "R"], "p"] -> -0.109
, AngleBracket["K+", Sp["d", "s", "L", "u", "L"], "p"] -> -0.0717
, AngleBracket["K+", Sp["d", "s", "L", "u", "R"], "p"] -> -0.0443
, AngleBracket["eta0", Sp["u", "d", "R", "u", "L"], "p"] -> 0.006 (* From 1705.01338 *)
, AngleBracket["eta0", Sp["u", "d", "L", "u", "L"], "p"] -> 0.113
};
PackageExport["LatticeReplacements"]


LatticeNucleonDecayExpression::usage = "Calculates proton decay expression from
hadronic matrix elements calculated on the Lattice. The expression is taken from
2111.01608.";

LatticeNucleonDecayExpression[proc_String] :=
  Block[
    {prefactor1, prefactor2, guts, baryon, meson, lepton}
  ,
    {baryon, meson, lepton} = ExtractBaryonMesonLepton[proc];

    prefactor1 = M["N"]/(32 \[Pi]^2);
    prefactor2 = (1 - M[meson]^2/M["N"]^2)^2;

    (* Whole list is Abs[]^2, but this applies to each element *)
    guts =
    Abs[
            Plus @@@ Table[
                    Abs[ (* This abs will mean we are slightly overestimating some rates *)
                            MatrixElement[meson, op, baryon]/M["\[CapitalLambda]"]^2
                    ],
                    {op, ProcessToWETTable[proc]}]
    ]^2;

    prefactor1 * prefactor2 * (Plus @@ guts)
  ];
PackageExport["LatticeNucleonDecayExpression"]
