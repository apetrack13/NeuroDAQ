
/*//////////////////////////////////////////////////////////////////                
////////////////////////////////////////////////////////////////////                                                                                                           


*/////////////////////////// - Info - //////////////////////////////

// All coordinates are starting as integrated circuit pins.
// From the top view :

//   CoordD           <---       CoordC
//                                 ^
//                                 ^
//                                 ^
//   CoordA           --->       CoordB


////////////////////////////////////////////////////////////////////


////////// -  Box parameters - /////////////

/* [Box dimensions] */
// - Length  
  Length        = 254;       
// - Width
  Width         = 200;                     
// - Height  
  Height        = 100;  
// - Wall thickness  
  Thick         = 2;//[2:5]  
  
/* [Box options] */
// - Filet diameter  
  Filet         = 2;//[0.1:12] 
// - Filet smoothness  
  Resolution    = 50;//[1:100] 
// - Tolerance (Panel/rails gap)
  m             = 0.9;
// - PCB feet (x4) 
  PCBFeet       = 1;// [0:No, 1:Yes]
// - PCB2 feet (x4) 
  PCB2Feet       = 1;// [0:No, 1:Yes] 
// - PCB3 feet (x4) 
  PCB3Feet       = 1;// [0:No, 1:Yes] 
// - PCB4 feet (x4) 
  PCB4Feet       = 1;// [0:No, 1:Yes] 
// - PCB5 feet (x4) 
  PCB5Feet       = 0;// [0:No, 1:Yes]
// - PCB6 feet (x4)
  PCB6Feet       = 1;// [0:No, 1:Yes]  
// - Ventilation Holes
  Vent          = 1;// [0:No, 1:Yes]
// - Holes width (in mm)
  Vent_width    = 1.5;   


  
/* [PCB_Feet - Raspberry Pi] */
//All dimensions are from the center foot axis

// - Low left corner X position
PCBPosX         = 180;
// - Low left corner Y position
PCBPosY         = 84;
// - PCB Length
PCBLength       = 49;
// - PCB Width
PCBWidth        = 58;
// - Feet height
FootHeight      = 10;
// - Foot diameter
FootDia         = 8;
// - Hole diameter
FootHole        = 3;  


/* [PCB2_Feet - Purple PCB] */
//All dimensions are from the center foot axis

// - Low left corner X position
PCB2PosX         = 7;
// - Low left corner Y position
PCB2PosY         = 116;
// - PCB2 Length
PCB2Length       = 63;
// - PCB Width
PCB2Width        = 54;
// - Feet height
Foot2Height      = 10;
// - Foot diameter
Foot2Dia         = 8;
// - Hole diameter
Foot2Hole       = 3; 


/* [PCB3_Feet - Green PCB 1 - Connected to Green PCB 2] */
//All dimensions are from the center foot axis

// - Low left corner X position
PCB3PosX         = 120;
// - Low left corner Y position
PCB3PosY         = 116;
// - PCB2 Length
PCB3Length       = 35;
// - PCB Width
PCB3Width        = 55;
// - Feet height
Foot3Height      = 10;
// - Foot diameter
Foot3Dia         = 8;
// - Hole diameter
Foot3Hole       = 3;

/* [PCB4_Feet - Green PCB 2 - Connected to Green PCB 1] */
//All dimensions are from the center foot axis

// - Low left corner X position
PCB4PosX         = 120;
// - Low left corner Y position
PCB4PosY         = 10;
// - PCB2 Length
PCB4Length       = 35;
// - PCB Width
PCB4Width        = 55;
// - Feet height
Foot4Height      = 10;
// - Foot diameter
Foot4Dia         = 8;
// - Hole diameter
Foot4Hole       = 3;

/* [PCB5_Feet - Green PCB 3] */
//All dimensions are from the center foot axis

