(* ::Package:: *)

(* ::Input:: *)
(*Quit[]*)


(* ::Input:: *)
(*Needs["MaTeX`"]*)


(* ::Input:: *)
(*SetOptions[MaTeX,FontSize->19];*)
(*MaTeX["x+5"]*)


(* ::Input:: *)
(*$Path=Append[$Path,NotebookDirectory[]<>"../"];*)


(* ::Input:: *)
(*Get["main.m"];*)
(*Get["operators.m"];*)
(*Get["rules.m"];*)
(*Get["decay.m"];*)
(*Get["pmatch.m"];*)
(*Get["symmetries.m"];*)


(* ::Text:: *)
(*Okay so you need to alter ToStringRep to accept Graphics objects and continue as you are. You will also need to remove a whole branch of the tree by symmetry.*)


(* ::Input:: *)
(*MultiwayGraph@MatchOperator[BViolatingOperatorsDim8["16"],$MatchingRulesDim8,4]*)


(* ::Input:: *)
(*o16MultiwayGraph=Block[{edgeList},*)
(*edgeList=EdgeList@MultiwayGraph@MatchOperator[BViolatingOperatorsDim8["16"],$MatchingRulesDim8,4];*)
(*Print[edgeList[[11]]];*)
(*edgeList[[1]]=maTeX["L_r Q_s \\bar{d}_{t}^{\\dagger} \\bar{d}_{u}^{\\dagger} H H"]\[DirectedEdge]{maTeX["L_r Q_s \\bar{d}_{t}^{\\dagger} \\bar{d}_{u}^{\\dagger} H H"],maTeX["Q_s H"]:>maTeX["\\partial \\bar{u}^\\dagger_x"]};*)
(*edgeList[[2]]=maTeX["L_r Q_s \\bar{d}_{t}^{\\dagger} \\bar{d}_{u}^{\\dagger} H H"]\[DirectedEdge]{maTeX["L_r Q_s \\bar{d}_{t}^{\\dagger} \\bar{d}_{u}^{\\dagger} H H"],maTeX["\\bar{d}^\\dagger_t H"]:>maTeX["\\partial Q_x"]};*)
(*edgeList[[3]]=Nothing;*)
(*edgeList[[4]]={maTeX["L_r Q_s \\bar{d}_{t}^{\\dagger} \\bar{d}_{u}^{\\dagger} H H"],maTeX["Q_s H"]:>maTeX["\\partial \\bar{u}^\\dagger_x"]}\[DirectedEdge]maTeX["L_r \\partial \\bar{u}^\dagger_x \\bar{d}_t^\\dagger \\bar{d}_u^\\dagger H"];*)
(*edgeList[[5]]={maTeX["L_r Q_s \\bar{d}_{t}^{\\dagger} \\bar{d}_{u}^{\\dagger} H H"],maTeX["\\bar{d}^\\dagger_t H"]:>maTeX["\\partial Q_x"]}\[DirectedEdge]maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"];*)
(*edgeList[[6]]=Nothing;*)
(*edgeList[[7]]=maTeX["L_r \\partial \\bar{u}^\dagger_x \\bar{d}_t^\\dagger \\bar{d}_u^\\dagger H"]\[DirectedEdge]{maTeX["L_r \\partial \\bar{u}^\dagger_x \\bar{d}_t^\\dagger \\bar{d}_u^\\dagger H"],maTeX["\\partial \\bar{d}^\\dagger_u H"]:>maTeX[" Q_y"]};*)
(*edgeList[[8]]=Nothing;*)
(*edgeList[[9]]={maTeX["L_r \\partial \\bar{u}^\dagger_x \\bar{d}_t^\\dagger \\bar{d}_u^\\dagger H"],maTeX["\\partial \\bar{d}^\\dagger_u H"]:>maTeX[" Q_y"]}\[DirectedEdge]maTeX["L_r Q_y \\bar{u}^\dagger_x \\bar{d}_u^\\dagger"];*)
(*edgeList[[10]]=Nothing;*)
(*edgeList[[11]]=maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"]\[DirectedEdge]{maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"],maTeX["\\partial Q_s H"]:>maTeX["\\bar{u}^\\dagger_y"]};*)
(*edgeList[[12]]=maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"]\[DirectedEdge]{maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"],maTeX["\\partial Q_x H"]:>maTeX["\\bar{u}^\\dagger_z"]};*)
(*edgeList[[13]]=maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"]\[DirectedEdge]{maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"],maTeX["\\partial \\bar{d}^\\dagger_u H"]:>maTeX[" Q_w"]};*)
(*edgeList[[14]]={maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"],maTeX["\\partial Q_s H"]:>maTeX["\\bar{u}^\\dagger_y"]}\[DirectedEdge]maTeX["L_r Q_x \\bar{u}^\dagger_y \\bar{d}_u^\\dagger"];*)
(*edgeList[[15]]={maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"],maTeX["\\partial Q_x H"]:>maTeX["\\bar{u}^\\dagger_z"]}\[DirectedEdge]maTeX["L_r Q_s \\bar{u}^\\dagger_z \\bar{d}_u^\\dagger"];*)
(*edgeList[[16]]={maTeX["L_r Q_s \\partial Q_x \\bar{d}_u^\\dagger H"],maTeX["\\partial \\bar{d}^\\dagger_u H"]:>maTeX[" Q_w"]}\[DirectedEdge]maTeX["L_r Q_s Q_x Q_w"];*)
(*edgeList[[17]]=Nothing;*)
(*edgeList[[18]]=Nothing;*)
(*edgeList[[19]]=Nothing;*)
(*edgeList[[20]]=Nothing;*)
(*edgeList[[21]]=Nothing;*)
(*edgeList[[22]]=Nothing;*)
(*MultiwayGraph[{1,1,edgeList}]*)
(*]*)


(* ::Input:: *)
(*texmag=0.8;*)
(*GetWeights["16",0]:=MaTeX["C_{16}^{rstu}",Magnification->texmag];*)
(*GetWeights["16",1]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_u]_{xs}^*",Magnification->texmag];*)
(*GetWeights["16",2]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_d]_{tx}",Magnification->texmag];*)
(*GetWeights["16",3]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_d]_{uy}",Magnification->texmag];*)
(*GetWeights["16",4]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_u]_{ys}^*",Magnification->texmag];*)
(*GetWeights["16",5]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_u]_{zx}^*",Magnification->texmag];*)
(*GetWeights["16",6]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_d]_{uw}",Magnification->texmag];*)


(* ::Input:: *)
(*Select[VertexList[o16MultiwayGraph],Length[#]==2&]*)


(* ::Input:: *)
(*Select[VertexList[o16MultiwayGraph],Length[#]==1&]*)


(* ::Input:: *)
(*texmagLeaf=0.9;*)
(*extendedO16MultiwayGraph=Block[{extendedEdgeList},*)
(*extendedEdgeList=Join[EdgeList[o16MultiwayGraph],*)
(*{*)
(*maTeX["L_r Q_x \\bar{u}^\\dagger_y \\bar{d}_u^\\dagger"]\[DirectedEdge]maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_u]_{xs}^* [\\mathbf{y}_d]_{uy} C_{16}^{rstu} [\\mathcal{O}_{duql}]_{uxyr}",Magnification->texmagLeaf],*)
(**)
(*maTeX["L_r Q_y \\bar{u}^\\dagger_x \\bar{d}_u^\\dagger"]\[DirectedEdge]maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_u]_{xs}^* [\\mathbf{y}_d]_{uy} C_{16}^{rstu} [\\mathcal{O}_{duql}]_{uxyr}",Magnification->texmagLeaf],*)
(**)
(*maTeX["L_r Q_s \\bar{u}^\\dagger_z \\bar{d}_u^\\dagger"]\[DirectedEdge]maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_u]_{zx}^* [\\mathbf{y}_d]_{tx} C_{16}^{rstu} [\\mathcal{O}_{duql}]_{uzsr}",Magnification->texmagLeaf],*)
(**)
(*maTeX["L_r Q_s Q_x Q_w"]\[DirectedEdge]maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_d]_{uw} [\\mathbf{y}_d]_{tx} C_{16}^{rstu} [\\mathcal{O}_{qqql}]_{sxwr}",Magnification->texmagLeaf]*)
(*}*)
(*];*)
(*MultiwayGraph[{1,1,extendedEdgeList}]*)
(*]*)


(* ::Input:: *)
(*vertices=MapThread[Rule,{VertexList[extendedO16MultiwayGraph],GraphEmbedding[Graph[extendedO16MultiwayGraph,GraphLayout->"LayeredDigraphEmbedding"]]}];*)


(* ::Input:: *)
(*vertices*)


(* ::Input:: *)
(*vertices[[-2]]=maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_u]_{zx}^* [\\mathbf{y}_d]_{tx} C_{16}^{rstu} [\\mathcal{O}_{duql}]_{uzsr}",Magnification->texmagLeaf]->{0,-0.5};*)
(*vertices[[-1]]=maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_d]_{uw} [\\mathbf{y}_d]_{tx} C_{16}^{rstu} [\\mathcal{O}_{qqql}]_{sxwr}",Magnification->texmagLeaf]->{1,-1};*)


(* ::Input:: *)
(*annotatedGraphO16=Block[{graph=extendedO16MultiwayGraph},*)
(*Graph[graph,*)
(*GraphLayout->"LayeredDigraphEmbedding",*)
(*VertexCoordinates->vertices,*)
(*VertexLabels->Join[*)
(*{*)
(*First[VertexList[graph]]->Placed[Framed[GetWeights["16",0],Background->White],Above],*)
(*maTeX["L_r Q_x \\bar{u}^\\dagger_y \\bar{d}_u^\\dagger"]->Placed[Framed[MaTeX["x \\leftrightarrow y",Magnification->texmag],Background->White],Below]*)
(*},*)
(*MapIndexed[#1->Placed[Framed[GetWeights["16",First[#2]],Background->White],Below]&,Select[VertexList[graph],Length[#]==2&&Head[#]===List&]]*)
(*]*)
(*]*)
(*]*)


(* ::Input:: *)
(*(*Load other PDFs you want to combine*)*)
(*op16t0=Import["/Users/johngargalionis/Projects/bviolation/bviolation-paper/tikz/o16_0.pdf", "PDF"][[1]];*)
(*op16t1=Import["/Users/johngargalionis/Projects/bviolation/bviolation-paper/tikz/o16_1.pdf","PDF"][[1]];*)
(*op16t2=Import["/Users/johngargalionis/Projects/bviolation/bviolation-paper/tikz/o16_2.pdf", "PDF"][[1]];*)


(* ::Input:: *)
(*(*Define positions for pdf1 and pdf2 within the main graph*)*)
(*positionPdf1={Scaled[{0.3,0.93}],Center};*)
(*positionPdf2={Scaled[{0.,0.78}],Center};*)
(*positionPdf3={Scaled[{0.,0.46}],Center};*)


(* ::Input:: *)
(*combinedGraphicsO16=Graphics[*)
(*{*)
(*Inset[annotatedGraphO16,Scaled[{0.5,0.5}],Center,ImageScaled[1]],*)
(*Inset[op16t0,positionPdf1[[1]],positionPdf1[[2]], Scaled[{0.14,0.14}]],*)
(*Inset[op16t1,positionPdf2[[1]],positionPdf2[[2]],Scaled[{0.18,0.18}]],*)
(*Inset[op16t2,positionPdf3[[1]],positionPdf3[[2]],Scaled[{0.21,0.21}]]*)
(*},*)
(*ImageSize->1000,*)
(*PlotRangePadding->{{Automatic,Automatic},{Automatic,Automatic}}*)
(*]*)


(* ::Input:: *)
(*Export["/Users/johngargalionis/Desktop/op16_matching_tree.pdf",combinedGraphicsO16,"PDF","AllowRasterization"->False]*)


(* ::Section:: *)
(*O49 example*)


(* ::Input:: *)
(**)


(* ::Input:: *)
(*MultiwayGraph@MatchOperator[BViolatingOperatorsDim9["49"],$MatchingRulesDim9,2]*)


(* ::Input:: *)
(*o49MultiwayGraph=Block[{edgeList},*)
(*edgeList=EdgeList@MultiwayGraph@MatchOperator[BViolatingOperatorsDim9["49"],$MatchingRulesDim9,4];*)
(*Print[edgeList[[6]]];*)
(*edgeList[[1]]=maTeX["L_{r} \\bar{e}_{s} \\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"]\[DirectedEdge]{maTeX["L_{r} \\bar{e}_{s} \\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"],maTeX["L_r \\bar{e}_s"]:>maTeX[" H"]};*)
(*edgeList[[2]]=maTeX["L_{r} \\bar{e}_{s} \\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"]\[DirectedEdge]{maTeX["L_{r} \\bar{e}_{s} \\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"],maTeX["\\bar{e}_{t}^{\\dagger} \\bar{e}_{s}"]:>maTeX["\\partial"]};*)
(*edgeList[[3]]={maTeX["L_{r} \\bar{e}_{s} \\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"],maTeX["L_r \\bar{e}_s"]:>maTeX[" H"]}\[DirectedEdge]maTeX["\\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} H"];*)
(*edgeList[[4]]={maTeX["L_{r} \\bar{e}_{s} \\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"],maTeX["\\bar{e}_{t}^{\\dagger} \\bar{e}_{s}"]:>maTeX["\\partial"]}\[DirectedEdge]maTeX["\\partial L_{r} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"];*)
(*edgeList[[5]]=maTeX["\\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} H"]\[DirectedEdge]{maTeX["\\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} H"],maTeX["Q_{u}^{\\dagger} H"]:>maTeX["\\partial \\bar{d}_{x}"]};*)
(*edgeList[[6]]=maTeX["\\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} H"]\[DirectedEdge]{maTeX["\\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} H"],maTeX["\\bar{e}_{t}^{\\dagger} H"]:>maTeX["\\partial L_{x}"]};*)
(*edgeList[[7]]={maTeX["\\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} H"],maTeX["Q_{u}^{\\dagger} H"]:>maTeX["\\partial \\bar{d}_{x}"]}\[DirectedEdge]maTeX["\\bar{e}_{t}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} \\partial \\bar{d}_{x}"];*)
(*edgeList[[8]]={maTeX["\\bar{e}_{t}^{\\dagger} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} H"],maTeX["\\bar{e}_{t}^{\\dagger} H"]:>maTeX["\\partial L_{x}"]}\[DirectedEdge]maTeX["\\partial L_{x} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"];*)
(*edgeList[[9]]=Nothing;*)
(*edgeList[[10]]=Nothing;*)
(*MultiwayGraph[{1,1,edgeList}]*)
(*]*)


(* ::Input:: *)
(*texmag=0.8;*)
(*GetWeights["49",0]:=MaTeX["C_{49}^{rstuvw}",Magnification->texmag];*)
(*GetWeights["49",2]:=MaTeX["\\frac{1}{16\\pi^2} \\delta_{ts}",Magnification->texmag];*)
(*GetWeights["49",1]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_e]_{sr}^*",Magnification->texmag];*)
(*GetWeights["49",3]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_d]_{xu}",Magnification->texmag];*)
(*GetWeights["49",4]:=MaTeX["\\frac{1}{16\\pi^2} [\\mathbf{y}_e]_{tx}",Magnification->texmag];*)


(* ::Input:: *)
(*Select[VertexList[o49MultiwayGraph],Length[#]==1&]*)


(* ::Input:: *)
(*o49MultiwayGraph*)


(* ::Input:: *)
(*texmagLeaf=0.9;*)
(*extendedO49MultiwayGraph=Block[{extendedEdgeList},*)
(*extendedEdgeList=Join[EdgeList[o49MultiwayGraph],*)
(*{*)
(*maTeX["\\partial L_{x} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"]\[DirectedEdge]maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_e]_{sr}^* [\\mathbf{y}_e]_{tx} C_{49}^{rstuvw} [\\mathcal{O}_{\\bar{l}qdDd}]^*_{xuvw}",Magnification->texmagLeaf],*)
(**)
(*maTeX["\\partial L_{r} Q_{u}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w}"]\[DirectedEdge]maTeX["\\frac{1}{16\\pi^2} C_{49}^{rstuvw} \\delta_{ts} [\\mathcal{O}_{\\bar{l}qdDd}]^*_{ruvw}",Magnification->texmagLeaf],*)
(**)
(*maTeX["\\bar{e}_{t}^{\\dagger} \\bar{d}_{v} \\bar{d}_{w} \\partial \\bar{d}_{x}"]\[DirectedEdge]maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_e]_{sr}^* [\\mathbf{y}_d]_{xu} C_{49}^{rstuvw} [\\mathcal{O}_{\\bar{e}dddD}]^*_{tvwx}",Magnification->texmagLeaf]*)
(*}*)
(*];*)
(*MultiwayGraph[{1,1,extendedEdgeList}]*)
(*]*)


(* ::Input:: *)
(*vertices=MapThread[Rule,{VertexList[extendedO49MultiwayGraph],GraphEmbedding[Graph[extendedO49MultiwayGraph,GraphLayout->"LayeredDigraphEmbedding"]]}];*)


(* ::Input:: *)
(*Select[VertexList[extendedO49MultiwayGraph],Length[#]==2&&Head[#]===List&]*)


(* ::Input:: *)
(*vertices*)


(* ::Input:: *)
(*vertices[[-1]]=maTeX["\\left(\\frac{1}{16\\pi^2}\\right)^2 [\\mathbf{y}_e]_{sr}^* [\\mathbf{y}_d]_{xu} C_{49}^{rstuvw} [\\mathcal{O}_{\\bar{e}dddD}]^*_{tvwx}",Magnification->0.9`]->{0.`,-0.5};*)


(* ::Input:: *)
(*annotatedGraphO49=Block[{graph=extendedO49MultiwayGraph},*)
(*Graph[graph,*)
(*GraphLayout->"LayeredDigraphEmbedding",*)
(*VertexCoordinates->vertices,*)
(*VertexLabels->Join[*)
(*{First[VertexList[graph]]->Placed[Framed[GetWeights["49",0],Background->White],Above]},*)
(*MapIndexed[#1->Placed[Framed[GetWeights["49",First[#2]],Background->White],Below]&,Select[VertexList[graph],Length[#]==2&&Head[#]===List&]]*)
(*]*)
(*]*)
(*]*)


(* ::Input:: *)
(*(*Load other PDFs you want to combine*)*)
(*op49t0=Import["/Users/johngargalionis/Projects/bviolation/bviolation-paper/tikz/o49_0.pdf", "PDF"][[1]];*)
(*op49t1=Import["/Users/johngargalionis/Projects/bviolation/bviolation-paper/tikz/o49_1.pdf","PDF"][[1]];*)


(* ::Input:: *)
(*(*Define positions for pdf1 and pdf2 within the main graph*)*)
(*positionPdf1={Scaled[{0.5,0.93}],Center};*)
(*positionPdf2={Scaled[{0.66,0.78}],Center};*)


(* ::Input:: *)
(*combinedGraphicsO49=Graphics[*)
(*{*)
(*Inset[annotatedGraphO49,Scaled[{0.3,0.5}],Center,ImageScaled[1]],*)
(*Inset[op49t0,positionPdf1[[1]],positionPdf1[[2]], Scaled[{0.14,0.14}]],*)
(*Inset[op49t1,positionPdf2[[1]],positionPdf2[[2]],Scaled[{0.18,0.18}]]*)
(*},*)
(*ImageSize->1000,*)
(*PlotRangePadding->{{Automatic,Automatic},{Automatic,Automatic}}*)
(*]*)


(* ::Input:: *)
(*Export["/Users/johngargalionis/Desktop/op49_matching_tree.pdf",combinedGraphicsO49,"PDF","AllowRasterization"->False]*)
