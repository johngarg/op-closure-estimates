OperatorMatchingRulesDim6 = {
  (* Op 1 *)
  Op[L[r], Q[s], Q[t], Q[u], rst___Wt] :> Op[Op["1"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r], Q[s], Q[t], Q[u], Deriv, Deriv, rst___Wt] :> Op[Op["1"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[Q[s]], Conj[Q[t]], Conj[Q[u]], rst___Wt] :> Op[Conj[Op["1"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[Q[s]], Conj[Q[t]], Conj[Q[u]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["1"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 2 *)
  Op[Conj[eb[r]], Q[s], Q[t], Conj[ub[u]], rst___Wt] :> Op[Op["2"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r]], Q[s], Q[t], Conj[ub[u]], Deriv, Deriv, rst___Wt] :> Op[Op["2"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], Conj[Q[s]], Conj[Q[t]], ub[u], rst___Wt] :> Op[Conj[Op["2"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], Conj[Q[s]], Conj[Q[t]], ub[u], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["2"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 3 *)
  Op[Conj[eb[r]], Conj[ub[s]], Conj[ub[t]], Conj[db[u]], rst___Wt] :> Op[Op["3"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r]], Conj[ub[s]], Conj[ub[t]], Conj[db[u]], Deriv, Deriv, rst___Wt] :> Op[Op["3"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], ub[s], ub[t], db[u], rst___Wt] :> Op[Conj[Op["3"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], ub[s], ub[t], db[u], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["3"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 4 *)
  Op[L[r], Q[s], Conj[ub[t]], Conj[db[u]], rst___Wt] :> Op[Op["4"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r], Q[s], Conj[ub[t]], Conj[db[u]], Deriv, Deriv, rst___Wt] :> Op[Op["4"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[Q[s]], ub[t], db[u], rst___Wt] :> Op[Conj[Op["4"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[Q[s]], ub[t], db[u], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["4"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]]
};

OperatorMatchingRulesDim7 = {
  (* Op 5 *)
  Op[L[r], db[s], db[t], db[u], Conj[H[]], rst___Wt] :> Op[Op["5"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r], db[s], db[t], db[u], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Op["5"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[db[s]], Conj[db[t]], Conj[db[u]], H[], rst___Wt] :> Op[Conj[Op["5"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[db[s]], Conj[db[t]], Conj[db[u]], H[], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["5"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 6 *)
  Op[Deriv, L[r], Conj[Q[s]], db[t], db[u], rst___Wt] :> Op[Op["6"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Deriv, L[r], Conj[Q[s]], db[t], db[u], Deriv, Deriv, rst___Wt] :> Op[Op["6"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[Deriv, L[r]], Q[s], Conj[db[t]], Conj[db[u]], rst___Wt] :> Op[Conj[Op["6"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[Deriv, L[r]], Q[s], Conj[db[t]], Conj[db[u]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["6"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 7 *)
  Op[Conj[eb[r]], db[s], db[t], Deriv, db[u], rst___Wt] :> Op[Op["7"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r]], db[s], db[t], Deriv, db[u], Deriv, Deriv, rst___Wt] :> Op[Op["7"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], Conj[db[s]], Conj[db[t]], Conj[Deriv, db[u]], rst___Wt] :> Op[Conj[Op["7"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], Conj[db[s]], Conj[db[t]], Conj[Deriv, db[u]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["7"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 8 *)
  Op[L[r], Conj[Q[s]], Conj[Q[t]], db[u], H[], rst___Wt] :> Op[Op["8"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r], Conj[Q[s]], Conj[Q[t]], db[u], H[], Deriv, Deriv, rst___Wt] :> Op[Op["8"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Q[s], Q[t], Conj[db[u]], Conj[H[]], rst___Wt] :> Op[Conj[Op["8"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Q[s], Q[t], Conj[db[u]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["8"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 9 *)
  Op[Conj[eb[r]], Conj[Q[s]], db[t], db[u], H[], rst___Wt] :> Op[Op["9"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r]], Conj[Q[s]], db[t], db[u], H[], Deriv, Deriv, rst___Wt] :> Op[Op["9"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], Q[s], Conj[db[t]], Conj[db[u]], Conj[H[]], rst___Wt] :> Op[Conj[Op["9"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r], Q[s], Conj[db[t]], Conj[db[u]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["9"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 10 *)
  Op[L[r], ub[s], db[t], db[u], H[], rst___Wt] :> Op[Op["10"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r], ub[s], db[t], db[u], H[], Deriv, Deriv, rst___Wt] :> Op[Op["10"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[ub[s]], Conj[db[t]], Conj[db[u]], Conj[H[]], rst___Wt] :> Op[Conj[Op["10"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r]], Conj[ub[s]], Conj[db[t]], Conj[db[u]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["10"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]]
};

DerivativeRules = {

  Op[Deriv, Deriv, rst__] :> Op[rst],

  Op[Deriv, eb[p_], rst__] :> Block[{x0 = Unique["x"], i0 = Unique["i"], j0 = Unique["j"]},
                                    Op[Conj[L[x0, i0]], H[j0], Eps[i0, j0], rst,
                                       MatchingValues["p" -> p, "x0" -> x0, "i0" -> i0, "j0" -> j0],
                                       Wt[Conj[ye[p, x0]]]
                                    ]
                              ],
  Op[Deriv, Conj[eb[p_]], rst__] :> Block[{x0 = Unique["x"], i0 = Unique["i"], j0 = Unique["j"]},
                                          Op[L[x0, i0], Conj[H[j0]], Eps[i0, j0], rst,
                                             MatchingValues["p" -> p, "x0" -> x0, "i0" -> i0, "j0" -> j0],
                                             Wt[ye[p, x0]]
                                          ]
                                    ],
  Op[Deriv, L[p_, i_], rst__] :> Block[{x0 = Unique["x"]},
                                       Op[Conj[eb[x0]], H[i], rst,
                                             MatchingValues["p" -> p, "x0" -> x0],
                                          Wt[Conj[ye[x0, p]]]
                                          ]
                                    ],
  Op[Deriv, Conj[L[p_, i_]], rst__] :> Block[{x0 = Unique["x"]},
                                             Op[eb[x0], Conj[H[i]], rst,
                                                MatchingValues["p" -> p, "x0" -> x0],
                                                Wt[ye[x0, p]]
                                             ]
                                       ],

  Op[Deriv, db[p_], rst__] :> Block[{x0 = Unique["x"], i0 = Unique["i"], j0 = Unique["j"]},
                                    Op[Conj[Q[x0, i0]], H[j0], Eps[i0, j0], rst,
                                       MatchingValues["p" -> p, "x0" -> x0, "i0" -> i0, "j0" -> j0],
                                       Wt[Conj[yd[p, x0]]]
                                    ]
                              ],
  Op[Deriv, Conj[db[p_]], rst__] :> Block[{x0 = Unique["x"], i0 = Unique["i"], j0 = Unique["j"]},
                                          Op[Q[x0, i0], Conj[H[j0]], Eps[i0, j0], rst,
                                             MatchingValues["p" -> p, "x0" -> x0, "i0" -> i0, "j0" -> j0],
                                             Wt[yd[p, x0]]
                                          ]
                                    ],
  Op[Deriv, Q[p_, i_], rst__] :> Block[{x0 = Unique["x"]},
                                       Op[Conj[db[x0]], H[i], rst,
                                             MatchingValues["p" -> p, "x0" -> x0],
                                          Wt[Conj[yd[x0, p]]]
                                          ]
                                    ],
  Op[Deriv, Conj[Q[p_, i_]], rst__] :> Block[{x0 = Unique["x"]},
                                             Op[db[x0], Conj[H[i]], rst,
                                                MatchingValues["p" -> p, "x0" -> x0],
                                                Wt[yd[x0, p]]
                                             ]
                                       ],

  Op[Deriv, ub[p_], rst__] :> Block[{x0 = Unique["x"], i0 = Unique["i"], j0 = Unique["j"]},
                                        Op[Conj[Q[x0, i0]], Conj[H[j0]], Eps[i0, j0], rst,
                                           MatchingValues["p" -> p, "x0" -> x0, "i0" -> i0, "j0" -> j0],
                                           Wt[Conj[yu[p, x0]]]
                                        ]
                                  ],
  Op[Deriv, Conj[ub[p_]], rst__] :> Block[{x0 = Unique["x"], i0 = Unique["i"], j0 = Unique["j"]},
                                              Op[Q[x0, i0], H[j0], Eps[i0, j0], rst,
                                                 MatchingValues["p" -> p, "x0" -> x0, "i0" -> i0, "j0" -> j0],
                                                 Wt[yu[p, x0]]
                                              ]
                                        ],
  Op[Deriv, Q[p_, i_], rst__] :> Block[{x0 = Unique["x"]},
                                       Op[Conj[ub[x0]], Conj[H[i]], rst,
                                          MatchingValues["p" -> p, "x0" -> x0],
                                          Wt[Conj[yu[x0, p]]]
                                       ]
                                 ],
  Op[Deriv, Conj[Q[p_, i_]], rst__] :> Block[{x0 = Unique["x"]},
                                             Op[ub[x0], H[i], rst,
                                                MatchingValues["p" -> p, "x0" -> x0],
                                                Wt[yu[x0, p]]
                                             ]
                                       ]
};

YukawaRules = {
  (* Up Yukawa *)
  (* ub H \[Rule] Qd *)
  Op[
    ub[r_], H[i_],
    rst___
  ] :> Block[{x0 = Unique["x"]},
             Op[Conj[Q[x0, i]], Deriv, rst,
                MatchingValues["r" -> r, "i" -> i, "x0" -> x0],
                Wt[Conj[yu[r, x0]]], Wt[loop]]
       ],

  Op[
    Conj[ub[r_]], Conj[H[i_]],
    rst___
  ] :> Block[{x0 = Unique["x"]},
             Op[Q[x0, i], Deriv,
                rst,
                MatchingValues["r" -> r, "i" -> i, "x0" -> x0],
                Wt[yu[r, x0]], Wt[loop]]
       ],

  (* ub Q \[Rule] Hd *)
  Op[
    ub[r_], Q[s_, i_],
    rst___
  ] :> Op[Conj[H[i]],
          rst,
          MatchingValues["i" -> i, "r" -> r, "s" -> s],
          Wt[Conj[yu[r, s]]], Wt[loop]
       ],

  Op[
    Conj[ub[r_]], Conj[Q[s_, i_]],
    rst___
  ] :> Op[H[i],
          rst,
          MatchingValues["i" -> i, "r" -> r, "s" -> s],
          Wt[yu[r, s]], Wt[loop]
       ],

  (* Q H \[Rule] ubd *)
  Op[Q[r_, i_], H[j_], rst___] :> Block[{x0 = Unique["x"]},
                                            Op[Conj[ub[x0]], Eps[i, j], Deriv, rst,
                                               MatchingValues["i" -> i, "j" -> j, "x0" -> x0,
                                                              "r" -> r],
                                               Wt[Conj[yu[x0, r]]], Wt[loop]]],
  Op[Conj[Q[r_, i_]], Conj[H[j_]], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[ub[x0], Eps[i, j], Deriv, rst,
             MatchingValues["i" -> i, "j" -> j, "x0" -> x0, "r" -> r],
             Wt[yu[x0, r]], Wt[loop]]],

  (* Down Yukawa *)
  (* db Hc -> Qc *)

  Op[db[r_], Conj[H[i_]], rst___] :> Block[{x0 = Unique["x"]},
                                               Op[Conj[Q[x0, i]], Deriv, rst,
                                                  MatchingValues["r" -> r, "i" -> i, "x0" -> x0],
                                                  Wt[Conj[yd[r, x0]]], Wt[loop]]],
  Op[Conj[db[r_]], H[i_], rst___] :> Block[{x0 = Unique["x"]},
                                               Op[Q[x0, i], Deriv, rst,
                                                  MatchingValues["r" -> r, "i" -> i, "x0" -> x0],
                                                  Wt[yd[r, x0]], Wt[loop]]],

  (* db Q -> H *)

  Op[db[r_], Q[s_, i_], rst___] :>
    Op[H[i], rst,
       MatchingValues["i" -> i, "r" -> r, "s" -> s],
       Wt[Conj[yd[r, s]]], Wt[loop]],
  Op[Conj[db[r_]], Conj[Q[s_, i_]], rst___] :>
    Op[Conj[H[i]], rst,
       MatchingValues["i" -> i, "r" -> r, "s" -> s],
       Wt[yd[r, s]], Wt[loop]],

  (* Q Hc -> dbc *)

  Op[Q[r_, i_], Conj[H[j_]], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[Conj[db[x0]], Eps[i, j], Deriv, rst,
             MatchingValues["i" -> i, "j" -> j, "r" -> r, "x0" -> x0],
             Wt[Conj[yd[x0, r]]], Wt[loop]]],
  Op[Conj[Q[r_, i_]], H[j_], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[db[x0], Eps[i, j], Deriv, rst,
             MatchingValues["i" -> i, "j" -> j, "r" -> r, "x0" -> x0],
             Wt[yd[x0, r]], Wt[loop]]],

  (* Electron Yukawa *)
  (* eb Hc -> Lc *)

  Op[eb[r_], Conj[H[i_]], rst___] :> Block[{x0 = Unique["x"]},
                                           Op[Conj[L[x0, i]], Deriv, rst,
                                              MatchingValues["r" -> r, "i" -> i, "x0" -> x0],
                                              Wt[Conj[ye[r, x0]]], Wt[loop]]],
  Op[Conj[eb[r_]], H[i_], rst___] :> Block[{x0 = Unique["x"]},
                                           Op[L[x0, i], Deriv, rst,
                                              MatchingValues["r" -> r, "i" -> i, "x0" -> x0],
                                              Wt[ye[r, x0]], Wt[loop]]],

  (* eb L -> H *)
  Op[eb[r_], L[s_, i_], rst___] :> Op[H[i], rst,
                                      MatchingValues["i" -> i, "r" -> r, "s" -> s],
                                      Wt[Conj[ye[r, s]]], Wt[loop]],
  Op[Conj[eb[r_]], Conj[L[s_, i_]], rst___] :> Op[Conj[H[i]], rst,
                                                  MatchingValues["i" -> i, "r" -> r, "s" -> s],
                                                  Wt[ye[r, s]], Wt[loop]],

  (* L Hc -> ebc *)

  Op[L[r_, i_], Conj[H[j_]], rst___] :> Block[{x0 = Unique["x"]},
                                              Op[Conj[eb[x0]], Eps[i, j], Deriv, rst,
                                                 MatchingValues["i" -> i, "j" -> j, "r" -> r, "x0" -> x0],
                                                 Wt[Conj[ye[x0, r]]], Wt[loop]]],
  Op[Conj[L[r_, i_]], H[j_], rst___] :> Block[{x0 = Unique["x"]},
                                              Op[eb[x0], Eps[i, j], Deriv, rst,
                                                 MatchingValues["i" -> i, "j" -> j, "r" -> r, "x0" -> x0],
                                                 Wt[ye[x0, r]], Wt[loop]]]
};

LoopRules = {
  Op[eb[r_], Conj[eb[s_]], rst___] :>
    Op[Delta[r, s], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s],
       Wt[loop]],

  Op[ub[r_], Conj[ub[s_]], rst___] :>
    Op[Delta[r, s], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s],
       Wt[loop]],

  Op[db[r_], Conj[db[s_]], rst___] :>
    Op[Delta[r, s], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s],
       Wt[loop]],

  Op[L[r_, i_], Conj[L[s_, j_]], rst___] :>
    Op[Delta[r, s], Eps[i, j], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s, "i" -> i, "j" -> j],
       Wt[loop]],

  Op[Q[r_, i_], Conj[Q[s_, j_]], rst___] :>
    Op[Delta[r, s], Eps[i, j], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s, "i" -> i, "j" -> j],
       Wt[loop]],

  Op[H[i_], Conj[H[j_]], rst___] :>
    Op[Eps[i, j], rst,
       MatchingValues["i" -> i, "j" -> j],
       Wt[hloop]]

};

EpsDeltaRules = {
  Op[Eps[i_, j_], Eps[i_, j_], rst___] :>
    Op[Wt[2], rst,
       MatchingValues["i" -> i, "j" -> j]],

  Op[Eps[m_, n_], Eps[i_, m_], Eps[l_, n_], rst___] :>
    Op[Eps[l, i], rst,
       MatchingValues["i" -> i, "m" -> m, "n" -> n, "l" -> l]]

};

FlavourDeltaRules = {
  Op[Delta[r_, p_], rst___] :>
    (Op[rst] /.  r -> p) ~Join~ Op[MatchingValues["r" -> r, "p" -> p]]
};

$MatchingRulesDim8 =
Join[YukawaRules, LoopRules, EpsDeltaRules];

$MatchingRulesDim9 =
Join[YukawaRules, LoopRules, EpsDeltaRules, DerivativeRules, FlavourDeltaRules];


(* LEFT Symmetries, or should this be done at the level of the SMEFT? Just do both! *)

(* These should be all of the operators for which a choice needs to be made
about where the strange quark should go. *)

Op["^S,LL_udd"][1,1,2,1] := Op["^S,LL_udd"][1,2,1,1];
Op["^S,RL_ddu"][1,2,1,1] := Op["^S,RL_ddu"][2,1,1,1];

Op["^S,RR_udd"][1,1,1,2] := Op["^S,RR_udd"][1,2,1,1];
Op["^S,LL_ddd"][1,2,1,1] := Op["^S,LL_ddd"][2,1,1,1];
Op["^S,LL_ddd"][1,1,1,2] := Op["^S,LL_ddd"][2,1,1,1];
Op["^S,RL_ddd"][1,2,1,1] := Op["^S,RL_ddd"][2,1,1,1];
Op["^S,LR_ddd"][1,2,1,1] := Op["^S,LR_ddd"][2,1,1,1];
Op["^S,RR_ddd"][1,1,1,2] := Op["^S,RR_ddd"][2,1,1,1];
Op["^S,RR_ddd"][1,2,1,1] := Op["^S,RR_ddd"][2,1,1,1];

Op["~^S,LL_ddd"][p_, p_, r_, s_] := 0;
Op["~^S,LR_ddu"][p_, p_, r_, s_] := 0;
Op["~^S,LR_ddd"][p_, p_, r_, s_] := 0;
Op["~^S,RL_ddd"][p_, p_, r_, s_] := 0;
Op["~^S,RR_ddd"][p_, p_, r_, s_] := 0;