// - Low left corner X position
PCB5PosX         = 60;
// - Low left corner Y position
PCB5PosY         = 10;
// - PCB2 Length
PCB5Length       = 35;
// - PCB Width
PCB5Width        = 55;
// - Feet height
Foot5Height      = 10;
// - Foot diameter
Foot5Dia         = 8;
// - Hole diameter
Foot5Hole       = 3;

/* [PCB6_Feet - Green PCB 1 - Connected to Green PCB 2] */
//All dimensions are from the center foot axis

// - Low left corner X position
PCB6PosX         = 5;
// - Low left corner Y position
PCB6PosY         = 10;
// - PCB2 Length
PCB6Length       = 35;
// - PCB Width
PCB6Width        = 55;
// - Feet height
Foot6Height      = 10;
// - Foot diameter
Foot6Dia         = 8;
// - Hole diameter
Foot6Hole       = 3;
  

/* [STL element to export] */
// - Top shell
TShell          = 0;// [0:No, 1:Yes]
// - Bottom shell
BShell          = 1;// [0:No, 1:Yes]
// - Front panel
FPanL           = 1;// [0:No, 1:Yes]
// - Back panel  
BPanL           = 1;// [0:No, 1:Yes]


  
/* [Hidden] */
// - Shell color  
Couleur1        = "Orange";       
// - Panels color    
Couleur2        = "OrangeRed";    
// Thick X 2 - make thicker; if it is a vent, want to make sure they go through shell
Dec_Thick       = Vent ? Thick*2 : Thick; 
// - Depth 
Dec_size        = Vent ? Thick*2 : 0.8;





/////////// - Generic rounded box - //////////

module RoundBox($a=Length, $b=Width, $c=Height){// Cube bords arrondis
                    $fn=Resolution;            
                    translate([0,Filet,Filet]){  
                    minkowski (){                                              
                        cube ([$a-(Length/2),$b-(2*Filet),$c-(2*Filet)], center = false);
                        rotate([0,90,0]){    
                        cylinder(r=Filet,h=Length/2, center = false);
                            } 
                        }
                    }
                }// End of RoundBox Module

      
////////////////////////////////// - Module Shell - //////////////////////////////////         

