OperatorMatchingRulesDim6 = {
  (* Op 1 *)
  Op[
    L[p_, i_], Q[q_, a_, j_], Q[r_, b_, k_], Q[s_, c_, l_],
    Eps[i_, k_], Eps[j_, l_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["1"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], Q[q_, a_, j_], Q[r_, b_, k_], Q[s_, c_, l_],
    Eps[i_, k_], Eps[j_, l_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["1"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Conj[Q[q_, a_, j_]], Conj[Q[r_, b_, k_]], Conj[Q[s_, c_, l_]],
    Eps[i_, k_], Eps[j_, l_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["1"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Conj[Q[q_, a_, j_]], Conj[Q[r_, b_, k_]], Conj[Q[s_, c_, l_]],
    Eps[i_, k_], Eps[j_, l_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["1"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 2 *)
  Op[
    Conj[eb[p_]], Q[q_, a_, i_], Q[r_, b_, j_], Conj[ub[s_, c_]],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["2"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[eb[p_]], Q[q_, a_, i_], Q[r_, b_, j_], Conj[ub[s_, c_]],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["2"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    eb[p_], Conj[Q[q_, a_, i_]], Conj[Q[r_, b_, j_]], ub[s_, c_],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["2"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    eb[p_], Conj[Q[q_, a_, i_]], Conj[Q[r_, b_, j_]], ub[s_, c_],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["2"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 3 *)
  Op[Conj[eb[p_]], Conj[ub[q_, a_]], Conj[ub[r_, b_]], Conj[db[s_, c_]],
     Eps[a_, b_, c_],
     rst___Wt
  ] :> Op[Op["3"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[eb[p_]], Conj[ub[q_, a_]], Conj[ub[r_, b_]], Conj[db[s_, c_]],
    Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["3"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    eb[p_], ub[q_, a_], ub[r_, b_], db[s_, c_],
    Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["3"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    eb[p_], ub[q_, a_], ub[r_, b_], db[s_, c_],
    Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["3"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 4 *)
  Op[
    L[p_, i_], Q[q_, a_, j_], Conj[ub[r_, b_]], Conj[db[s_, c_]],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["4"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    L[p_, i_], Q[q_, a_, j_], Conj[ub[r_, b_]], Conj[db[s_, c_]],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["4"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Conj[Q[q_, a_, j_]], ub[r_, b_], db[s_, c_],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["4"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Deriv, Deriv,
    Conj[L[p_, i_]], Conj[Q[q_, a_, j_]], ub[r_, b_], db[s_, c_],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["4"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]]

};

OperatorMatchingRulesDim7 = {
  (* Op 5 *)
  Op[
    L[p_, i_], db[q_, a_], db[r_, b_], db[s_, c_], Conj[H[j_]],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["5"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Conj[db[q_, a_]], Conj[db[r_, b_]], Conj[db[s_, c_]], H[j_],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["5"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 6a *)
  Op[
    L[p_, i_], Conj[Q[q_, a_, j_]], Conj[Q[r_, b_, k_]], db[s_, c_], H[l_],
    Eps[i_, k_], Eps[j_, l_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["6a"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Q[q_, a_, j_], Q[r_, b_, k_], Conj[db[s_, c_]], Conj[H[l_]],
    Eps[i_, k_], Eps[j_, l_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["6a"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 6b *)
  Op[
    L[p_, i_], Conj[Q[q_, a_, j_]], Conj[Q[r_, b_, k_]], db[s_, c_], H[l_],
    Eps[i_, l_], Eps[j_, k_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["6b"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    Conj[L[p_, i_]], Q[q_, a_, j_], Q[r_, b_, k_], Conj[db[s_, c_]], Conj[H[l_]],
    Eps[i_, l_], Eps[j_, k_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["6b"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 7 *)
  Op[
    Conj[eb[p_]], Conj[Q[q_, a_, i_]], db[r_, b_], db[s_, c_], H[j_],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["7"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  Op[
    eb[p_], Q[q_, a_, i_], Conj[db[r_, b_]], Conj[db[s_, c_]], Conj[H[j_]],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["7"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],

  (* Op 8 *)
  Op[
    L[p_, i_], ub[q_, a_], db[r_, b_], db[s_, c_], H[j_],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Op["8"][p, q, r, s], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]],
  Op[
    Conj[L[p_, i_]], Conj[ub[q_, a_]], Conj[db[r_, b_]], Conj[db[s_, c_]], Conj[H[j_]],
    Eps[i_, j_], Eps[a_, b_, c_],
    rst___Wt
  ] :> Op[Conj[Op["8"][p, q, r, s]], MatchingValues["p" -> p, "q" -> q, "r" -> r, "s" -> s]]

};

DerivativeRules = {
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
                                    ]
};


YukawaRules = {
  (* Up Yukawa *)
  (* ub H \[Rule] Qd *)
  Op[
    ub[r_, a_], H[i_],
    rst___
  ] :> Block[{x0 = Unique["x"]},
             Op[Conj[Q[x0, a, i]], Deriv, rst,
                MatchingValues["r" -> r, "i" -> i, "a" -> a, "x0" -> x0],
                Wt[Conj[yu[r, x0]]], Wt[loop]]
       ],

  Op[
    Conj[ub[r_, a_]], Conj[H[i_]],
    rst___
  ] :> Block[{x0 = Unique["x"]},
             Op[Q[x0, a, i], Deriv,
                rst,
                MatchingValues["r" -> r, "i" -> i, "a" -> a, "x0" -> x0],
                Wt[yu[r, x0]], Wt[loop]]
       ],

  (* ub Q \[Rule] Hd *)
  Op[
    ub[r_, a_], Q[s_, b_, i_],
    rst___
  ] :> Op[Conj[H[i]], Delta[a, b],
          rst,
          MatchingValues["i" -> i, "a" -> a, "b" -> b, "r" -> r, "s" -> s],
          Wt[Conj[yu[r, s]]], Wt[loop]
       ],

  Op[
    Conj[ub[r_, a_]], Conj[Q[s_, b_, i_]],
    rst___
  ] :> Op[H[i], Delta[a, b],
          rst,
          MatchingValues["i" -> i, "a" -> a, "b" -> b, "r" -> r, "s" -> s],
          Wt[yu[r, s]], Wt[loop]
       ],

  (* Q H \[Rule] ubd *)
  Op[Q[r_, a_, i_], H[j_], rst___] :> Block[{x0 = Unique["x"]},
                                            Op[Conj[ub[x0, a]], Eps[i, j], Deriv, rst,
                                               MatchingValues["i" -> i, "j" -> j, "a" -> a, "x0" -> x0,
                                                              "r" -> r],
                                               Wt[Conj[yu[x0, r]]], Wt[loop]]],
  Op[Conj[Q[r_, a_, i_]], Conj[H[j_]], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[ub[x0, a], Eps[i, j], Deriv, rst,
             MatchingValues["i" -> i, "j" -> j, "a" -> a, "x0" -> x0,
                            "r" -> r],
             Wt[yu[x0, r]], Wt[loop]]],

  (* Down Yukawa *)
  (* db Hc -> Qc *)

  Op[db[r_, a_], Conj[H[i_]], rst___] :> Block[{x0 = Unique["x"]},
                                               Op[Conj[Q[x0, a, i]], Deriv, rst,
                                                  MatchingValues["r" -> r, "i" -> i, "a" -> a, "x0" -> x0],
                                                  Wt[Conj[yd[r, x0]]], Wt[loop]]],
  Op[Conj[db[r_, a_]], H[i_], rst___] :> Block[{x0 = Unique["x"]},
                                               Op[Q[x0, a, i], Deriv, rst,
                                                  MatchingValues["r" -> r, "i" -> i, "a" -> a, "x0" -> x0],
                                                  Wt[yd[r, x0]], Wt[loop]]],

  (* db Q -> H *)

  Op[db[r_, a_], Q[s_, b_, i_], rst___] :>
    Op[H[i], Delta[a, b], rst,
       MatchingValues["i" -> i, "a" -> a, "b" -> b, "r" -> r,
                      "s" -> s],
       Wt[Conj[yd[r, s]]], Wt[loop]],
  Op[Conj[db[r_, a_]], Conj[Q[s_, b_, i_]], rst___] :>
    Op[Conj[H[i]], Delta[a, b], rst,
       MatchingValues["i" -> i, "a" -> a, "b" -> b, "r" -> r,
                      "s" -> s],
       Wt[yd[r, s]], Wt[loop]],

  (* Q Hc -> dbc *)

  Op[Q[r_, a_, i_], Conj[H[j_]], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[Conj[db[x0, a]], Eps[i, j], Deriv, rst,
             MatchingValues["i" -> i, "j" -> j, "a" -> a, "r" -> r,
                            "x0" -> x0],
             Wt[Conj[yd[x0, r]]], Wt[loop]]],
  Op[Conj[Q[r_, a_, i_]], H[j_], rst___] :>
    Block[{x0 = Unique["x"]},
          Op[db[x0, a], Eps[i, j], Deriv, rst,
             MatchingValues["i" -> i, "j" -> j, "a" -> a, "r" -> r,
                            "x0" -> x0],
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

  Op[ub[r_, a_], Conj[ub[s_, b_]], rst___] :>
    Op[Delta[r, s], Delta[a, b], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s, "a" -> a, "b" -> b],
       Wt[loop]],

  Op[db[r_, a_], Conj[db[s_, b_]], rst___] :>
    Op[Delta[r, s], Delta[a, b], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s, "a" -> a, "b" -> b],
       Wt[loop]],

  Op[L[r_, i_], Conj[L[s_, j_]], rst___] :>
    Op[Delta[r, s], Eps[i, j], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s, "i" -> i, "j" -> j],
       Wt[loop]],

  Op[Q[r_, a_, i_], Conj[Q[s_, b_, j_]], rst___] :>
    Op[Delta[r, s], Delta[a, b], Eps[i, j], Deriv, rst,
       MatchingValues["r" -> r, "s" -> s, "a" -> a, "b" -> b, "i" -> i,
                      "j" -> j],
       Wt[loop]],

  Op[H[i_], Conj[H[j_]], rst___] :>
    Op[Eps[i, j], rst,
       MatchingValues["i" -> i, "j" -> j],
       Wt[loop]]

};

EpsDeltaRules = {
  Op[Eps[i_, j_], Eps[i_, j_], rst___] :>
    Op[Wt[2], rst,
       MatchingValues[ "i" -> i, "j" -> j]],

  Op[Delta[i_, j_], Delta[i_, j_], rst___] :>
    Op[Wt[3], rst,
       MatchingValues[ "i" -> i, "j" -> j]],

  Op[Eps[m_, n_], Eps[i_, m_], Eps[l_, n_], rst___] :>
    Op[Eps[l, i], rst,
       MatchingValues[ "i" -> i, "m" -> m, "n" -> n, "l" -> l]],

  Op[Delta[a_, c_], Eps[a_, b_, d_], rst___] :>
    Op[Eps[c, b, d], rst,
       MatchingValues["a" -> a, "c" -> c, "b" -> b, "d" -> d]],

  Op[Delta[d_, c_], Delta[c_, a_], Eps[a_, b_, ee_], rst___] :>
    Op[Eps[d, b, e], rst,
       MatchingValues["a" -> a, "c" -> c, "b" -> b, "d" -> d,
                      "ee" -> ee]]
};

FlavourDeltaRules = {
  Op[Delta[r_, p_], rst___] :>
    (Op[rst] /.  r -> p) ~Join~ Op[MatchingValues["r" -> r, "p" -> p]]
};


YukawaTransformations = {
  Op[yu[r_, s_], rst___] :> Block[{y00 = Unique["yuk"]},
                                  Op[Conjugate[Ru[r, y00]], yu[y00], Conjugate[Lu[s, y00]], rst]],
  Op[yd[r_, s_], rst___] :> Block[{y00 = Unique["yuk"]},
                                  Op[Conjugate[Rd[r, y00]], yd[y00], Conjugate[Ld[s, y00]], rst]],
  Op[ye[r_, s_], rst___] :> Block[{y00 = Unique["yuk"]},
                                  Op[Conjugate[Rl[r, y00]], yl[y00], Conjugate[Ll[s, y00]], rst]],

  Op[Conj[yu[r_, s_]], rst___] :> Block[{y00 = Unique["yuk"]},
                                        Op[Ru[r, y00], yu[y00], Lu[s, y00], rst]],
  Op[Conj[yd[r_, s_]], rst___] :> Block[{y00 = Unique["yuk"]},
                                        Op[Rd[r, y00], yd[y00], Ld[s, y00], rst]],
  Op[Conj[ye[r_, s_]], rst___] :> Block[{y00 = Unique["yuk"]},
                                        Op[Rl[r, y00], yl[y00], Ll[s, y00], rst]]
};

ExpandSU2 = {
  Op["1"][r_, s_, t_, uu_] -> {
    d[uu] e[r] u[s] u[t],
    -d[s] e[r] u[t] u[uu],
    -d[t] d[uu] u[s] \[Nu][r],
    d[s] d[t] u[uu] \[Nu][r]
    },

  Op["2"][r_, s_, t_, uu_] -> {
    Conj[eb[r]] Conj[ub[uu]] d[t] u[s],
    Conj[eb[r]] Conj[ub[uu]] d[s] u[t]
    },

  Op["3"][r_, s_, t_, uu_] -> {
    -Conj[db[uu]] Conj[eb[r]] Conj[ub[s]] Conj[ub[t]]
    },

  Op["4"][r_, s_, t_, uu_] -> {
    -Conj[db[uu]] Conj[ub[t]] e[r] u[s],
    -Conj[db[uu]] Conj[ub[t]] d[s] \[Nu][r]
    },

  Op["5"][r_, s_, t_, uu_] -> {
    -Conj[H0] db[s] db[t] db[uu] e[r]
(*,-HM db[s] db[t] db[uu] \[Nu][r]*)
    },

  Op["6a"][r_, s_, t_, uu_] -> {
    H0 Conj[d[s]] Conj[d[t]] db[uu] e[r],
    (*-HP Conj[d[t]] Conj[u[s]] db[uu] e[r],*)

    H0 Conj[d[s]] Conj[u[t]] db[uu] \[Nu][r]
(*,HP Conj[u[s]] Conj[u[t]] db[uu] \[Nu][r]*)
     },

  Op["6b"][r_, s_, t_, uu_] -> {
    (*-HP Conj[d[t]] Conj[u[s]] db[uu] e[r],
     -HP Conj[d[s]] Conj[u[t]] db[uu] e[r],*)

    H0 Conj[d[t]] Conj[u[s]] db[uu] \[Nu][r],
    H0 Conj[d[s]] Conj[u[t]] db[uu] \[Nu][r]
     },

  Op["7"][r_, s_, t_, uu_] -> {
    -H0 Conj[d[s]] Conj[eb[r]] db[t] db[uu]
(*,HP Conj[eb[r]] Conj[u[s]] db[t] db[uu]*)
    },

  Op["8"][r_, s_, t_, uu_] -> {
    (*-HP db[t] db[uu] e[r] ub[
     s],*)
    -H0 db[t] db[uu] ub[s] \[Nu][r]
    }
};

RemoveHiggs = {H0 -> vev/\[CapitalLambda],
               Conj[H0] -> vev/\[CapitalLambda]};

LEFTOperatorMatchingRules = {
  (*\[Delta]B=\[Delta]L=1*)
  Op[u[r_], d[s_], d[t_], \[Nu][u_], rst___] :> Op[Op["^S,LL_udd"][r, s, t, u], rst],
  Op[Conj[u[r_]], Conj[d[s_]], Conj[d[t_]], Conj[\[Nu][u_]], rst___] :> Op[Conj[Op["^S,LL_udd"][r, s, t, u]], rst],

  Op[d[r_], u[s_], u[t_], e[u_], rst___] :> Op[Op["^S,LL_duu"][r, s, t, u], rst],
  Op[Conj[d[r_]], Conj[u[s_]], Conj[u[t_]], Conj[e[u_]], rst___] :> Op[Conj[Op["^S,LL_duu"][r, s, t, u]], rst],

  Op[u[r_], u[s_], Conj[db[t_]], Conj[eb[u_]], rst___] :> Op[Op["^S,LR_uud"][r, s, t, u], rst],
  Op[Conj[u[r_]], Conj[u[s_]], db[t_], eb[u_], rst___] :> Op[Conj[Op["^S,LR_uud"][r, s, t, u]], rst],

  Op[d[r_], u[s_], Conj[ub[t_]], Conj[eb[u_]], rst___] :> Op[Op["^S,LR_duu"][r, s, t, u], rst],
  Op[Conj[d[r_]], Conj[u[s_]], ub[t_], eb[u_], rst___] :> Op[Conj[Op["^S,LR_duu"][r, s, t, u]], rst],

  Op[Conj[ub[r_]], Conj[ub[s_]], d[t_], e[u_], rst___] :> Op[Op["^S,RL_uud"][r, s, t, u], rst],
  Op[ub[r_], ub[s_], Conj[d[t_]], Conj[e[u_]], rst___] :> Op[Conj[Op["^S,RL_uud"][r, s, t, u]], rst],

  Op[Conj[db[r_]], Conj[ub[s_]], u[t_], e[u_], rst___] :> Op[Op["^S,RL_duu"][r, s, t, u], rst],
  Op[db[r_], ub[s_], Conj[u[t_]], Conj[e[u_]], rst___] :> Op[Conj[Op["^S,RL_duu"][r, s, t, u]], rst],

  Op[Conj[db[r_]], Conj[ub[s_]], d[t_], \[Nu][u_], rst___] :> Op[Op["^S,RL_dud"][r, s, t, u], rst],
  Op[db[r_], ub[s_], Conj[d[t_]], Conj[\[Nu][u_]], rst___] :> Op[Conj[Op["^S,RL_dud"][r, s, t, u]], rst],

  Op[Conj[db[r_]], Conj[db[s_]], u[t_], \[Nu][u_], rst___] :> Op[Op["^S,RL_ddu"][r, s, t, u], rst],
  Op[db[r_], db[s_], Conj[u[t_]], Conj[\[Nu][u_]], rst___] :> Op[Conj[Op["^S,RL_ddu"][r, s, t, u]], rst],

  Op[Conj[db[r_]], Conj[ub[s_]], Conj[ub[t_]], Conj[eb[u_]], rst___] :> Op[Op["^S,RR_duu"][r, s, t, u], rst],
  Op[db[r_], ub[s_], ub[t_], eb[u_], rst___] :> Op[Conj[Op["^S,RR_duu"][r, s, t, u]], rst],

  (*\[Delta]B=-\[Delta]L=1*)
  Op[d[r_], d[s_], eb[t_], d[u_], rst___] :> Op[Op["^S,LL_ddd"][r, s, t, u], rst],
  Op[Conj[d[r_]], Conj[d[s_]], Conj[eb[t_]], Conj[d[u_]], rst___] :> Op[Conj[Op["^S,LL_ddd"][r, s, t, u]], rst],

  Op[u[r_], d[s_], Conj[\[Nu][t_]], Conj[db[u_]], rst___] :> Op[Op["^S,LR_udd"][r, s, t, u], rst],
  Op[Conj[u[r_]], Conj[d[s_]], \[Nu][t_], db[u_], rst___] :> Op[Conj[Op["^S,LR_udd"][r, s, t, u]], rst],

  Op[d[r_], d[s_], Conj[\[Nu][t_]], Conj[ub[u_]], rst___] :> Op[Op["^S,LR_ddu"][r, s, t, u], rst],
  Op[Conj[d[r_]], Conj[d[s_]], \[Nu][t_], ub[u_], rst___] :> Op[Conj[Op["^S,LR_ddu"][r, s, t, u]], rst],

  Op[d[r_], d[s_], Conj[e[t_]], Conj[db[u_]], rst___] :> Op[Op["^S,LR_ddd"][r, s, t, u], rst],
  Op[Conj[d[r_]], Conj[d[s_]], e[t_], db[u_], rst___] :> Op[Conj[Op["^S,LR_ddd"][r, s, t, u]], rst],

  Op[Conj[db[r_]], Conj[db[s_]], eb[t_], d[u_], rst___] :> Op[Op["^S,RL_ddd"][r, s, t, u], rst],
  Op[db[r_], db[s_], Conj[eb[t_]], Conj[d[u_]], rst___] :> Op[Conj[Op["^S,RL_ddd"][r, s, t, u]], rst],

  Op[Conj[ub[r_]], Conj[db[s_]], Conj[\[Nu][t_]], Conj[db[u_]], rst___] :> Op[Op["^S,RR_udd"][r, s, t, u], rst],
  Op[ub[r_], db[s_], \[Nu][t_], db[u_], rst___] :> Op[Conj[Op["^S,RR_udd"][r, s, t, u]], rst],

  Op[Conj[db[r_]], Conj[db[s_]], Conj[e[t_]], Conj[db[u_]], rst___] :> Op[Op["^S,RR_ddd"][r, s, t, u], rst],
  Op[db[r_], db[s_], e[t_], db[u_], rst___] :> Op[Conj[Op["^S,RR_ddd"][r, s, t, u]], rst]

};

ToMassBasis = {
  \[Nu][r_] :> Block[{y00 = Unique["mass"]}, Ll[r, y00] \[Nu][y00]],
  e[r_] :> Block[{y00 = Unique["mass"]}, Ll[r, y00] e[y00]],
  u[r_] :> Block[{y00 = Unique["mass"]}, Lu[r, y00] u[y00]],
  d[r_] :> Block[{y00 = Unique["mass"]}, Ld[r, y00] d[y00]],
  eb[r_] :> Block[{y00 = Unique["mass"]}, Rl[r, y00] eb[y00]],
  ub[r_] :> Block[{y00 = Unique["mass"]}, Ru[r, y00] ub[y00]],
  db[r_] :> Block[{y00 = Unique["mass"]}, Rd[r, y00] db[y00]]
};

MixingMatrixRules = {

  Op[Conjugate[Lu[x_, y_]], Ld[x_, z_], rst__] :> Op[CKM[y, z], rst],

  Op[Conjugate[Lu[x_, y_]], Lu[x_, z_], rst__] :> (Op[rst] /. y -> z),
  Op[Conjugate[Ld[x_, y_]], Ld[x_, z_], rst__] :> (Op[rst] /. y -> z),
  Op[Conjugate[Ll[x_, y_]], Ll[x_, z_], rst__] :> (Op[rst] /. y -> z),

  Op[Conjugate[Ru[x_, y_]], Ru[x_, z_], rst__] :> (Op[rst] /. y -> z),
  Op[Conjugate[Rd[x_, y_]], Rd[x_, z_], rst__] :> (Op[rst] /. y -> z),
  Op[Conjugate[Rl[x_, y_]], Rl[x_, z_], rst__] :> (Op[rst] /. y -> z)

};

ToUpDiagonalBasis = {
  Op[Ld[x_, y_], rst__] :> Op[CKM[x, y], rst],
  Op[Lu[x_, y_], rst__] :> (Op[rst] /. y -> x),
  Op[Ll[x_, y_], rst__] :> (Op[rst] /. y -> x),

  Op[Ru[x_, y_], rst__] :> (Op[rst] /. y -> x),
  Op[Rl[x_, y_], rst__] :> (Op[rst] /. y -> x),
  Op[Rd[x_, y_], rst__] :> (Op[rst] /. y -> x),

  Op[Conjugate[Ld[x_, y_]], rst__] :> Op[Conjugate[CKM[x, y]], rst],
  Op[Conjugate[Lu[x_, y_]], rst__] :> (Op[rst] /. y -> x),
  Op[Conjugate[Ll[x_, y_]], rst__] :> (Op[rst] /. y -> x),

  Op[Conjugate[Ru[x_, y_]], rst__] :> (Op[rst] /. y -> x),
  Op[Conjugate[Rl[x_, y_]], rst__] :> (Op[rst] /. y -> x),
  Op[Conjugate[Rd[x_, y_]], rst__] :> (Op[rst] /. y -> x)
};

$MatchingRulesDim8 =
Join[YukawaRules, LoopRules, EpsDeltaRules, OperatorMatchingRulesDim6];

$MatchingRulesDim9 =
Join[YukawaRules, LoopRules, EpsDeltaRules, FlavourDeltaRules, DerivativeRules, OperatorMatchingRulesDim7];


(* LEFT Symmetries, or should this be done at the level of the SMEFT? *)

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
