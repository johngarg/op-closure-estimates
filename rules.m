OperatorMatchingRulesDim6 = {
  (* Op 1 *)
  Op[
    L[p_, i_], Q[q_, j_], Q[r_, k_], Q[s_, l_],
    Eps[i_, k_], Eps[j_, l_],
    rst___Wt
  ] :> Op[Op["1"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], Q[q_, j_], Q[r_, k_], Q[s_, l_],
    Eps[i_, k_], Eps[j_, l_],
    rst___Wt
  ] :> Op[Op["1"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Conj[Q[q_, j_]], Conj[Q[r_, k_]], Conj[Q[s_, l_]],
    Eps[i_, k_], Eps[j_, l_],
    rst___Wt
  ] :> Op[Conj[Op["1"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Conj[Q[q_, j_]], Conj[Q[r_, k_]], Conj[Q[s_, l_]],
    Eps[i_, k_], Eps[j_, l_],
    rst___Wt
  ] :> Op[Conj[Op["1"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 2 *)
  Op[
    Conj[eb[p_]], Q[q_, i_], Q[r_, j_], Conj[ub[s_]],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Op["2"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[eb[p_]], Q[q_, i_], Q[r_, j_], Conj[ub[s_]],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Op["2"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    eb[p_], Conj[Q[q_, i_]], Conj[Q[r_, j_]], ub[s_],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Conj[Op["2"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    eb[p_], Conj[Q[q_, i_]], Conj[Q[r_, j_]], ub[s_],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Conj[Op["2"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 3 *)
  Op[Conj[eb[p_]], Conj[ub[q_]], Conj[ub[r_]], Conj[db[s_]],
     rst___Wt
  ] :> Op[Op["3"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[eb[p_]], Conj[ub[q_]], Conj[ub[r_]], Conj[db[s_]],
    rst___Wt
  ] :> Op[Op["3"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    eb[p_], ub[q_], ub[r_], db[s_],
    rst___Wt
  ] :> Op[Conj[Op["3"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    eb[p_], ub[q_], ub[r_], db[s_],
    rst___Wt
  ] :> Op[Conj[Op["3"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 4 *)
  Op[
    L[p_, i_], Q[q_, j_], Conj[ub[r_]], Conj[db[s_]],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Op["4"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], Q[q_, j_], Conj[ub[r_]], Conj[db[s_]],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Op["4"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Conj[Q[q_, j_]], ub[r_], db[s_],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Conj[Op["4"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Conj[Q[q_, j_]], ub[r_], db[s_],
    Eps[i_, j_],
    rst___Wt
  ] :> Op[Conj[Op["4"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]]

};

OperatorMatchingRulesDim7 = {
  (* Op 5 *)
  Op[
    L[p_, i_], db[q_], db[r_], db[s_], Conj[H[j_]],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Op["5"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], db[q_], db[r_], db[s_], Conj[H[j_]],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Op["5"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Conj[db[q_]], Conj[db[r_]], Conj[db[s_]], H[j_],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Conj[Op["5"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Conj[db[q_]], Conj[db[r_]], Conj[db[s_]], H[j_],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Conj[Op["5"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 6a *)
  Op[
    L[p_, i_], Conj[Q[q_, j_]], Conj[Q[r_, k_]], db[s_], H[l_],
    Eps[i_, k_], Eps[j_, l_],
    rst___
  ] :> Op[Op["6a"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], Conj[Q[q_, j_]], Conj[Q[r_, k_]], db[s_], H[l_],
    Eps[i_, k_], Eps[j_, l_],
    rst___
  ] :> Op[Op["6a"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Q[q_, j_], Q[r_, k_], Conj[db[s_]], Conj[H[l_]],
    Eps[i_, k_], Eps[j_, l_],
    rst___
  ] :> Op[Conj[Op["6a"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Q[q_, j_], Q[r_, k_], Conj[db[s_]], Conj[H[l_]],
    Eps[i_, k_], Eps[j_, l_],
    rst___
  ] :> Op[Conj[Op["6a"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 6b *)
  Op[
    L[p_, i_], Conj[Q[q_, j_]], Conj[Q[r_, k_]], db[s_], H[l_],
    Eps[i_, l_], Eps[j_, k_],
    rst___
  ] :> Op[Op["6b"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], Conj[Q[q_, j_]], Conj[Q[r_, k_]], db[s_], H[l_],
    Eps[i_, l_], Eps[j_, k_],
    rst___
  ] :> Op[Op["6b"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Q[q_, j_], Q[r_, k_], Conj[db[s_]], Conj[H[l_]],
    Eps[i_, l_], Eps[j_, k_],
    rst___
  ] :> Op[Conj[Op["6b"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Q[q_, j_], Q[r_, k_], Conj[db[s_]], Conj[H[l_]],
    Eps[i_, l_], Eps[j_, k_],
    rst___
  ] :> Op[Conj[Op["6b"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 7 *)
  Op[
    Conj[eb[p_]], Conj[Q[q_, i_]], db[r_], db[s_], H[j_],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Op["7"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[eb[p_]], Conj[Q[q_, i_]], db[r_], db[s_], H[j_],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Op["7"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    eb[p_], Q[q_, i_], Conj[db[r_]], Conj[db[s_]], Conj[H[j_]],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Conj[Op["7"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    eb[p_], Q[q_, i_], Conj[db[r_]], Conj[db[s_]], Conj[H[j_]],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Conj[Op["7"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 8 *)
  Op[
    L[p_, i_], ub[q_], db[r_], db[s_], H[j_],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Op["8"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], ub[q_], db[r_], db[s_], H[j_],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Op["8"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Conj[ub[q_]], Conj[db[r_]], Conj[db[s_]], Conj[H[j_]],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Conj[Op["8"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Conj[ub[q_]], Conj[db[r_]], Conj[db[s_]], Conj[H[j_]],
    (* Eps[i_, j_], *)
    rst___
  ] :> Op[Conj[Op["8"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]]

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