module Coque(){//Shell  
    Thick = Thick*2;  
    difference(){    
        difference(){//sides decoration
            union(){    
                     difference() {//Substraction Fileted box
                      
                        difference(){//Median cube slicer
                            union() {//union               
                            difference(){//Coque    
                                RoundBox();
                                translate([Thick/2,Thick/2,Thick/2]){     
                                        RoundBox($a=Length-Thick, $b=Width-Thick, $c=Height-Thick);
                                        }
                                        }//Fin diff Coque                            
                                difference(){//larger Rails        
                                     translate([Thick+m,Thick/2,Thick/2]){// Rails
                                          RoundBox($a=Length-((2*Thick)+(2*m)), $b=Width-Thick, $c=Height-(Thick*2));
                                                          }//fin Rails
                                     translate([((Thick+m/2)*1.55),Thick/2,Thick/2+0.1]){ // +0.1 added to avoid the artefact
                                          RoundBox($a=Length-((Thick*3)+2*m), $b=Width-Thick, $c=Height-Thick);
                                                    }           
                                                }//Fin largeur Rails
                                    }//Fin union                                   
                               translate([-Thick,-Thick,Height/2]){// Cube à soustraire
                                    cube ([Length+100, Width+100, Height], center=false);
                                            }                                            
                                      }//End Median cube slicer
                               translate([-Thick/2,Thick,Thick]){ 
                                    RoundBox($a=Length+Thick, $b=Width-Thick*2, $c=Height-Thick);       
                                    }                          
                                }                                          


                difference(){// wall fixation box legs
                    union(){
                        translate([3*Thick +5,Thick,Height/2]){
                            rotate([90,0,0]){
                                    $fn=6;
                                    cylinder(d=16,Thick/2);
                                    }   
                            }
                            
                       translate([Length-((3*Thick)+5),Thick,Height/2]){
                            rotate([90,0,0]){
                                    $fn=6;
                                    cylinder(d=16,Thick/2);
                                    }   
                            }

                        }
                            translate([4,Thick+Filet,Height/2-57]){   
                             rotate([45,0,0]){
                                   cube([Length,40,40]);    
                                  }
                           }
                           translate([0,-(Thick*1.46),Height/2]){
                                cube([Length,Thick*2,10]);
                           }
                    } //Fin fixation box legs
            }

        union(){// outbox sides decorations
            
            for(i=[0:Thick:Length/4]){

                // Ventilation holes ;) 
                    translate([10+i,-Dec_Thick+Dec_size,1]){
                    cube([Vent_width,Dec_Thick,Height/4]);
                    }
                    translate([(Length-10) - i,-Dec_Thick+Dec_size,1]){
                    cube([Vent_width,Dec_Thick,Height/4]);
                    }
                    translate([(Length-10) - i,Width-Dec_size,1]){
                    cube([Vent_width,Dec_Thick,Height/4]);
                    }
                    translate([10+i,Width-Dec_size,1]){
                    cube([Vent_width,Dec_Thick,Height/4]);
                    }
  
                
                    }// fin de for
               // }
                }//fin union decoration
            }//fin difference decoration


            union(){ //sides holes
                $fn=50;
                translate([3*Thick+5,20,Height/2+4]){
                    rotate([90,0,0]){
                    cylinder(d=2,20);
                    }
                }
                translate([Length-((3*Thick)+5),20,Height/2+4]){
                    rotate([90,0,0]){
                    cylinder(d=2,20);
                    }
                }
                translate([3*Thick+5,Width+5,Height/2-4]){
                    rotate([90,0,0]){
                    cylinder(d=2,20);
                    }
                }
                translate([Length-((3*Thick)+5),Width+5,Height/2-4]){
                    rotate([90,0,0]){
                    cylinder(d=2,20);
                    }
                }
            }//fin sides holes

        }//fin difference holes
}// fin shell 

////////////////////////////// ///////////////////////////////////////////





/////////////////////// - Foot with base filet - /////////////////////////////
module foot(FootDia,FootHole,FootHeight){
    Filet=2;
    color(Couleur1)   
    translate([0,0,Filet-1.5])
    difference(){
    
    difference(){
            //translate ([0,0,-Thick]){
                cylinder(d=FootDia+Filet,FootHeight-Thick, $fn=100);
                        //}
                    rotate_extrude($fn=100){
                            translate([(FootDia+Filet*2)/2,Filet,0]){
                                    minkowski(){
                                            square(10);
                                            circle(Filet, $fn=100);
                                        }
                                 }
                           }
                   }
            cylinder(d=FootHole,FootHeight+1, $fn=100);
               }          
}// Fin module foot
  
module Feet(){     
//////////////////// - PCB only visible in the preview mode - /////////////////////    
    translate([3*Thick+2,Thick+5,FootHeight+(Thick/2)-0.5]){
    
    %square ([PCBLength+10,PCBWidth+10]);
       translate([PCBLength/2,PCBWidth/2,0.5]){ 
        color("Olive")
        %text("PCB", halign="center", valign="center", font="Arial black");
       }
    } // Fin PCB 
  
    
////////////////////////////// - 4 Feet - //////////////////////////////////////////     
    translate([3*Thick+7,Thick+10,Thick/2]){
        foot(FootDia,FootHole,FootHeight);
    }
    translate([(3*Thick)+PCBLength+7,Thick+10,Thick/2]){
        foot(FootDia,FootHole,FootHeight);
        }
    translate([(3*Thick)+PCBLength+7,(Thick)+PCBWidth+10,Thick/2]){
        foot(FootDia,FootHole,FootHeight);
        }        
    translate([3*Thick+7,(Thick)+PCBWidth+10,Thick/2]){
        foot(FootDia,FootHole,FootHeight);
    }   

} // Fin module Feet
 


 
/////////////////////// - Foot2 with base filet - /////////////////////////////
module foot2(Foot2Dia,Foot2Hole,Foot2Height){
    Filet=2;
    color(Couleur1)   
    translate([0,0,Filet-1.5])
    difference(){
    
    difference(){
            //translate ([0,0,-Thick]){
                cylinder(d=Foot2Dia+Filet,Foot2Height-Thick, $fn=100);
                        //}
                    rotate_extrude($fn=100){
                            translate([(Foot2Dia+Filet*2)/2,Filet,0]){
                                    minkowski(){
                                            square(10);
                                            circle(Filet, $fn=100);
                                        }
                                 }
                           }
                   }
            cylinder(d=Foot2Hole,Foot2Height+1, $fn=100);
               }          
}// Fin module foot2

