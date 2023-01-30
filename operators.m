BViolatingOperatorsDim8 = <|

  "9" -> Op[Wt[G["9"][p, q, r, s]],
            L[p, i], Q[q, j], Conj[ub[r]], Conj[ub[s]], Conj[H[k]], Conj[H[l]],
            Eps[i, k], Eps[j, l]
         ],

  "10" -> Op[Wt[G["10"][p, q, r, s]],
             Conj[eb[p]], Q[q, i], Q[r, j], Conj[db[s]], H[k], H[l],
             Eps[k, i], Eps[j, l]
          ],

  "11" -> Op[Wt[G["11"][p, q, r, s]],
             L[p, i], Q[q, j], Conj[db[r]], Conj[db[s]], H[k], H[l],
             Eps[k, i], Eps[j, l]
          ],

  "12a" -> Op[Wt[G["12a"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, l], Eps[j, m], Eps[k, n]
           ],

  "12b" -> Op[Wt[G["12b"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, m], Eps[j, l], Eps[k, n]
           ],

  "12c" -> Op[Wt[G["12c"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, k], Eps[j, l], Eps[m, n]
           ],

  "12d" -> Op[Wt[G["12d"][p, q, r, s]],
              L[p, i], Q[q, j], Q[r, k], Q[s, l], H[m], Conj[H[n]],
              Eps[i, n], Eps[j, l], Eps[k, m]
           ],

  "13a" -> Op[Wt[G["13a"][p, q, r, s]],
              Conj[eb[p]], Q[q, i], Q[r, j], Conj[ub[s]], H[k], Conj[H[l]],
              Eps[i, k], Eps[j, l]
           ],

  "13b" -> Op[Wt[G["13b"][p, q, r, s]],
              Conj[eb[p]], Q[q, i], Q[r, j], Conj[ub[s]], H[k], Conj[H[l]],
              Eps[i, j], Eps[k, l]
           ],

  "14" -> Op[Wt[G["14"][p, q, r, s]],
             Conj[eb[p]], Conj[ub[q]], Conj[ub[r]], Conj[db[s]], H[i], Conj[H[j]],
             Eps[i, j]
          ],

  "15a" -> Op[Wt[G["15a"][p, q, r, s]],
              L[p, i], Q[q, j], Conj[ub[r, b]], Conj[db[s]], H[k], Conj[H[l]],
              Eps[i, k], Eps[j, l]
           ],

  "15b" -> Op[Wt[G["15b"][p, q, r, s]],
              L[p, i], Q[q, j], Conj[ub[r]], Conj[db[s]], H[k], Conj[H[l]],
              Eps[i, l], Eps[j, k]
           ],

  "15c" -> Op[Wt[G["15c"][p, q, r, s]],
              L[p, i], Q[q, j], Conj[ub[r]], Conj[db[s]], H[k], Conj[H[l]],
              Eps[i, j], Eps[k, l]
           ]

|>;

BViolatingOperatorsDim9 = <|

  "19"  -> Op[Wt[G["19"][p,q,r,s,t,u]],
              Conj[eb[p]], Conj[eb[q]], eb[r], db[s], db[t], db[u]
           ],

  "20"  -> Op[Wt[G["20"][p,q,r,s]],
              Conj[eb[p]], Conj[Q[q,i]], Conj[Q[r,j]], Conj[Q[s,k]], H[l], H[m], H[n],
              Eps[i, l], Eps[j, m], Eps[k, n]
           ]

(* , "21"  -> Prod[G["21"][r,s,t,u,v,w] *)
(*               , Conj[eb[r]], db[s,a], db[t,b], db[u,c], db[v,d], Conj[db[w,e]] *)
(*            ] *)

(*       , "22"  -> Prod[G["22"][r,s,t,u,v,w] *)
(*                     , L[r,i], L[s,j], eb[t], ub[u,a], db[v,b], db[w,c] *)
(*                     , Eps[j,i] *)
(*                  ] *)
(*       , "23"  -> Prod[G["23"][r,s,t,u,v,w] *)
(*                     , Conj[eb[r]], Conj[Q[s,a,i]], Conj[Q[t,b,j]], Conj[ub[u,c]], db[v,d], db[w,e] *)
(*                     , Eps[j,i] *)
(*                  ] *)
(*       , "24a" -> Prod[G["24a"][r,s,t,u,v,w] *)
(*                     , L[r,i], L[s,l], eb[t], Conj[Q[u,a,i]], Conj[Q[v,b,l]], db[w,c] *)
(*                  ] *)
(*       , "24b" -> Prod[G["24b"][r,s,t,u,v,w] *)
(*                     , L[r,i], L[s,j], eb[t], Conj[Q[u,a,k]], Conj[Q[v,b,l]], db[w,c] *)
(*                     , Eps[j,i], Eps[l,k] *)
(*                  ] *)
(*       , "25a" -> Prod[G["25a"][r,s,t,u,v,w] *)
(*                     , L[r,i], L[s,l], Conj[L[t,i]], Conj[Q[u,a,l]], db[v,b], db[w,c] *)
(*                  ] *)
(*       , "25b" -> Prod[G["25b"][r,s,t,u,v,w] *)
(*                     , L[r,i], L[s,j], Conj[L[t,k]], Conj[Q[u,a,l]], db[v,b], db[w,c] *)
(*                     , Eps[j,i], Eps[l,k] *)
(*                  ] *)
(*       , "26"  -> Prod[G["26"][r,s,t,u,v,w] *)
(*                     , L[r,j], Conj[Q[s,a,j]], db[t,b], db[u,c], db[v,d], Conj[db[w,e]] *)
(*                  ] *)
(*       , "27"  -> Prod[G["27"][r,s,t,u,v,w] *)
(*                     , Conj[eb[r]], ub[s,a], Conj[ub[t,b]], db[u,c], db[v,d], db[w,e] *)
(*                  ] *)
(*       , "28"  -> Prod[G["28"][r,s,t,u,v,w] *)
(*                     , L[r,j], Conj[L[s,j]], Conj[eb[t]], db[u,a], db[v,b], db[w,c] *)
(*                  ] *)
(*       , "29"  -> Prod[G["29"][r,s,t,u] *)
(*                     , L[r,i], db[s,a], db[t,b], db[u,c], Conj[H[j]], Conj[H[i]], H[j] *)
(*                  ] *)
(*       , "30"  -> Prod[G["30"][r,s,t,u] *)
(*                     , L[r,i], Conj[Q[s,a,l]], Conj[Q[t,b,m]], ub[u,c], H[l], H[m], H[n] *)
(*                     , Eps[i,n] *)
(*                  ] *)
(*       , "31"  -> Prod[G["31"][r,s,t,u,v,w] *)
(*                     , Conj[eb[r]], Q[s,a,j], Conj[Q[t,b,j]], db[u,c], db[v,d], db[w,e] *)
(*                  ] *)
(*       , "32"  -> Prod[G["32"][r,s,t,u,v,w] *)
(*                     , L[r,i], Conj[Q[s,a,j]], Conj[Q[t,b,i]], Conj[Q[u,c,l]], Conj[ub[v,d]], db[w,e] *)
(*                     , Eps[j,l] *)
(*                  ] *)
(*       , "33"  -> Prod[G["33"][r,s,t,u,v,w] *)
(*                     , L[r,i], Q[s,a,j], ub[t,b], db[u,c], db[v,d], db[w,e] *)
(*                     , Eps[j,i] *)
(*                  ] *)
(*       , "34a" -> Prod[G["34a"][r,s,t,u,v,w] *)
(*                     , L[r,j], Conj[Q[s,a,j]], Conj[Q[t,b,l]], Q[u,c,l], db[v,d], db[w,e] *)
(*                  ] *)
(*       , "34b" -> Prod[G["34b"][r,s,t,u,v,w] *)
(*                     , L[r,i], Conj[Q[s,a,j]], Conj[Q[t,b,k]], Q[u,c,l], db[v,d], db[w,e] *)
(*                     , Eps[k,j], Eps[l,i] *)
(*                  ] *)
(*       , "35a" -> Prod[G["35a"][r,s,t,u] *)
(*                     , L[r,i], Conj[Q[s,a,i]], Conj[Q[t,b,l]], db[u,c], H[l], H[m], Conj[H[m]] *)
(*                  ] *)
(*       , "35b" -> Prod[G["35b"][r,s,t,u] *)
(*                     , L[r,i], Conj[Q[s,a,j]], Conj[Q[t,b,l]], db[u,c], H[l], H[m], Conj[H[n]] *)
(*                     , Eps[j,n], Eps[i,m] *)
(*                  ] *)
(*       , "35c" -> Prod[G["35c"][r,s,t,u] *)
(*                     , L[r,i], Conj[Q[s,a,j]], Conj[Q[t,b,k]], db[u,c], H[l], H[m], Conj[H[l]] *)
(*                     , Eps[j,k], Eps[i,m] *)
(*                  ] *)
(*       , "35d" -> Prod[G["35d"][r,s,t,u] *)
(*                     , L[r,i], Conj[Q[s,a,l]], Conj[Q[t,b,k]], db[u,c], H[l], H[k], Conj[H[i]] *)
(*                  ] *)
(*       , "36"  -> Prod[G["36"][r,s,t,u] *)
(*                     , L[r,i], ub[s,a], db[t,b], db[u,c], H[j], H[k], Conj[H[j]] *)
(*                     , Eps[i,k] *)
(*                  ] *)
(*       , "37"  -> Prod[G["37"][r,s,t,u] *)
(*                     , Conj[eb[r]], Conj[Q[s,a,i]], db[t,b], db[u,c], H[j], H[i], Conj[H[j]] *)
(*                  ] *)
(*       , "38"  -> Prod[G["38"][r,s,t,u,v,w] *)
(*                     , L[r,j], eb[s], Conj[eb[t]], Conj[Q[u,a,j]], db[v,b], db[w,c] *)
(*                  ] *)
(*       , "39"  -> Prod[G["39"][r,s,t,u,v,w] *)
(*                     , L[r,j], Conj[Q[s,a,j]], ub[t,b], Conj[ub[u,c]], db[v,d], db[w,e] *)
(*                  ] *)

  |>;
