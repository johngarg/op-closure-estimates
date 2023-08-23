OperatorMatchingRulesDim6 = {
  (* Op 1 *)
  Op[L[r_], Q[s_], Q[t_], Q[u_], rst___Wt] :> Op[Op["1"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], Q[s_], Q[t_], Q[u_], Deriv, Deriv, rst___Wt] :> Op[Op["1"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[Q[s_]], Conj[Q[t_]], Conj[Q[u_]], rst___Wt] :> Op[Conj[Op["1"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[Q[s_]], Conj[Q[t_]], Conj[Q[u_]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["1"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 2 *)
  Op[Conj[eb[r_]], Q[s_], Q[t_], Conj[ub[u_]], rst___Wt] :> Op[Op["2"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r_]], Q[s_], Q[t_], Conj[ub[u_]], Deriv, Deriv, rst___Wt] :> Op[Op["2"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Conj[Q[s_]], Conj[Q[t_]], ub[u_], rst___Wt] :> Op[Conj[Op["2"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Conj[Q[s_]], Conj[Q[t_]], ub[u_], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["2"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 3 *)
  Op[Conj[eb[r_]], Conj[ub[s_]], Conj[ub[t_]], Conj[db[u_]], rst___Wt] :> Op[Op["3"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r_]], Conj[ub[s_]], Conj[ub[t_]], Conj[db[u_]], Deriv, Deriv, rst___Wt] :> Op[Op["3"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], ub[s_], ub[t_], db[u_], rst___Wt] :> Op[Conj[Op["3"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], ub[s_], ub[t_], db[u_], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["3"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 4 *)
  Op[L[r_], Q[s_], Conj[ub[t_]], Conj[db[u_]], rst___Wt] :> Op[Op["4"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], Q[s_], Conj[ub[t_]], Conj[db[u_]], Deriv, Deriv, rst___Wt] :> Op[Op["4"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[Q[s_]], ub[t_], db[u_], rst___Wt] :> Op[Conj[Op["4"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[Q[s_]], ub[t_], db[u_], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["4"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]]
};

OperatorMatchingRulesDim7 = {
  (* Op 5 *)
  Op[L[r_], db[s_], db[t_], db[u_], Conj[H[]], rst___Wt] :> Op[Op["5"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], db[s_], db[t_], db[u_], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Op["5"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[db[s_]], Conj[db[t_]], Conj[db[u_]], H[], rst___Wt] :> Op[Conj[Op["5"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[db[s_]], Conj[db[t_]], Conj[db[u_]], H[], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["5"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 6 *)
  Op[Deriv, L[r_], Conj[Q[s_]], db[t_], db[u_], rst___Wt] :> Op[Op["6"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Deriv, L[r_], Conj[Q[s_]], db[t_], db[u_], Deriv, Deriv, rst___Wt] :> Op[Op["6"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[Deriv, L[r_]], Q[s_], Conj[db[t_]], Conj[db[u_]], rst___Wt] :> Op[Conj[Op["6"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[Deriv, L[r_]], Q[s_], Conj[db[t_]], Conj[db[u_]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["6"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 7 *)
  Op[Conj[eb[r_]], db[s_], db[t_], Deriv, db[u_], rst___Wt] :> Op[Op["7"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r_]], db[s_], db[t_], Deriv, db[u_], Deriv, Deriv, rst___Wt] :> Op[Op["7"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Conj[db[s_]], Conj[db[t_]], Conj[Deriv, db[u_]], rst___Wt] :> Op[Conj[Op["7"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Conj[db[s_]], Conj[db[t_]], Conj[Deriv, db[u_]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["7"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 8 *)
  Op[L[r_], Conj[Q[s_]], Conj[Q[t_]], db[u_], H[], rst___Wt] :> Op[Op["8"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], Conj[Q[s_]], Conj[Q[t_]], db[u_], H[], Deriv, Deriv, rst___Wt] :> Op[Op["8"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Q[t_], Conj[db[u_]], Conj[H[]], rst___Wt] :> Op[Conj[Op["8"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Q[t_], Conj[db[u_]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["8"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 9 *)
  Op[Conj[eb[r_]], Conj[Q[s_]], db[t_], db[u_], H[], rst___Wt] :> Op[Op["9"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r_]], Conj[Q[s_]], db[t_], db[u_], H[], Deriv, Deriv, rst___Wt] :> Op[Op["9"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Q[s_], Conj[db[t_]], Conj[db[u_]], Conj[H[]], rst___Wt] :> Op[Conj[Op["9"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Q[s_], Conj[db[t_]], Conj[db[u_]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["9"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 10 *)
  Op[L[r_], ub[s_], db[t_], db[u_], H[], rst___Wt] :> Op[Op["10"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], ub[s_], db[t_], db[u_], H[], Deriv, Deriv, rst___Wt] :> Op[Op["10"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[ub[s_]], Conj[db[t_]], Conj[db[u_]], Conj[H[]], rst___Wt] :> Op[Conj[Op["10"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[ub[s_]], Conj[db[t_]], Conj[db[u_]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["10"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]]
};

OperatorMatchingRulesDim8 = {
  (* Op 16 *)
  Op[L[r_], Q[s_], Conj[db[t_]], Conj[db[u_]], H[], H[], rst___Wt] :> Op[Op["16"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], Q[s_], Conj[db[t_]], Conj[db[u_]], H[], H[], Deriv, Deriv, rst___Wt] :> Op[Op["16"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[Q[s_]], db[t_], db[u_], Conj[H[]], Conj[H[]], rst___Wt] :> Op[Conj[Op["16"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Conj[Q[s_]], db[t_], db[u_], Conj[H[]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["16"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
};

OperatorMatchingRulesDim9 = {
  (* Op 26 *)
  Op[Conj[eb[r_]], Conj[Q[s_]], Conj[Q[t_]], Conj[Q[u_]], H[], H[], H[], rst___Wt] :> Op[Op["26"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r_]], Conj[Q[s_]], Conj[Q[t_]], Conj[Q[u_]], H[], H[], H[], Deriv, Deriv, rst___Wt] :> Op[Op["26"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Q[s_], Q[t_], Q[u_], Conj[H[]], Conj[H[]], Conj[H[]], rst___Wt] :> Op[Conj[Op["26"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Q[s_], Q[t_], Q[u_], Conj[H[]], Conj[H[]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["26"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 34 *)
  Op[Conj[eb[r_]], Conj[Q[s_]], Conj[Q[t_]], db[u_], H[], H[], Deriv, rst___Wt] :> Op[Op["34"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[eb[r_]], Conj[Q[s_]], Conj[Q[t_]], db[u_], H[], H[], Deriv, Deriv, Deriv, rst___Wt] :> Op[Op["34"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Q[s_], Q[t_], Conj[db[u_]], Conj[H[]], Conj[H[]], Deriv, rst___Wt] :> Op[Conj[Op["34"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[eb[r_], Q[s_], Q[t_], Conj[db[u_]], Conj[H[]], Conj[H[]], Deriv, Deriv, Deriv, rst___Wt] :> Op[Conj[Op["34"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 38 *)
  Op[L[r_], Conj[Q[s_]], Conj[Q[t_]], Conj[Q[u_]], H[], H[], Deriv, rst___Wt] :> Op[Op["38"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], Conj[Q[s_]], Conj[Q[t_]], Conj[Q[u_]], H[], H[], Deriv, Deriv, Deriv, rst___Wt] :> Op[Op["38"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Q[t_], Q[u_], Conj[H[]], Conj[H[]], Deriv, rst___Wt] :> Op[Conj[Op["38"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Q[t_], Q[u_], Conj[H[]], Conj[H[]], Deriv, Deriv, Deriv, rst___Wt] :> Op[Conj[Op["38"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 37 *)
  Op[L[r_], Conj[Q[s_]], Conj[Q[t_]], ub[u_], H[], H[], H[], rst___Wt] :> Op[Op["37"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], Conj[Q[s_]], Conj[Q[t_]], ub[u_], H[], H[], H[], Deriv, Deriv, rst___Wt] :> Op[Op["37"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Q[t_], Conj[ub[u_]], Conj[H[]], Conj[H[]], Conj[H[]], rst___Wt] :> Op[Conj[Op["37"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Q[t_], Conj[ub[u_]], Conj[H[]], Conj[H[]], Conj[H[]], Deriv, Deriv, rst___Wt] :> Op[Conj[Op["37"][r,s,t,u]], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  (* Op 44 *)
  Op[L[r_], Conj[Q[s_]], ub[t_], db[u_], H[], H[], Deriv, rst___Wt] :> Op[Op["44"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[L[r_], Conj[Q[s_]], ub[t_], db[u_], H[], H[], Deriv, Deriv, Deriv, rst___Wt] :> Op[Op["44"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Conj[ub[t_]], Conj[db[u_]], Conj[H[]], Conj[H[]], Deriv, rst___Wt] :> Op[Op["44"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
  Op[Conj[L[r_]], Q[s_], Conj[ub[t_]], Conj[db[u_]], Conj[H[]], Conj[H[]], Deriv, Deriv, Deriv, rst___Wt] :> Op[Op["44"][r,s,t,u], MatchingValues["r" -> r, "s" -> s, "t" -> t, "u" -> u]],
};

DerivativeRules = {

  Op[Deriv, Deriv, rst__] :> Op[rst],

  Op[Deriv, eb[p_], rst__] :> Block[{x0 = Unique["x"]},
                                    Op[Conj[L[x0]], H[], rst,
                                       MatchingValues["p" -> p, "x0" -> x0],
                                       Wt[Conj[ye[p, x0]]]
                                       ]
                                    ],
  Op[Deriv, Conj[eb[p_]], rst__] :> Block[{x0 = Unique["x"]},
                                          Op[L[x0], Conj[H[]], rst,
                                             MatchingValues["p" -> p, "x0" -> x0],
                                             Wt[ye[p, x0]]
                                             ]
                                          ],
  Op[Deriv, L[p_], rst__] :> Block[{x0 = Unique["x"]},
                                   Op[Conj[eb[x0]], H[], rst,
                                      MatchingValues["p" -> p, "x0" -> x0],
                                      Wt[Conj[ye[x0, p]]]
                                      ]
                                   ],
  Op[Deriv, Conj[L[p_]], rst__] :> Block[{x0 = Unique["x"]},
                                         Op[eb[x0], Conj[H[]], rst,
                                            MatchingValues["p" -> p, "x0" -> x0],
                                            Wt[ye[x0, p]]
                                            ]
                                         ],

  Op[Deriv, db[p_], rst__] :> Block[{x0 = Unique["x"]},
                                    Op[Conj[Q[x0]], H[], rst,
                                       MatchingValues["p" -> p, "x0" -> x0],
                                       Wt[Conj[yd[p, x0]]]
                                       ]
                                    ],
  Op[Deriv, Conj[db[p_]], rst__] :> Block[{x0 = Unique["x"]},
                                          Op[Q[x0], Conj[H[]], rst,
                                             MatchingValues["p" -> p, "x0" -> x0],
                                             Wt[yd[p, x0]]
                                             ]
                                          ],
  Op[Deriv, Q[p_], rst__] :> Block[{x0 = Unique["x"]},
                                   Op[Conj[db[x0]], H[], rst,
                                      MatchingValues["p" -> p, "x0" -> x0],
                                      Wt[Conj[yd[x0, p]]]
                                      ]
                                   ],
  Op[Deriv, Conj[Q[p_]], rst__] :> Block[{x0 = Unique["x"]},
                                         Op[db[x0], Conj[H[]], rst,
                                            MatchingValues["p" -> p, "x0" -> x0],
                                            Wt[yd[x0, p]]
                                            ]
                                         ],

  Op[Deriv, ub[p_], rst__] :> Block[{x0 = Unique["x"]},
                                    Op[Conj[Q[x0]], Conj[H[]], rst,
                                       MatchingValues["p" -> p, "x0" -> x0],
                                       Wt[Conj[yu[p, x0]]]
                                       ]
                                    ],
  Op[Deriv, Conj[ub[p_]], rst__] :> Block[{x0 = Unique["x"]},
                                          Op[Q[x0], H[], rst,
                                             MatchingValues["p" -> p, "x0" -> x0],
                                             Wt[yu[p, x0]]
                                             ]
                                          ],
  Op[Deriv, Q[p_], rst__] :> Block[{x0 = Unique["x"]},
                                   Op[Conj[ub[x0]], Conj[H[]], rst,
                                      MatchingValues["p" -> p, "x0" -> x0],
                                      Wt[Conj[yu[x0, p]]]
                                      ]
                                   ],
  Op[Deriv, Conj[Q[p_]], rst__] :> Block[{x0 = Unique["x"]},
                                         Op[ub[x0], H[], rst,
                                            MatchingValues["p" -> p, "x0" -> x0],
                                            Wt[yu[x0, p]]
                                            ]
                                         ]
};

TwoDerivativeRule = {Op[Deriv, Deriv, rst__] :> Op[rst]};

YukawaRules = {
  (* Up Yukawa *)
  (* ub H \[Rule] Qd *)
  Op[
    ub[r_], H[],
    rst___
  ] :> Block[{x0 = Unique["x"]},
             Op[Conj[Q[x0]], Deriv, rst,
                MatchingValues["r" -> r, "x0" -> x0],
                Wt[Conj[yu[r, x0]]], Wt[loop]]
       ],

  Op[
    Conj[ub[r_]], Conj[H[]],
    rst___
  ] :> Block[{x0 = Unique["x"]},
             Op[Q[x0], Deriv,
                rst,
                MatchingValues["r" -> r, "x0" -> x0],
                Wt[yu[r, x0]], Wt[loop]]
       ],

  (* ub Q \[Rule] Hd *)
  Op[
    ub[r_], Q[s_],
    rst___
  ] :> Op[Conj[H[]],
          rst,
          MatchingValues["r" -> r, "s" -> s],
          Wt[Conj[yu[r, s]]], Wt[loop]
       ],

  Op[
    Conj[ub[r_]], Conj[Q[s_]],
    rst___
  ] :> Op[H[],
          rst,
          MatchingValues["r" -> r, "s" -> s],
          Wt[yu[r, s]], Wt[loop]
       ],

  (* Q H \[Rule] ubd *)
  Op[Q[r_], H[], rst___] :> Block[{x0 = Unique["x"]},
                                  Op[Conj[ub[x0]], Deriv, rst,
                                     MatchingValues["x0" -> x0, "r" -> r],
                                     Wt[Conj[yu[x0, r]]], Wt[loop]]],
  Op[Conj[Q[r_]], Conj[H[]], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[ub[x0], Deriv, rst,
             MatchingValues["x0" -> x0, "r" -> r],
             Wt[yu[x0, r]], Wt[loop]]],

  (* Down Yukawa *)
  (* db Hc -> Qc *)

  Op[db[r_], Conj[H[]], rst___] :> Block[{x0 = Unique["x"]},
                                         Op[Conj[Q[x0]], Deriv, rst,
                                            MatchingValues["r" -> r, "x0" -> x0],
                                            Wt[Conj[yd[r, x0]]], Wt[loop]]],
  Op[Conj[db[r_]], H[], rst___] :> Block[{x0 = Unique["x"]},
                                         Op[Q[x0], Deriv, rst,
                                            MatchingValues["r" -> r, "x0" -> x0],
                                            Wt[yd[r, x0]], Wt[loop]]],

  (* db Q -> H *)

  Op[db[r_], Q[s_], rst___] :>
    Op[H[], rst,
       MatchingValues["r" -> r, "s" -> s],
       Wt[Conj[yd[r, s]]], Wt[loop]],
  Op[Conj[db[r_]], Conj[Q[s_]], rst___] :>
    Op[Conj[H[]], rst,
       MatchingValues["r" -> r, "s" -> s],
       Wt[yd[r, s]], Wt[loop]],

  (* Q Hc -> dbc *)

  Op[Q[r_], Conj[H[]], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[Conj[db[x0]], Deriv, rst,
             MatchingValues["r" -> r, "x0" -> x0],
             Wt[Conj[yd[x0, r]]], Wt[loop]]],
  Op[Conj[Q[r_]], H[], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[db[x0], Deriv, rst,
             MatchingValues["r" -> r, "x0" -> x0],
             Wt[yd[x0, r]], Wt[loop]]],

  (* Electron Yukawa *)
  (* eb Hc -> Lc *)

  Op[eb[r_], Conj[H[]], rst___] :> Block[{x0 = Unique["x"]},
                                         Op[Conj[L[x0]], Deriv, rst,
                                            MatchingValues["r" -> r, "x0" -> x0],
                                            Wt[Conj[ye[r, x0]]], Wt[loop]]],
  Op[Conj[eb[r_]], H[], rst___] :> Block[{x0 = Unique["x"]},
                                         Op[L[x0], Deriv, rst,
                                            MatchingValues["r" -> r, "x0" -> x0],
                                            Wt[ye[r, x0]], Wt[loop]]],

  (* eb L -> H *)
  Op[eb[r_], L[s_], rst___] :> Op[H[], rst,
                                  MatchingValues["r" -> r, "s" -> s],
                                  Wt[Conj[ye[r, s]]], Wt[loop]],
  Op[Conj[eb[r_]], Conj[L[s_]], rst___] :> Op[Conj[H[]], rst,
                                              MatchingValues["r" -> r, "s" -> s],
                                              Wt[ye[r, s]], Wt[loop]],

  (* L Hc -> ebc *)

  Op[L[r_], Conj[H[]], rst___] :> Block[{x0 = Unique["x"]},
                                        Op[Conj[eb[x0]], Deriv, rst,
                                           MatchingValues["r" -> r, "x0" -> x0],
                                           Wt[Conj[ye[x0, r]]], Wt[loop]]],
  Op[Conj[L[r_]], H[], rst___] :> Block[{x0 = Unique["x"]},
                                        Op[eb[x0], Deriv, rst,
                                           MatchingValues["r" -> r, "x0" -> x0],
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

  Op[L[r_], Conj[L[s_]], rst___] :>
    Op[Delta[r, s], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s],
       Wt[loop]],

  Op[Q[r_], Conj[Q[s_]], rst___] :>
    Op[Delta[r, s], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s],
       Wt[loop]],

  Op[H[], Conj[H[]], rst___] :>
    Op[rst, MatchingValues[], Wt[hloop]]

};

FlavourDeltaRules = {
  Op[Delta[r_, p_], rst___] :>
    (Op[rst] /.  r -> p) ~Join~ Op[MatchingValues["r" -> r, "p" -> p]]
};

$MatchingRulesDim8 =
Join[YukawaRules, LoopRules, FlavourDeltaRules];

$MatchingRulesDim9 =
Join[YukawaRules, LoopRules, FlavourDeltaRules];


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