module Feet2(){     
//////////////////// - PCB2 only visible in the preview mode - /////////////////////    
    translate([3*Thick+2,Thick+5,Foot2Height+(Thick/2)-0.5]){
    
    %square ([PCB2Length+10,PCB2Width+10]);
       translate([PCB2Length/2,PCB2Width/2,0.5]){ 
        color("Olive")
        %text("PCB", halign="center", valign="center", font="Arial black");
       }
    } // Fin PCB2
  
    
////////////////////////////// - 4 Feet - //////////////////////////////////////////     
    translate([3*Thick+7,Thick+10,Thick/2]){
        foot(Foot2Dia,Foot2Hole,Foot2Height);
    }
    translate([(3*Thick)+PCB2Length+7,Thick+10,Thick/2]){
        foot(Foot2Dia,Foot2Hole,Foot2Height);
        }
    translate([(3*Thick)+PCB2Length+7,(Thick)+PCB2Width+10,Thick/2]){
        foot(Foot2Dia,Foot2Hole,Foot2Height);
        }        
    translate([3*Thick+7,(Thick)+PCB2Width+10,Thick/2]){
        foot(Foot2Dia,Foot2Hole,Foot2Height);
    }   

} // Fin module Feet2

/////////////////////// - Foot3 with base filet - /////////////////////////////
module foot3(Foot3Dia,Foot3Hole,Foot3Height){
    Filet=2;
    color(Couleur1)   
    translate([0,0,Filet-1.5])
    difference(){
    
    difference(){
            //translate ([0,0,-Thick]){
                cylinder(d=Foot3Dia+Filet,Foot3Height-Thick, $fn=100);
                        //}
                    rotate_extrude($fn=100){
                            translate([(Foot3Dia+Filet*2)/2,Filet,0]){
                                    minkowski(){
                                            square(10);
                                            circle(Filet, $fn=100);
                                        }
                                 }
                           }
                   }
            cylinder(d=Foot3Hole,Foot3Height+1, $fn=100);
               }          
}// Fin module foot3

module Feet3(){     
//////////////////// - PCB3 only visible in the preview mode - /////////////////////    
    translate([3*Thick+2,Thick+5,Foot3Height+(Thick/2)-0.5]){
    
    %square ([PCB3Length+10,PCB3Width+10]);
       translate([PCB3Length/2,PCB3Width/2,0.5]){ 
        color("Olive")
        %text("PCB", halign="center", valign="center", font="Arial black");
       }
    } // Fin PCB3
  
    
////////////////////////////// - 4 Feet - //////////////////////////////////////////     
    translate([3*Thick+7,Thick+10,Thick/2]){
        foot(Foot3Dia,Foot3Hole,Foot3Height);
    }
    translate([(3*Thick)+PCB3Length+7,Thick+10,Thick/2]){
        foot(Foot3Dia,Foot3Hole,Foot3Height);
        }
    translate([(3*Thick)+PCB3Length+7,(Thick)+PCB3Width+10,Thick/2]){
        foot(Foot3Dia,Foot3Hole,Foot3Height);
        }        
    translate([3*Thick+7,(Thick)+PCB3Width+10,Thick/2]){
        foot(Foot3Dia,Foot3Hole,Foot3Height);
    }   

} // Fin module Feet3


