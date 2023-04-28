Dim6and7Symmetries::usage = "Repalcement rule of symmetries arrising from
relabelling equivalence in the operators as we define them.";
Dim6and7Symmetries = {
        Op["1"][r_, OrderlessPatternSequence[s_, t_, u_]] :>
          Op["1"][r, s, t, u],
        Op["2"][r_, OrderlessPatternSequence[s_, t_], u_] :>
          Op["2"][r, s, t, u],
        Op["3"][r_, OrderlessPatternSequence[s_, t_], u_] :>
          Op["3"][r, s, t, u],
        Op["5"][r_, OrderlessPatternSequence[s_, t_, u_]] :>
          Op["5"][r, s, t, u],
        Op["6"][r_, s_, OrderlessPatternSequence[t_, u_]] :>
          Op["6"][r, s, t, u],
        Op["7"][r_, OrderlessPatternSequence[s_, t_, u_]] :>
          Op["7"][r, s, t, u],
        Op["8"][r_, OrderlessPatternSequence[s_, t_], u_] :>
          Op["8"][r, s, t, u],
        Op["9"][r_, s_, OrderlessPatternSequence[t_, u_]] :>
          Op["9"][r, s, t, u],
        Op["10"][r_, s_, OrderlessPatternSequence[t_, u_]] :>
          Op["10"][r, s, t, u]
};

Dim8and9Symmetries::usage = "Repalcement rule of symmetries arrising from
relabelling equivalence in the operators as we define them.";
Dim8and9Symmetries = {
        G["11"][r_, OrderlessPatternSequence[s_, t_], u_] :>
         G["11"][r, s, t, u],
        G["12"][r_, s_, OrderlessPatternSequence[t_, u_]] :>
         G["12"][r, s, t, u],
        G["13"][r_, OrderlessPatternSequence[s_, t_], u_] :>
         G["13"][r, s, t, u],
        G["14"][r_, s_, OrderlessPatternSequence[t_, u_]] :>
         G["14"][r, s, t, u],
        G["15"][r_, OrderlessPatternSequence[s_, t_], u_] :>
         G["15"][r, s, t, u],
        G["16"][r_, s_, OrderlessPatternSequence[t_, u_]] :>
         G["16"][r, s, t, u],
        G["17"][r_, s_, OrderlessPatternSequence[t_, u_]] :>
         G["17"][r, s, t, u],
        G["18"][r_, OrderlessPatternSequence[s_, t_, u_]] :>
         G["18"][r, s, t, u],
        G["19"][r_, OrderlessPatternSequence[s_, t_], u_] :>
         G["19"][r, s, t, u],
        G["20"][r_, OrderlessPatternSequence[s_, t_, u_]] :>
         G["20"][r, s, t, u],
        G["22"][r_, OrderlessPatternSequence[s_, t_], u_] :>
         G["22"][r, s, t, u],
        G["23"][r_, OrderlessPatternSequence[s_, t_], u_] :>
         G["23"][r, s, t, u],
        G["25"][OrderlessPatternSequence[r_, s_], t_, OrderlessPatternSequence[u_, v_, w_]] :>
         G["25"][r, s, t, u, v, w],
        G["26"][r_, OrderlessPatternSequence[s_, t_, u_]] :>
         G["26"][r, s, t, u],
        G["27"][r_, OrderlessPatternSequence[s_, t_, u_, v_], w_] :>
         G["27"][r, s, t, u, v, w],
        G["28"][OrderlessPatternSequence[r_, s_], t_, u_, OrderlessPatternSequence[v_, w_]] :>
         G["28"][r, s, t, u, v, w],
        G["29"][r_, OrderlessPatternSequence[s_, t_], u_, OrderlessPatternSequence[v_, w_]] :>
         G["29"][r, s, t, u, v, w]
};

(* Propagate the P head through functions *)
P[f_[x__]] := f @@ P /@ List[x];

Relabellings::usage = "Go from an association rule

  <|P[r] -> s, P[x] -> x, P[p] -> p, P[q] -> q, P[s] -> r|>

to a replacement rule like

  {r -> s, x -> x, p -> p, q -> q, s -> r}

";
Relabellings[frame_] := Normal[frame] /. P -> Identity;

IsSymmetricRelabelling::usage = "Checks whether the relabelling is symmetric.";
IsSymmetricRelabelling[op_, match_] :=
  op === (op /. Relabellings[match] /. Dim8and9Symmetries);

MatchingContributionsAreEquivalentUpToRelabelling[expr1_, expr2_] :=
  Block[{expr1NoG, expr2NoG, op, match},
   op = expr1 /. Times[z___, G[x_][y__], w___] :> G[x][y];
   expr1NoG = expr1 /. G[x_][y__] :> 1;
   expr2NoG = expr2 /. G[x_][y__] :> 1;
   match = PatternMatch[P[List @@ expr1NoG], List @@ expr2NoG];
   If[match === False, False, IsSymmetricRelabelling[op, match]]
   ];

RemoveEquivalentBy::usage = "General function to remove equivalent terms from a
list of terms. Equivalence is judged by the function f[x_,y_].";
RemoveEquivalentBy[f_][diags_] := Block[{i, j, copyDiags},
   copyDiags = diags;
   i = 1;
   While[i < Length[copyDiags], j = i + 1;
    While[j <= Length[copyDiags],
     If[f[copyDiags[[i]], copyDiags[[j]]],
       copyDiags = Delete[copyDiags, j];, j++; Nothing];];
    i++];
   copyDiags];

RemoveEquivalent[diags_] :=
  RemoveEquivalentBy[
    MatchingContributionsAreEquivalentUpToRelabelling][
   DeleteDuplicates[diags]];
RelabelDummyFlavourIndices[expr_] :=
 Block[{indices =
    expr /. Times[z___, Op[x_][y__], w___] :>
      DeleteDuplicates@List[y]},
  expr /. GetFlavourRelabellings[indices]]

RelabelFlavourIndices[expr_] :=
 Block[{indices =
    expr /. Times[z___, G[x_][y__], w___] :>
      DeleteDuplicates@List[y]},
  expr /. MapThread[
    Rule, {indices, Take[{p, q, r, s, t, u}, Length[indices]]}]]

RewriteMatchingExpression[expr_] :=
        expr /. (Times[z___, Op[x_][y__], w___] :> G[x][y] -> Times[z, w]);
