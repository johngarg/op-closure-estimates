BViolatingOperatorsDim8 = <|
  "11" -> Op[Wt[G["11"][r,s,t,u]], Deriv, L[r], Q[s], Q[t], Conj[db[u]], H[]],
  "12" -> Op[Wt[G["12"][r,s,t,u]], L[r], Conj[Deriv, ub[s]], Conj[db[t]], Conj[db[u]], H[]],
  "13" -> Op[Wt[G["13"][r,s,t,u]], L[r], Conj[ub[s]], Conj[ub[t]], Conj[Deriv, db[u]], Conj[H[]]],
  "14" -> Op[Wt[G["14"][r,s,t,u]], L[r], Q[s], Conj[ub[t]], Conj[ub[u]], Conj[H[]], Conj[H[]]],
  "15" -> Op[Wt[G["15"][r,s,t,u]], Conj[eb[r]], Q[s], Q[t], Conj[db[u]], H[], H[]],
  "16" -> Op[Wt[G["16"][r,s,t,u]], L[r], Q[s], Conj[db[t]], Conj[db[u]], H[], H[]],
  "17" -> Op[Wt[G["17"][r,s,t,u]], Conj[Deriv, eb[r]], Q[s], Conj[ub[t]], Conj[ub[u]], Conj[H[]]],
  "18" -> Op[Wt[G["18"][r,s,t,u]], L[r], Q[s], Q[t], Q[u], H[], Conj[H[]]],
  "19" -> Op[Wt[G["19"][r,s,t,u]], Deriv, L[r], Q[s], Q[t], Conj[ub[u]], Conj[H[]]],
  "20" -> Op[Wt[G["20"][r,s,t,u]], Conj[eb[r]], Q[s], Q[t], Deriv, Q[u], H[]],
  "21" -> Op[Wt[G["21"][r,s,t,u]], Conj[eb[r]], Q[s], Conj[ub[t]], Conj[Deriv, db[u]], H[]],
  "22" -> Op[Wt[G["22"][r,s,t,u]], Conj[eb[r]], Q[s], Q[t], Conj[ub[u]], H[], Conj[H[]]],
  "23" -> Op[Wt[G["23"][r,s,t,u]], Conj[eb[r]], Conj[ub[s]], Conj[ub[t]], Conj[db[u]], H[], Conj[H[]]],
  "24" -> Op[Wt[G["24"][r,s,t,u]], L[r], Q[s], Conj[ub[t]], Conj[db[u]], H[], Conj[H[]]]
|>;

BViolatingOperatorsDim9 = <|
  "25" -> Op[Wt[G["25"][r,s,t,u,v,w]], Conj[eb[r]], Conj[eb[s]], eb[t], db[u], db[v], db[w]],
  "26" -> Op[Wt[G["26"][r,s,t,u]], Conj[eb[r]], Conj[Q[s]], Conj[Q[t]], Conj[Q[u]], H[], H[], H[]],
  "27" -> Op[Wt[G["27"][r,s,t,u,v,w]], Conj[eb[r]], db[s], db[t], db[u], db[v], Conj[db[w]]],
  "28" -> Op[Wt[G["28"][r,s,t,u,v,w]], L[r], L[s], eb[t], ub[u], db[v], db[w]],
  "29" -> Op[Wt[G["29"][r,s,t,u,v,w]], Conj[eb[r]], Conj[Q[s]], Conj[Q[t]], Conj[ub[u]], db[v], db[w]],
  "30" -> Op[Wt[G["30"][r,s,t,u,v,w]], L[r], L[s], eb[t], Conj[Q[u]], Conj[Q[v]], db[w]],
  "31" -> Op[Wt[G["31"][r,s,t,u,v,w]], L[r], L[s], Conj[L[t]], Conj[Q[u]], db[v], db[w]],
  "32" -> Op[Wt[G["32"][r,s,t,u,v,w]], L[r], Conj[Q[s]], db[t], db[u], db[v], Conj[db[w]]],
  "33" -> Op[Wt[G["33"][r,s,t,u,v,w]], Conj[eb[r]], ub[s], Conj[ub[t]], db[u], db[v], db[w]],
  "34" -> Op[Wt[G["34"][r,s,t,u]], Conj[Deriv, eb[r]], Conj[Q[s]], Conj[Q[t]], db[u], H[], H[]],
  "35" -> Op[Wt[G["35"][r,s,t,u,v,w]], L[r], Conj[L[s]], Conj[eb[t]], db[u], db[v], db[w]],
  "36" -> Op[Wt[G["36"][r,s,t,u]], L[r], db[s], db[t], db[u], Conj[H[]], Conj[H[]], H[]],
  "37" -> Op[Wt[G["37"][r,s,t,u]], L[r], Conj[Q[s]], Conj[Q[t]], ub[u], H[], H[], H[]],
  "38" -> Op[Wt[G["38"][r,s,t,u]], L[r], Conj[Q[s]], Conj[Q[t]], Conj[Deriv, Q[u]], H[], H[]],
  "39" -> Op[Wt[G["39"][r,s,t,u,v,w]], Conj[eb[r]], Q[s], Conj[Q[t]], db[u], db[v], db[w]],
  "40" -> Op[Wt[G["40"][r,s,t,u,v,w]], L[r], Conj[Q[s]], Conj[Q[t]], Conj[Q[u]], Conj[ub[v]], db[w]],
  "41" -> Op[Wt[G["41"][r,s,t,u,v,w]], L[r], Q[s], ub[t], db[u], db[v], db[w]],
  "42" -> Op[Wt[G["42"][r,s,t,u,v,w]], L[r], Conj[Q[s]], Conj[Q[t]], Q[u], db[v], db[w]],
  "43" -> Op[Wt[G["43"][r,s,t,u]], Deriv, L[r], Conj[Q[s]], db[t], db[u], H[], Conj[H[]]],
  "44" -> Op[Wt[G["44"][r,s,t,u]], Deriv, L[r], Conj[Q[s]], ub[t], db[u], H[], H[]],
  "45" -> Op[Wt[G["45"][r,s,t,u]], L[r], Conj[Q[s]], Conj[Q[t]], db[u], H[], H[], Conj[H[]]],
  "46" -> Op[Wt[G["46"][r,s,t,u]], L[r], ub[s], db[t], db[u], H[], H[], Conj[H[]]],
  "47" -> Op[Wt[G["47"][r,s,t,u]], Conj[eb[r]], Conj[Q[s]], db[t], db[u], H[], H[], Conj[H[]]],
  "48" -> Op[Wt[G["48"][r,s,t,u]], Conj[eb[r]], db[s], db[t], Deriv, db[u], H[], Conj[H[]]],
  "49" -> Op[Wt[G["49"][r,s,t,u,v,w]], L[r], eb[s], Conj[eb[t]], Conj[Q[u]], db[v], db[w]],
  "50" -> Op[Wt[G["50"][r,s,t,u,v,w]], L[r], Conj[Q[s]], ub[t], Conj[ub[u]], db[v], db[w]]
  |>;