/////////////////////// - Foot4 with base filet - /////////////////////////////
module foot4(Foot4Dia,Foot4Hole,Foot4Height){
    Filet=2;
    color(Couleur1)   
    translate([0,0,Filet-1.5])
    difference(){
    
    difference(){
            //translate ([0,0,-Thick]){
                cylinder(d=Foot4Dia+Filet,Foot4Height-Thick, $fn=100);
                        //}
                    rotate_extrude($fn=100){
                            translate([(Foot4Dia+Filet*2)/2,Filet,0]){
                                    minkowski(){
                                            square(10);
                                            circle(Filet, $fn=100);
                                        }
                                 }
                           }
                   }
            cylinder(d=Foot4Hole,Foot4Height+1, $fn=100);
               }          
}// Fin module foot4

module Feet4(){     
//////////////////// - PCB4 only visible in the preview mode - /////////////////////    
    translate([3*Thick+2,Thick+5,Foot4Height+(Thick/2)-0.5]){
    
    %square ([PCB4Length+10,PCB4Width+10]);
       translate([PCB4Length/2,PCB4Width/2,0.5]){ 
        color("Olive")
        %text("PCB", halign="center", valign="center", font="Arial black");
       }
    } // Fin PCB4
  
    
////////////////////////////// - 4 Feet - //////////////////////////////////////////     
    translate([3*Thick+7,Thick+10,Thick/2]){
        foot(Foot4Dia,Foot4Hole,Foot4Height);
    }
    translate([(3*Thick)+PCB4Length+7,Thick+10,Thick/2]){
        foot(Foot4Dia,Foot4Hole,Foot4Height);
        }
    translate([(3*Thick)+PCB4Length+7,(Thick)+PCB4Width+10,Thick/2]){
        foot(Foot4Dia,Foot4Hole,Foot4Height);
        }        
    translate([3*Thick+7,(Thick)+PCB4Width+10,Thick/2]){
        foot(Foot4Dia,Foot4Hole,Foot4Height);
    }   

} // Fin module Feet4


/////////////////////// - Foot5 with base filet - /////////////////////////////
module foot5(Foot5Dia,Foot5Hole,Foot5Height){
    Filet=2;
    color(Couleur1)   
    translate([0,0,Filet-1.5])
    difference(){
    
    difference(){
            //translate ([0,0,-Thick]){
                cylinder(d=Foot5Dia+Filet,Foot3Height-Thick, $fn=100);
                        //}
                    rotate_extrude($fn=100){
                            translate([(Foot5Dia+Filet*2)/2,Filet,0]){
                                    minkowski(){
                                            square(10);
                                            circle(Filet, $fn=100);
                                        }
                                 }
                           }
                   }
            cylinder(d=Foot5Hole,Foot5Height+1, $fn=100);
               }          
}// Fin module foot5

module Feet5(){     
//////////////////// - PCB5 only visible in the preview mode - /////////////////////    
    translate([3*Thick+2,Thick+5,Foot5Height+(Thick/2)-0.5]){
    
    %square ([PCB5Length+10,PCB5Width+10]);
       translate([PCB3Length/2,PCB3Width/2,0.5]){ 
        color("Olive")
        %text("PCB", halign="center", valign="center", font="Arial black");
       }
    } // Fin PCB3
  
    
////////////////////////////// - 4 Feet - //////////////////////////////////////////     
    translate([3*Thick+7,Thick+10,Thick/2]){
        foot(Foot5Dia,Foot5Hole,Foot5Height);
    }
    translate([(3*Thick)+PCB5Length+7,Thick+10,Thick/2]){
        foot(Foot5Dia,Foot5Hole,Foot5Height);
        }
    translate([(3*Thick)+PCB5Length+7,(Thick)+PCB5Width+10,Thick/2]){
        foot(Foot5Dia,Foot5Hole,Foot5Height);
        }        
    translate([3*Thick+7,(Thick)+PCB5Width+10,Thick/2]){
        foot(Foot5Dia,Foot5Hole,Foot5Height);
    }   

} // Fin module Feet5


/////////////////////// - Foot6 with base filet - /////////////////////////////
module foot6(Foot6Dia,Foot6Hole,Foot6Height){
    Filet=2;
    color(Couleur1)   
    translate([0,0,Filet-1.5])
    difference(){
    
    difference(){
            //translate ([0,0,-Thick]){
                cylinder(d=Foot6Dia+Filet,Foot6Height-Thick, $fn=100);
                        //}
                    rotate_extrude($fn=100){
                            translate([(Foot6Dia+Filet*2)/2,Filet,0]){
                                    minkowski(){
                                            square(10);
                                            circle(Filet, $fn=100);
                                        }
                                 }
                           }
                   }
            cylinder(d=Foot6Hole,Foot6Height+1, $fn=100);
               }          
}// Fin module foot6

module Feet6(){     
//////////////////// - PCB6 only visible in the preview mode - /////////////////////    
    translate([3*Thick+2,Thick+5,Foot6Height+(Thick/2)-0.5]){
    
    %square ([PCB6Length+10,PCB6Width+10]);
       translate([PCB6Length/2,PCB6Width/2,0.5]){ 
        color("Olive")
        %text("PCB", halign="center", valign="center", font="Arial black");
       }
    } // Fin PCB6
  
    
////////////////////////////// - 4 Feet - //////////////////////////////////////////     
    translate([3*Thick+7,Thick+10,Thick/2]){
        foot(Foot6Dia,Foot6Hole,Foot6Height);
    }
    translate([(3*Thick)+PCB6Length+7,Thick+10,Thick/2]){
        foot(Foot6Dia,Foot6Hole,Foot6Height);
        }
    translate([(3*Thick)+PCB6Length+7,(Thick)+PCB6Width+10,Thick/2]){
        foot(Foot6Dia,Foot6Hole,Foot6Height);
        }        
    translate([3*Thick+7,(Thick)+PCB6Width+10,Thick/2]){
        foot(Foot6Dia,Foot6Hole,Foot6Height);
    }   

} // Fin module Feet6


////////////////////////////////////////////////////////////////////////
////////////////////// <- Holes Panel Manager -> ///////////////////////
////////////////////////////////////////////////////////////////////////

//                           <- Panel ->  
module Panel(Length,Width,Thick,Filet){
    scale([0.5,1,1])
    minkowski(){
            cube([Thick,Width-(Thick*2+Filet*2+m),Height-(Thick*2+Filet*2+m)]);
            translate([0,Filet,Filet])
            rotate([0,90,0])
            cylinder(r=Filet,h=Thick, $fn=100);
      }
}