(* Arbitrarily start the numbering here at 101 *)
BViolatingOperatorsDim10 = <|
  "101" -> Op[Wt[G["101"][r,s,t,u,v,w]], Conj[eb[r]], Q[s], Q[t], Conj[Q[u]], Conj[ub[v]], Conj[ub[w]], Conj[H[]]],
  "102" -> Op[Wt[G["102"][r,s,t,u,v,w]], L[r], ub[s], Conj[ub[t]], Conj[ub[u]], Conj[ub[v]], Conj[db[w]], Conj[H[]]],
  "103" -> Op[Wt[G["103"][r,s,t,u,v,w]], L[r], Q[s], Conj[Q[t]], Conj[ub[u]], Conj[ub[v]], Conj[db[w]], Conj[H[]]],
  "104" -> Op[Wt[G["104"][r,s,t,u,v,w]], Conj[eb[r]], Q[s], ub[t], Conj[ub[u]], Conj[ub[v]], Conj[db[w]], Conj[H[]]],
  "105" -> Op[Wt[G["105"][r,s,t,u,v,w]], Conj[eb[r]], Conj[Q[s]], Conj[ub[t]], Conj[ub[u]], Conj[db[v]], Conj[db[w]], H[]],
  "106" -> Op[Wt[G["106"][r,s,t,u,v,w]], Conj[eb[r]], Conj[Q[s]], Conj[ub[t]], Conj[ub[u]], Conj[ub[v]], Conj[db[w]], Conj[H[]]],
  "107" -> Op[Wt[G["107"][r,s,t,u,v,w]], Conj[eb[r]], Q[s], Conj[ub[t]], Conj[ub[u]], db[v], Conj[db[w]], Conj[H[]]],
  "108" -> Op[Wt[G["108"][r,s,t,u,v,w]], L[r], Conj[ub[s]], Conj[ub[t]], db[u], Conj[db[v]], Conj[db[w]], Conj[H[]]],
  "109" -> Op[Wt[G["109"][r,s,t,u,v,w]], L[r], Q[s], Q[t], ub[u], Conj[ub[v]], Conj[ub[w]], Conj[H[]]],
  "110" -> Op[Wt[G["110"][r,s,t,u,v,w]], Conj[eb[r]], Q[s], ub[t], Conj[ub[u]], Conj[ub[v]], Conj[db[w]], H[]],
  "111" -> Op[Wt[G["111"][r,s,t,u,v,w]], L[r], ub[s], Conj[ub[t]], Conj[ub[u]], Conj[db[v]], Conj[db[w]], H[]]
  |>;