//                          <- Circle hole -> 
// Cx=Cylinder X position | Cy=Cylinder Y position | Cdia= Cylinder dia | Cheight=Cyl height
module CylinderHole(OnOff,Cx,Cy,Cdia){
    if(OnOff==1)
    translate([Cx,Cy,-1])
        cylinder(d=Cdia,10, $fn=50);
}
//                          <- Square hole ->  
// Sx=Square X position | Sy=Square Y position | Sl= Square Length | Sw=Square Width | Filet = Round corner
module SquareHole(OnOff,Sx,Sy,Sl,Sw,Filet){
    if(OnOff==1)
     minkowski(){
        translate([Sx+Filet/2,Sy+Filet/2,-1])
            cube([Sl-Filet,Sw-Filet,10]);
            cylinder(d=Filet,h=10, $fn=100);
       }
}


 
//                      <- Linear text panel -> 
module LText(OnOff,Tx,Ty,Font,Size,Content){
    if(OnOff==1)
    translate([Tx,Ty,Thick+.5])
    linear_extrude(height = 0.5){
    text(Content, size=Size, font=Font);
    }
}
//                     <- Circular text panel->  
module CText(OnOff,Tx,Ty,Font,Size,TxtRadius,Angl,Turn,Content){ 
      if(OnOff==1) {
      Angle = -Angl / len(Content);
      translate([Tx,Ty,Thick+.5])
          for (i= [0:len(Content)-1] ){   
              rotate([0,0,i*Angle+90+Turn])
              translate([0,TxtRadius,0]) {
                linear_extrude(height = 0.5){
                text(Content[i], font = Font, size = Size,  valign ="baseline", halign ="center");
                    }
                }   
             }
      }
}
////////////////////// <- New module Panel -> //////////////////////
module FPanL(){
    difference(){
        color(Couleur2)
        Panel(Length,Width,Thick,Filet);
    
 
    rotate([90,0,90]){
        color(Couleur2){
//                     <- Cutting shapes from here ->  
        SquareHole  (1,140,8,58,17,1); //(On/Off, Xpos,Ypos,Length,Width,Filet)
        SquareHole  (0,40,20,15,10,1);
        SquareHole  (0,60,20,15,10,1); 
        CylinderHole(0,27,40,8);       //(On/Off, Xpos, Ypos, Diameter)
        CylinderHole(0,47,40,8);
        CylinderHole(0,67,40,8);
        SquareHole  (0,20,50,80,30,3);
        CylinderHole(0,93,30,10);
        SquareHole  (0,120,20,30,60,3);
//                            <- To here -> 
           }
       }
}

    color(Couleur1){
        translate ([-.5,0,0])
        rotate([90,0,90]){
//                      <- Adding text from here ->          
        LText(1,15,75,"Arial Black",10,"NeuroDAQ");//(On/Off, Xpos, Ypos, "Font", Size, "Text")
        LText(0,120,83,"Arial Black",4,"Level");
        LText(0,20,11,"Arial Black",6,"  1     2      3");
        CText(0,93,29,"Arial Black",4,10,180,0,"1 . 2 . 3 . 4 . 5 . 6");//(On/Off, Xpos, Ypos, "Font", Size, Diameter, Arc(Deg), Starting Angle(Deg),"Text")
//                            <- To here ->
            }
      }
}


/////////////////////////// <- Main part -> /////////////////////////

if(TShell==1)
// Top Shell
        color( Couleur1,1){
            translate([0,Width,Height+0.2]){
                rotate([0,180,180]){
                        Coque();
                        }
                }
        }

if(BShell==1)
// Bottom shell
        color(Couleur1){ 
        Coque();
        }

// PCB feet
if (PCBFeet==1)
// Feet
        translate([PCBPosX,PCBPosY,0]){ 
        Feet();
        }
// PCB2 feet
if (PCB2Feet==1)
// Feet
        translate([PCB2PosX,PCB2PosY,0]){ 
        Feet2();
        }
        
// PCB3 feet
if (PCB3Feet==1)
// Feet
        translate([PCB3PosX,PCB3PosY,0]){ 
        Feet3();
        }
        
 // PCB4 feet
if (PCB4Feet==1)
// Feet
        translate([PCB4PosX,PCB4PosY,0]){ 
        Feet4();
        }

// PCB5 feet
if (PCB5Feet==1)
// Feet
        translate([PCB5PosX,PCB5PosY,0]){ 
        Feet5();
        }
        
// PCB6 feet
if (PCB6Feet==1)
// Feet
        translate([PCB6PosX,PCB6PosY,0]){ 
        Feet6();
        } 
        
// Front panel  <<<<<< Text and holes only on this one.
//rotate([0,-90,-90]) 
if(FPanL==1)
        translate([Length-(Thick*2+m/2),Thick+m/2,Thick+m/2])
        FPanL();

// Back panel
if(BPanL==1)
        color(Couleur2)
        translate([Thick+m/2,Thick+m/2,Thick+m/2])
        Panel(Length,Width,Thick,Filet);