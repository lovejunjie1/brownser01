//Maya ASCII 2016 scene
//Name: facial_ctrl.ma
//Last modified: Tue, May 30, 2017 04:49:52 PM
//Codeset: 936
requires maya "2016";
requires -nodeType "VRaySettingsNode" "vrayformaya" "3.10.01";
requires -nodeType "aiOptions" -nodeType "aiAOVDriver" -nodeType "aiAOVFilter" "mtoa" "1.2.7.0";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2016.0.0";
requires "xfrog4.0" "1.0";
requires "vrayformaya2008" "1.0";
requires "vrayformaya" "2.20.01";
requires "shapeCorrect2013x64" "v1.20";
requires "rpmaya" "2.0";
requires "maxwell" "2.7.8";
requires "am_metaballs" "3.0";
requires "elastikSolver" "0.990";
requires "TurtleForMaya70" "2.1.0.0";
requires "TurtleForMaya2008" "4.1.0.3";
requires "finalRender" "1.0";
requires "libCausticMap" "2.0";
requires "RenderMan_for_Maya" "1.0";
requires "TurtleForMaya85" "4.1.0.4";
requires "NormalBump2D" "1.0";
requires "TurtleForMaya2009" "5.1.0.2";
requires "AM_Velvet" "3.0";
requires "CorrectiveShape70" "7.0";
requires "xfrog" "1.0";
requires "AM_Glossy_30" "3.0";
requires -nodeType "mentalrayFramebuffer" -nodeType "mentalrayOutputPass" -nodeType "mentalrayRenderPass"
		 -nodeType "mentalrayUserBuffer" -nodeType "mentalraySubdivApprox" -nodeType "mentalrayCurveApprox"
		 -nodeType "mentalraySurfaceApprox" -nodeType "mentalrayDisplaceApprox" -nodeType "mentalrayOptions"
		 -nodeType "mentalrayGlobals" -nodeType "mentalrayItemsList" -nodeType "mentalrayShader"
		 -nodeType "mentalrayUserData" -nodeType "mentalrayText" -nodeType "mentalrayTessellation"
		 -nodeType "mentalrayPhenomenon" -nodeType "mentalrayLightProfile" -nodeType "mentalrayVertexColors"
		 -nodeType "mentalrayIblShape" -nodeType "mapVizShape" -nodeType "mentalrayCCMeshProxy"
		 -nodeType "cylindricalLightLocator" -nodeType "discLightLocator" -nodeType "rectangularLightLocator"
		 -nodeType "sphericalLightLocator" -nodeType "abcimport" -nodeType "mia_physicalsun"
		 -nodeType "mia_physicalsky" -nodeType "mia_material" -nodeType "mia_material_x" -nodeType "mia_roundcorners"
		 -nodeType "mia_exposure_simple" -nodeType "mia_portal_light" -nodeType "mia_light_surface"
		 -nodeType "mia_exposure_photographic" -nodeType "mia_exposure_photographic_rev" -nodeType "mia_lens_bokeh"
		 -nodeType "mia_envblur" -nodeType "mia_ciesky" -nodeType "mia_photometric_light"
		 -nodeType "mib_texture_vector" -nodeType "mib_texture_remap" -nodeType "mib_texture_rotate"
		 -nodeType "mib_bump_basis" -nodeType "mib_bump_map" -nodeType "mib_passthrough_bump_map"
		 -nodeType "mib_bump_map2" -nodeType "mib_lookup_spherical" -nodeType "mib_lookup_cube1"
		 -nodeType "mib_lookup_cube6" -nodeType "mib_lookup_background" -nodeType "mib_lookup_cylindrical"
		 -nodeType "mib_texture_lookup" -nodeType "mib_texture_lookup2" -nodeType "mib_texture_filter_lookup"
		 -nodeType "mib_texture_checkerboard" -nodeType "mib_texture_polkadot" -nodeType "mib_texture_polkasphere"
		 -nodeType "mib_texture_turbulence" -nodeType "mib_texture_wave" -nodeType "mib_reflect"
		 -nodeType "mib_refract" -nodeType "mib_transparency" -nodeType "mib_continue" -nodeType "mib_opacity"
		 -nodeType "mib_twosided" -nodeType "mib_refraction_index" -nodeType "mib_dielectric"
		 -nodeType "mib_ray_marcher" -nodeType "mib_illum_lambert" -nodeType "mib_illum_phong"
		 -nodeType "mib_illum_ward" -nodeType "mib_illum_ward_deriv" -nodeType "mib_illum_blinn"
		 -nodeType "mib_illum_cooktorr" -nodeType "mib_illum_hair" -nodeType "mib_volume"
		 -nodeType "mib_color_alpha" -nodeType "mib_color_average" -nodeType "mib_color_intensity"
		 -nodeType "mib_color_interpolate" -nodeType "mib_color_mix" -nodeType "mib_color_spread"
		 -nodeType "mib_geo_cube" -nodeType "mib_geo_torus" -nodeType "mib_geo_sphere" -nodeType "mib_geo_cone"
		 -nodeType "mib_geo_cylinder" -nodeType "mib_geo_square" -nodeType "mib_geo_instance"
		 -nodeType "mib_geo_instance_mlist" -nodeType "mib_geo_add_uv_texsurf" -nodeType "mib_photon_basic"
		 -nodeType "mib_light_infinite" -nodeType "mib_light_point" -nodeType "mib_light_spot"
		 -nodeType "mib_light_photometric" -nodeType "mib_cie_d" -nodeType "mib_blackbody"
		 -nodeType "mib_shadow_transparency" -nodeType "mib_lens_stencil" -nodeType "mib_lens_clamp"
		 -nodeType "mib_lightmap_write" -nodeType "mib_lightmap_sample" -nodeType "mib_amb_occlusion"
		 -nodeType "mib_fast_occlusion" -nodeType "mib_map_get_scalar" -nodeType "mib_map_get_integer"
		 -nodeType "mib_map_get_vector" -nodeType "mib_map_get_color" -nodeType "mib_map_get_transform"
		 -nodeType "mib_map_get_scalar_array" -nodeType "mib_map_get_integer_array" -nodeType "mib_fg_occlusion"
		 -nodeType "mib_bent_normal_env" -nodeType "mib_glossy_reflection" -nodeType "mib_glossy_refraction"
		 -nodeType "builtin_bsdf_architectural" -nodeType "builtin_bsdf_architectural_comp"
		 -nodeType "builtin_bsdf_carpaint" -nodeType "builtin_bsdf_ashikhmin" -nodeType "builtin_bsdf_lambert"
		 -nodeType "builtin_bsdf_mirror" -nodeType "builtin_bsdf_phong" -nodeType "contour_store_function"
		 -nodeType "contour_store_function_simple" -nodeType "contour_contrast_function_levels"
		 -nodeType "contour_contrast_function_simple" -nodeType "contour_shader_simple" -nodeType "contour_shader_silhouette"
		 -nodeType "contour_shader_maxcolor" -nodeType "contour_shader_curvature" -nodeType "contour_shader_factorcolor"
		 -nodeType "contour_shader_depthfade" -nodeType "contour_shader_framefade" -nodeType "contour_shader_layerthinner"
		 -nodeType "contour_shader_widthfromcolor" -nodeType "contour_shader_widthfromlightdir"
		 -nodeType "contour_shader_widthfromlight" -nodeType "contour_shader_combi" -nodeType "contour_only"
		 -nodeType "contour_composite" -nodeType "contour_ps" -nodeType "mi_metallic_paint"
		 -nodeType "mi_metallic_paint_x" -nodeType "mi_bump_flakes" -nodeType "mi_car_paint_phen"
		 -nodeType "mi_metallic_paint_output_mixer" -nodeType "mi_car_paint_phen_x" -nodeType "physical_lens_dof"
		 -nodeType "physical_light" -nodeType "dgs_material" -nodeType "dgs_material_photon"
		 -nodeType "dielectric_material" -nodeType "dielectric_material_photon" -nodeType "oversampling_lens"
		 -nodeType "path_material" -nodeType "parti_volume" -nodeType "parti_volume_photon"
		 -nodeType "transmat" -nodeType "transmat_photon" -nodeType "mip_rayswitch" -nodeType "mip_rayswitch_advanced"
		 -nodeType "mip_rayswitch_environment" -nodeType "mip_card_opacity" -nodeType "mip_motionblur"
		 -nodeType "mip_motion_vector" -nodeType "mip_matteshadow" -nodeType "mip_cameramap"
		 -nodeType "mip_mirrorball" -nodeType "mip_grayball" -nodeType "mip_gamma_gain" -nodeType "mip_render_subset"
		 -nodeType "mip_matteshadow_mtl" -nodeType "mip_binaryproxy" -nodeType "mip_rayswitch_stage"
		 -nodeType "mip_fgshooter" -nodeType "mib_ptex_lookup" -nodeType "misss_physical"
		 -nodeType "misss_physical_phen" -nodeType "misss_fast_shader" -nodeType "misss_fast_shader_x"
		 -nodeType "misss_fast_shader2" -nodeType "misss_fast_shader2_x" -nodeType "misss_skin_specular"
		 -nodeType "misss_lightmap_write" -nodeType "misss_lambert_gamma" -nodeType "misss_call_shader"
		 -nodeType "misss_set_normal" -nodeType "misss_fast_lmap_maya" -nodeType "misss_fast_simple_maya"
		 -nodeType "misss_fast_skin_maya" -nodeType "misss_fast_skin_phen" -nodeType "misss_fast_skin_phen_d"
		 -nodeType "misss_mia_skin2_phen" -nodeType "misss_mia_skin2_phen_d" -nodeType "misss_lightmap_phen"
		 -nodeType "misss_mia_skin2_surface_phen" -nodeType "surfaceSampler" -nodeType "mib_data_bool"
		 -nodeType "mib_data_int" -nodeType "mib_data_scalar" -nodeType "mib_data_vector"
		 -nodeType "mib_data_color" -nodeType "mib_data_string" -nodeType "mib_data_texture"
		 -nodeType "mib_data_shader" -nodeType "mib_data_bool_array" -nodeType "mib_data_int_array"
		 -nodeType "mib_data_scalar_array" -nodeType "mib_data_vector_array" -nodeType "mib_data_color_array"
		 -nodeType "mib_data_string_array" -nodeType "mib_data_texture_array" -nodeType "mib_data_shader_array"
		 -nodeType "mib_data_get_bool" -nodeType "mib_data_get_int" -nodeType "mib_data_get_scalar"
		 -nodeType "mib_data_get_vector" -nodeType "mib_data_get_color" -nodeType "mib_data_get_string"
		 -nodeType "mib_data_get_texture" -nodeType "mib_data_get_shader" -nodeType "mib_data_get_shader_bool"
		 -nodeType "mib_data_get_shader_int" -nodeType "mib_data_get_shader_scalar" -nodeType "mib_data_get_shader_vector"
		 -nodeType "mib_data_get_shader_color" -nodeType "user_ibl_env" -nodeType "user_ibl_rect"
		 -nodeType "mia_material_x_passes" -nodeType "mi_metallic_paint_x_passes" -nodeType "mi_car_paint_phen_x_passes"
		 -nodeType "misss_fast_shader_x_passes" -dataType "byteArray" "Mayatomr" "2014.0 - 3.11.1.4 ";
requires "3delight_for_maya2012" "6.0.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201603180400-990260";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	rename -uid "4ACA88F7-4F72-0FDB-F5E3-719E7EE37C76";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 8.4214761237181364 35.714401341191881 112.64894094835179 ;
	setAttr ".r" -type "double3" -9.9052664017913461 -350.99999999991803 -5.0315635869442361e-016 ;
	setAttr ".rp" -type "double3" -7.1054273576010019e-015 0 -7.1054273576010019e-015 ;
	setAttr ".rpt" -type "double3" 2.2530202877024184e-014 1.1865862808164495e-014 8.1069287322989339e-014 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "5292932F-4A6D-8EED-B5DC-7990FFC450CF";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999979;
	setAttr ".coi" 87.880971357507875;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 1.6915613983579476 34.09299901855146 34.939372572780741 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "F5EBD181-427A-3410-928E-339C81FCF148";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 3.1765734877187706 106.67629219098546 37.289268485235816 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "94745CBF-4687-D9D5-1A89-119D2CF89810";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 12.764765047634388;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "DD2E6373-406E-40F8-D494-63ACC82237DB";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -3.5306115845936152 40.018917054591824 114.25644786930674 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "DBC10D1E-4A29-77C1-5D76-5586046716AF";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 83.848471598912624;
	setAttr ".ow" 73.44058310999192;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" -0.66166956173399161 33.793309991676885 30.407976270394116 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "DE2113D2-4D6C-C1B5-A61B-03B8F3BADCB4";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 108.19589039259694 32.226523539524443 36.805833453328233 ;
	setAttr ".r" -type "double3" 0 89.999999999999972 0 ;
	setAttr ".rpt" -type "double3" 0 0 2.8398992587956425e-029 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "516770C8-4FD4-E07B-2DF2-42B5A96EEC01";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 103.06340624220566;
	setAttr ".ow" 43.05166939832808;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 5.1324841503912779 21.949848962066767 33.45906544275806 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Face___innerShow";
	rename -uid "07A1B220-4864-8389-8CE5-DE9F411B871C";
createNode transform -n "facial_Gui_Grp" -p "Face___innerShow";
	rename -uid "959916A3-4230-CA6D-AD31-E187FD7E15A1";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0 1.3877787807814457e-017 ;
	setAttr ".rp" -type "double3" -7.8886090522101303e-031 25.732062403737171 14.11865666685439 ;
	setAttr ".sp" -type "double3" -7.8886090522101303e-031 25.732062403737171 14.11865666685439 ;
createNode transform -n "facial_Gui_Gro" -p "facial_Gui_Grp";
	rename -uid "E8F00B89-4E32-AB5C-1E56-0AA54859E6C6";
	setAttr ".rp" -type "double3" -7.8886090522101303e-031 25.732062403737171 14.11865666685439 ;
	setAttr ".sp" -type "double3" -7.8886090522101303e-031 25.732062403737171 14.11865666685439 ;
createNode transform -n "facial__Ctrl_Grp" -p "facial_Gui_Gro";
	rename -uid "C1963E43-414C-DB91-B8BD-229F3D0EA9EF";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -9.8106544971891652e-031 32.001633250217786 17.55864203767813 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.9220454449790349e-031 -6.2695708464806152 -3.4399853708237398 ;
	setAttr ".sp" -type "double3" 1.9220454449790349e-031 -6.2695708464806152 -3.4399853708237398 ;
createNode transform -n "facial__Ctrl_Gro" -p "facial__Ctrl_Grp";
	rename -uid "AF233B57-488F-BCD6-5C88-A5BFFF05A4B9";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.9220454449790482e-031 -6.2695708464806152 -3.4399853708237416 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "facial__Ctrl" -p "facial__Ctrl_Gro";
	rename -uid "B0536780-41E8-B43A-2A07-AC88109FDC02";
	addAttr -ci true -sn "____________" -ln "____________" -min 0 -max 1 -en "Control_Vis:Control_Vis" 
		-at "enum";
	addAttr -ci true -sn "Face_C" -ln "Face_C" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "Defm_C" -ln "Defm_C" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "Sel_C" -ln "Sel_C" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k on ".____________";
	setAttr -cb on ".Face_C" 1;
	setAttr -cb on ".Defm_C";
	setAttr -cb on ".Sel_C";
createNode nurbsCurve -n "facial__Ctrl_Shape" -p "facial__Ctrl";
	rename -uid "6070A9F7-4442-78C4-DCE5-AB9E9214172E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 20 2 no 3
		25 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
		23
		6.1703884664350257 26.676927331461272 -3.0076214161614758
		-0.00107713877482619 27.619508952867363 -3.2664186424547759
		-6.1725427439846534 26.676927331461343 -3.0076214161614945
		-11.739902296627262 23.941448923698527 -2.2565626129374676
		-16.158183853615093 19.68084141532972 -1.0867611013766962
		-18.994895232172382 14.312162754671984 0.3872747960828879
		-19.972359358035668 8.3609366148143334 2.0212561755859149
		-18.994895232172372 2.409710474956654 3.6552375550889553
		-16.158183853615093 -2.9589681857010559 5.1292734525485297
		-11.739902296627262 -7.2195756940698788 6.2990749641093036
		-6.1725427439846552 -9.9550541018326992 7.0501337673333255
		-0.0010771387748356202 -10.897635723238784 7.3089309936266291
		6.1703884664349973 -9.9550541018326992 7.0501337673333255
		11.737748019077593 -7.2195756940698788 6.2990749641093036
		16.156029576065489 -2.9589681857010559 5.1292734525485297
		18.992740954622789 2.4097104749566456 3.6552375550889593
		19.970205080486064 8.3609366148143192 2.021256175585922
		18.9927409546228 14.312162754671965 0.38727479608288962
		16.156029576065489 19.680841415329713 -1.0867611013766945
		11.737748019077618 23.941448923698513 -2.2565626129374605
		6.1703884664350257 26.676927331461272 -3.0076214161614758
		-0.00107713877482619 27.619508952867363 -3.2664186424547759
		-6.1725427439846534 26.676927331461343 -3.0076214161614945
		;
createNode transform -n "Eye_Aim_Grp" -p "facial__Ctrl";
	rename -uid "B2BF9E8D-48F9-56F2-238B-798C96F1166F";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -2.4404914804560736e-006 8.5530394196338975 53.895067183927509 ;
createNode transform -n "Eye_Aim_Gro" -p "Eye_Aim_Grp";
	rename -uid "F764DA1B-48A3-5170-D459-FCABD77B69F8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Eye_Aim_Ctrl" -p "Eye_Aim_Gro";
	rename -uid "A304BC8A-44BA-76DE-A161-F6AE316F1DC7";
	addAttr -ci true -sn "Eyelid_Follow" -ln "Eyelid_Follow" -min 0 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".Eyelid_Follow" 8;
createNode nurbsCurve -n "Eye_Aim_Ctrl_Shape" -p "Eye_Aim_Ctrl";
	rename -uid "43F976C4-4C38-5E2F-2C87-288287938AF2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 109 0 no 3
		110 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109
		110
		0.00026196272460557815 -2.913054782502996 -3.158637575752242e-013
		0.42725571592337463 -2.8805712482892694 -3.158637575752242e-013
		0.84506081747921813 -2.7874983228716896 -3.158637575752242e-013
		1.2460773721335794 -2.6378113360778057 -3.158637575752242e-013
		1.6224578862303365 -2.4338452783513103 -3.158637575752242e-013
		1.9661141454490705 -2.1785575749964439 -3.158637575752242e-013
		2.2695150318638846 -1.8763740473696571 -3.158637575752242e-013
		2.5241527894251465 -1.5321091087569072 -3.158637575752242e-013
		2.7275342398240539 -1.1555050683290167 -3.158637575752242e-013
		2.8781806704085011 -0.75488054447079878 -3.158637575752242e-013
		2.9713842727581263 -0.33699291011576787 -3.158637575752242e-013
		3.0023822165864655 0.09005037005291168 -3.158637575752242e-013
		3.4297886337811816 0.090055864949126901 -3.158637575752242e-013
		2.3831179910794651 0.090055864949126901 -3.158637575752242e-013
		3.0023822165864655 0.09005037005291168 -3.158637575752242e-013
		2.9713877116247578 0.51709432341412342 -3.158637575752242e-013
		2.8781841092751339 0.93498195776915471 -3.158637575752242e-013
		2.7275376786906906 1.3356064816273741 -3.158637575752242e-013
		2.5241631060250436 1.7122105220552648 -3.158637575752242e-013
		2.2695287873304126 2.0564823384012754 -3.158637575752242e-013
		1.9661175843157039 2.3586555494281649 -3.158637575752242e-013
		1.6224578862303365 2.6139398139164003 -3.158637575752242e-013
		1.2460945664667449 2.8179333825759505 -3.158637575752242e-013
		0.84508145067901563 2.9676306859697315 -3.158637575752242e-013
		0.42725571592337463 3.0606348340546563 -3.158637575752242e-013
		0.00026196272460557815 3.0930564686689923 -3.158637575752242e-013
		0.00026196272460557815 3.4592854484656317 -3.158637575752242e-013
		0.00026196272460557815 3.0930564686689923 -3.158637575752242e-013
		-0.42673179047416426 3.0606348340546563 -3.158637575752242e-013
		-0.84455752522980454 2.9676306859697315 -3.158637575752242e-013
		-1.2455706410175322 2.8179333825759505 -3.158637575752242e-013
		-1.6219339607811276 2.6139398139164003 -3.158637575752242e-013
		-1.9655936588664937 2.3586555494281649 -3.158637575752242e-013
		-2.2690048618812031 2.0564823384012754 -3.158637575752242e-013
		-2.5236391805758327 1.7122105220552648 -3.158637575752242e-013
		-2.7270137532414784 1.3356064816273741 -3.158637575752242e-013
		-2.8776601838259221 0.93498195776915471 -3.158637575752242e-013
		-2.9708637861755487 0.51709432341412342 -3.158637575752242e-013
		-3.0018582911372556 0.09005037005291168 -3.158637575752242e-013
		-2.3831408454248777 0.090055864949126901 -3.158637575752242e-013
		-3.4298114881265875 0.090055864949126901 -3.158637575752242e-013
		-3.0018582911372556 0.09005037005291168 -3.158637575752242e-013
		-2.970860347308915 -0.33699291011576787 -3.158637575752242e-013
		-2.8776567449592889 -0.75488054447079878 -3.158637575752242e-013
		-2.7270103143748448 -1.1555050683290167 -3.158637575752242e-013
		-2.523628863975933 -1.5321091087569072 -3.158637575752242e-013
		-2.2689911064146724 -1.8763740473696571 -3.158637575752242e-013
		-1.9655902199998614 -2.1785575749964439 -3.158637575752242e-013
		-1.6219339607811276 -2.4338452783513103 -3.158637575752242e-013
		-1.2455534466843687 -2.6378113360778057 -3.158637575752242e-013
		-0.84453689203000726 -2.7874983228716896 -3.158637575752242e-013
		-0.42673179047416426 -2.8805712482892694 -3.158637575752242e-013
		0.00026196272460557815 -2.913054782502996 -3.158637575752242e-013
		0.00026196272460557815 -3.4671421687179418 -3.158637575752242e-013
		0.00026196272460557815 -1.4527263114046305 -3.158637575752242e-013
		-0.43439014646547952 -1.390231788086185 -3.158637575752242e-013
		-0.83382826133536991 -1.2078136686810155 -3.158637575752242e-013
		-1.1656926468701274 -0.92025220197702495 -3.158637575752242e-013
		-1.4031016826009044 -0.55083883167838366 -3.158637575752242e-013
		-1.5268149097170123 -0.1295051090705924 -3.158637575752242e-013
		-1.5268149097170123 0.30961718285550921 -3.158637575752242e-013
		-1.4031016826009044 0.73094712271000528 -3.158637575752242e-013
		-1.1656926468701274 1.1003639318752796 -3.158637575752242e-013
		-0.83382826133536991 1.3879219597126364 -3.158637575752242e-013
		-0.43439014646547952 1.5703538345843384 -3.158637575752242e-013
		0.00026196272460557815 1.632810530369823 -3.158637575752242e-013
		0.43491407191468956 1.5703538345843384 -3.158637575752242e-013
		0.83435218678458212 1.3879219597126364 -3.158637575752242e-013
		1.1662165723193376 1.1003639318752796 -3.158637575752242e-013
		1.4036256080501142 0.73094712271000528 -3.158637575752242e-013
		1.5273388351662214 0.30961718285550921 -3.158637575752242e-013
		1.5273388351662214 -0.1295051090705924 -3.158637575752242e-013
		1.4036256080501142 -0.55083883167838366 -3.158637575752242e-013
		1.1662165723193376 -0.92025220197702495 -3.158637575752242e-013
		0.83435218678458212 -1.2078136686810155 -3.158637575752242e-013
		0.43491407191468956 -1.390231788086185 -3.158637575752242e-013
		0.00026196272460557815 -1.4527263114046305 -3.158637575752242e-013
		0.00026196272460557815 0.090055864949126901 -3.158637575752242e-013
		1.145040031594361 0.090055864949126901 -3.158637575752242e-013
		0.65602631867247951 0.090055864949126901 -3.158637575752242e-013
		0.65602631867247951 -0.0042464552896905273 -3.158637575752242e-013
		0.60316406079259643 -0.18521234131581693 -3.158637575752242e-013
		0.50077868453330887 -0.34367118911672584 -3.158637575752242e-013
		0.35870534846451502 -0.46762857576376488 -3.158637575752242e-013
		0.1868063782025112 -0.54528850093299452 -3.158637575752242e-013
		0.00026196272460557815 -0.57298513279381802 -3.158637575752242e-013
		-0.18628245275330002 -0.54528850093299452 -3.158637575752242e-013
		-0.35818142301530359 -0.46762857576376488 -3.158637575752242e-013
		-0.50025475908409778 -0.34367118911672584 -3.158637575752242e-013
		-0.60264013534338579 -0.18521234131581693 -3.158637575752242e-013
		-0.65550239322326853 -0.0042464552896905273 -3.158637575752242e-013
		-0.65549895435663574 0.090055864949126901 -3.158637575752242e-013
		-1.1457162706000104 0.090055864949126901 -3.158637575752242e-013
		0.00026196272460557815 0.090055864949126901 -3.158637575752242e-013
		0.00026196272460557815 0.75334789995626972 -3.158637575752242e-013
		-0.18627970165999388 0.72555497982972583 -3.158637575752242e-013
		-0.35810232908274831 0.64774718339528381 -3.158637575752242e-013
		-0.50017566515154277 0.52380699108140993 -3.158637575752242e-013
		-0.60261606327695494 0.36538012474018616 -3.158637575752242e-013
		-0.65549895435663574 0.18441836535401906 -3.158637575752242e-013
		-0.65549895435663574 0.090055864949126901 -3.158637575752242e-013
		0.65602631867247951 0.090055864949126901 -3.158637575752242e-013
		0.65602287980584684 0.18441836535401906 -3.158637575752242e-013
		0.60313998872616559 0.36538012474018616 -3.158637575752242e-013
		0.5006995906007532 0.52380699108140993 -3.158637575752242e-013
		0.35862625453195951 0.64774718339528381 -3.158637575752242e-013
		0.18680362710920506 0.72555497982972583 -3.158637575752242e-013
		0.00026196272460557815 0.75334789995626972 -3.158637575752242e-013
		0.00026196272460557815 1.632810530369823 -3.158637575752242e-013
		0.00026196272460557815 3.4592854484656317 -3.158637575752242e-013
		;
createNode transform -n "C_Jaw_Grp" -p "facial__Ctrl";
	rename -uid "DDF0C5CC-4BDE-D887-1711-07A3AE8843B7";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -1.4012984643248171e-045 -8.7509373418458427 22.152649313795489 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 2.5 2.5 2.5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0.00029848766917562491 2.8483691433883665e-014 ;
	setAttr ".sp" -type "double3" 0 0.0007424273086857891 7.0847383515371116e-014 ;
	setAttr ".spt" -type "double3" 0 -0.00044393963951016419 -4.2363692081487451e-014 ;
createNode transform -n "Jaw_Ctrl_Gro" -p "C_Jaw_Grp";
	rename -uid "9B0E6A74-4D3F-DFD4-3DE4-8AA118121E68";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 2.0708733881863508e-016 -3.9968028886505628e-015 -9.8575239171049998e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 180 179.9999999505751 -179.99999999946905 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0.29016331138981899 -7.8960318052907523e-015 ;
	setAttr ".sp" -type "double3" 0 0.29016331138981899 -7.8960318052907523e-015 ;
createNode transform -n "Jaw_Ctrl" -p "Jaw_Ctrl_Gro";
	rename -uid "795BBD50-4D38-28D7-4A77-169ABFFA933F";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0.00074242730869388321 -7.8960318052907523e-015 ;
	setAttr ".sp" -type "double3" 0 0.00074242730869388321 -7.8960318052907523e-015 ;
	setAttr ".mntl" -type "double3" -2 -2 -2 ;
	setAttr ".mxtl" -type "double3" 2 2 2 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "Jaw_Ctrl_Shape" -p "Jaw_Ctrl";
	rename -uid "63F29FF4-478B-E327-EA83-459504556C84";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.64002096618749427 0.00074242730868635928 -7.9404248778184301e-015
		-0.63029740743187668 0.11188083956296004 -7.9404248778184301e-015
		-0.60142245127200833 0.21964234860805443 -7.9404248778184301e-015
		-0.55427376804608774 0.32075382878785752 -7.9404248778184301e-015
		-0.49028556966010922 0.41213991344119466 -7.9404248778184301e-015
		-0.41139748613250926 0.4910279969687949 -7.9404248778184301e-015
		-0.32001140147917256 0.55501619535477342 -7.9404248778184301e-015
		-0.21889992129936919 0.6021648785806929 -7.9404248778184301e-015
		-0.11113841225427459 0.63103983474056158 -7.9404248778184301e-015
		0 0.64076339349618106 -7.9404248778184301e-015
		0.11113841225427484 0.63103983474056158 -7.9404248778184301e-015
		0.21889992129936911 0.6021648785806929 -7.9404248778184301e-015
		0.32001140147917256 0.55501619535477342 -7.9404248778184301e-015
		0.41139748613250943 0.4910279969687949 -7.9404248778184301e-015
		0.49028556966010933 0.41213991344119466 -7.9404248778184301e-015
		0.55427376804608819 0.32075382878785752 -7.9404248778184301e-015
		0.60142245127200844 0.21964234860805443 -7.9404248778184301e-015
		0.63029740743187668 0.11188083956296004 -7.9404248778184301e-015
		0.64002096618749427 0.00074242730868635928 -7.9404248778184301e-015
		0.63029740743187668 -0.11039598494558972 -7.9404248778184301e-015
		0.60142245127200844 -0.21815749399068329 -7.9404248778184301e-015
		0.55427376804608819 -0.31926897417048616 -7.9404248778184301e-015
		0.49028556966010933 -0.41065505882382403 -7.9404248778184301e-015
		0.41139748613250943 -0.48954314235142382 -7.9404248778184301e-015
		0.32001140147917256 -0.55353134073740184 -7.9404248778184301e-015
		0.21889992129936911 -0.60068002396332265 -7.9404248778184301e-015
		0.11113841225427484 -0.62955498012319266 -7.9404248778184301e-015
		0 -0.63927853887880814 -7.9404248778184301e-015
		-0.11113841225427459 -0.62955498012319266 -7.9404248778184301e-015
		-0.21889992129936919 -0.60068002396332265 -7.9404248778184301e-015
		-0.32001140147917256 -0.55353134073740184 -7.9404248778184301e-015
		-0.41139748613250926 -0.48954314235142382 -7.9404248778184301e-015
		-0.49028556966010922 -0.41065505882382403 -7.9404248778184301e-015
		-0.55427376804608774 -0.31926897417048616 -7.9404248778184301e-015
		-0.60142245127200833 -0.21815749399068329 -7.9404248778184301e-015
		-0.63029740743187668 -0.11039598494558972 -7.9404248778184301e-015
		-0.64002096618749427 0.00074242730868635928 -7.9404248778184301e-015
		0.64002096618749427 0.00074242730868635928 -7.9404248778184301e-015
		;
createNode transform -n "Jaw_loc" -p "Jaw_Ctrl";
	rename -uid "E74219E7-4F29-42E8-54E2-E28BB3A2CE72";
	setAttr -l on ".v" no;
	setAttr ".rp" -type "double3" 0 -2.7890687406556571 -7.8960318052907523e-015 ;
	setAttr ".sp" -type "double3" 0 -2.7890687406556571 -7.8960318052907523e-015 ;
createNode transform -n "Mouth_Stick_loc" -p "Jaw_loc";
	rename -uid "A247B3F3-491D-F1BA-EC29-658C85F4C509";
	setAttr ".t" -type "double3" 0.62028131087213711 -0.302093086960808 0 ;
	setAttr ".rp" -type "double3" -0.62028131087213723 0.59175506016533463 -1.5001459162891754e-014 ;
	setAttr ".sp" -type "double3" -0.62028131087213723 0.59175506016533463 -1.5001459162891754e-014 ;
createNode locator -n "Mouth_Stick_loc_Shape" -p "Mouth_Stick_loc";
	rename -uid "52D0BECC-40CF-88F7-239B-9D9C0C8EE74E";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -0.62028131087213723 0.59175506016533486 -1.5001888620247428e-014 ;
createNode transform -n "Lips_out_Stick_loc" -p "Jaw_loc";
	rename -uid "A8E5FFD6-48C1-8F70-01F7-32A2E3F49A5C";
	setAttr ".rp" -type "double3" 0 0.0016132107635312561 -2.2106886520492756e-014 ;
	setAttr ".sp" -type "double3" 0 0.0016132107635312561 -2.2106886520492756e-014 ;
createNode locator -n "Lips_out_Stick_loc_Shape" -p "Lips_out_Stick_loc";
	rename -uid "1D34727E-4B47-555A-443B-0A8A892CD860";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 0.0016132107635317139 -2.210731597784843e-014 ;
createNode transform -n "Mouth_Stick_Ctrl_Gro" -p "C_Jaw_Grp";
	rename -uid "DC1D34F0-4232-FBBD-7BFC-7C8AE31601E7";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".rp" -type "double3" -0.057569375291654942 0.59175506016532342 7.7368667028565596e-014 ;
	setAttr ".sp" -type "double3" -0.057569375291654845 0.59175506016532342 7.7368667028565609e-014 ;
	setAttr ".spt" -type "double3" -9.7144514654701197e-017 1.2325951644078307e-032 
		-1.1832913578315177e-029 ;
createNode transform -n "Mouth_Stick_Ctrl" -p "Mouth_Stick_Ctrl_Gro";
	rename -uid "7EFE9970-47E7-C6BB-D06B-D0940E8064A9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -0.62028131087213834 0.59175506016532042 6.2995663583193995e-015 ;
	setAttr ".sp" -type "double3" -0.62028131087213834 0.59175506016532042 6.2995663583193995e-015 ;
	setAttr ".mntl" -type "double3" 0 -1 -1 ;
	setAttr ".mtxe" yes;
	setAttr ".xtxe" yes;
createNode nurbsCurve -n "Mouth_Stick_Ctrl_Shape" -p "Mouth_Stick_Ctrl";
	rename -uid "C68CB182-4EB2-93AD-D319-A2813D053D61";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 11;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.73084731449713858 0.70869788479032336 -3.1816771439707718e-015
		-0.72633821924713859 0.70959472922782341 -3.1816771439707718e-015
		-0.5142244024971383 0.70959472922782352 -3.1816771439707718e-015
		-0.50971530724713832 0.70869788479032347 -3.1816771439707718e-015
		-0.50589267524713832 0.70614369579032343 -3.1816771439707718e-015
		-0.50333848624713839 0.70232106379032344 -3.1816771439707718e-015
		-0.50244164180963835 0.69781196854032346 -3.1816771439707718e-015
		-0.50244164180963835 0.48569815179032338 -3.1816771439707718e-015
		-0.50333848624713828 0.48118905654032335 -3.1816771439707718e-015
		-0.50589267524713832 0.47736642454032335 -3.1816771439707718e-015
		-0.50971530724713832 0.47481223554032337 -3.1816771439707718e-015
		-0.5142244024971383 0.47391539110282338 -3.1816771439707718e-015
		-0.72633821924713859 0.47391539110282338 -3.1816771439707718e-015
		-0.73084731449713836 0.47481223554032326 -3.1816771439707718e-015
		-0.73466994649713835 0.4773664245403233 -3.1816771439707718e-015
		-0.7372241354971385 0.48118905654032329 -3.1816771439707718e-015
		-0.73812097993463843 0.48569815179032327 -3.1816771439707718e-015
		-0.73812097993463854 0.69781196854032346 -3.1816771439707718e-015
		-0.7372241354971385 0.70232106379032344 -3.1816771439707718e-015
		-0.73466994649713835 0.70614369579032343 -3.1816771439707718e-015
		-0.73084731449713858 0.70869788479032336 -3.1816771439707718e-015
		;
createNode transform -n "Jaw_Line" -p "Mouth_Stick_Ctrl_Gro";
	rename -uid "AA3D0F9F-49CA-F782-2093-2F9926E4FD6B";
	setAttr -l on -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 -3.5527136788005009e-015 1.7763568394002505e-015 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -74.783372394939988 -45.511279486540765 ;
	setAttr ".sp" -type "double3" 0 -74.783372394939974 -45.511279486540765 ;
	setAttr ".spt" -type "double3" 0 -1.4210854715202007e-014 -7.1054273576010034e-015 ;
createNode nurbsCurve -n "Jaw_Line_Shape" -p "Jaw_Line";
	rename -uid "FED06BD0-4A29-806A-DC63-DD8E9157A00E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 1 0 no 3
		6 0 0 0 1 1 1
		4
		-0.62028131087214045 0.59175506016557644 1.6263379531977762e-013
		-0.20586013079765075 0.59175506016549118 9.8684949101368602e-014
		0.20856104927683899 0.5917550601653917 4.8946957598161589e-014
		0.62298222935132874 0.59175506016530643 -7.8964612626464259e-015
		;
createNode parentConstraint -n "Mouth_Stick_Ctrl_Gro_parentConstraint1" -p "Mouth_Stick_Ctrl_Gro";
	rename -uid "526D6830-4164-52C5-C37A-FCA6BF571217";
	addAttr -ci true -k true -sn "w0" -ln "Mouth_Stick_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 4.8572257327350599e-017 -9.6589403142388619e-015 
		9.3355878583167851e-014 ;
	setAttr ".rst" -type "double3" 0.05756937529165488 -2.3020930869608103 -9.8532293435482643e-016 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "Mouth_Stick_Ctrl_Gro_scaleConstraint1" -p "Mouth_Stick_Ctrl_Gro";
	rename -uid "B1C05754-4CB9-1C4E-76FC-3DA6AE7B22E9";
	addAttr -ci true -k true -sn "w0" -ln "Mouth_Stick_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0.63617896266965934 0.63617896266965934 0.63617896266965934 ;
	setAttr -k on ".w0";
createNode transform -n "Lips_out_Stick_Ctrl_Gro" -p "C_Jaw_Grp";
	rename -uid "4FE4C315-4BA4-E0FC-F387-349AD1BDF613";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.63772931899128837 0.63772931899128837 0.63772931899128837 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0.0016132107635312561 -1.5015404744487334e-014 ;
	setAttr ".sp" -type "double3" 0 0.0016132107635312561 -1.5015404744487334e-014 ;
createNode transform -n "Lips_out_Stick_Ctrl" -p "Lips_out_Stick_Ctrl_Gro";
	rename -uid "F6B8DEA2-4C44-075F-B00F-5291BEEBD821";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0.0016132107635312561 -1.5015404744487334e-014 ;
	setAttr ".sp" -type "double3" 0 0.0016132107635312561 -1.5015404744487334e-014 ;
	setAttr ".mtxe" yes;
	setAttr ".xtxe" yes;
createNode nurbsCurve -n "Lips_out_Stick_Ctrl_Shape" -p "Lips_out_Stick_Ctrl";
	rename -uid "7F8E525F-4662-A086-BAFA-E08C0C198538";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 11;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		2.3840761566279479e-014 -0.23096039513974764 -2.5926789172912669e-014
		-0.040385960238607653 -0.22742700601426835 -2.5926789172912669e-014
		-0.079544806683102362 -0.2169342986981273 -2.5926789172912669e-014
		-0.11628713667849648 -0.19980120486096375 -2.5926789172912669e-014
		-0.14949541009462047 -0.17654889467098811 -2.5926789172912669e-014
		-0.17816210543446634 -0.14788219933114213 -2.5926789172912669e-014
		-0.20141441562444201 -0.11467392591501809 -2.5926789172912669e-014
		-0.21854750946160548 -0.077931595919623967 -2.5926789172912669e-014
		-0.22904021677774661 -0.038772749475129133 -2.5926789172912669e-014
		-0.23257360590322601 0.0016132107635023684 -2.5926789172912669e-014
		-0.22904021677774661 0.041999171002133837 -2.5926789172912669e-014
		-0.21854750946160548 0.081158017446628677 -2.5926789172912669e-014
		-0.20141441562444184 0.11790034744202256 -2.5926789172912669e-014
		-0.17816210543446628 0.15110862085814661 -2.5926789172912669e-014
		-0.14949541009462045 0.17977531619799256 -2.5926789172912669e-014
		-0.11628713667849648 0.20302762638796829 -2.5926789172912669e-014
		-0.07954480668310232 0.22016072022513189 -2.5926789172912669e-014
		-0.040385960238607584 0.23065342754127297 -2.5926789172912669e-014
		2.3944044995157032e-014 0.23418681666675228 -2.5926789172912669e-014
		0.040385960238655393 0.23065342754127297 -2.5926789172912669e-014
		0.079544806683150338 0.22016072022513189 -2.5926789172912669e-014
		0.11628713667854423 0.20302762638796823 -2.5926789172912669e-014
		0.14949541009466835 0.17977531619799253 -2.5926789172912669e-014
		0.17816210543451447 0.15110862085814658 -2.5926789172912669e-014
		0.20141441562449008 0.11790034744202256 -2.5926789172912669e-014
		0.21854750946165369 0.081158017446628594 -2.5926789172912669e-014
		0.22904021677779476 0.041999171002133705 -2.5926789172912669e-014
		0.23257360590327411 0.0016132107635022203 -2.5926789172912669e-014
		0.22904021677779476 -0.038772749475129278 -2.5926789172912669e-014
		0.21854750946165369 -0.07793159591962405 -2.5926789172912669e-014
		0.20141441562449003 -0.1146739259150181 -2.5926789172912669e-014
		0.1781621054345143 -0.14788219933114219 -2.5926789172912669e-014
		0.1494954100946683 -0.17654889467098819 -2.5926789172912669e-014
		0.1162871366785441 -0.19980120486096375 -2.5926789172912669e-014
		0.079544806683150171 -0.2169342986981273 -2.5926789172912669e-014
		0.040385960238655323 -0.22742700601426835 -2.5926789172912669e-014
		2.3840761566279479e-014 -0.23096039513974764 -2.5926789172912669e-014
		2.3944044995157032e-014 0.23418681666675228 -2.5926789172912669e-014
		;
createNode parentConstraint -n "Lips_out_Stick_Ctrl_Gro_parentConstraint1" -p "Lips_out_Stick_Ctrl_Gro";
	rename -uid "E5A7FDE5-420E-2F44-AEBA-ADA0E1CDCD7E";
	addAttr -ci true -k true -sn "w0" -ln "Jaw_CtrlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0.00087078345483737455 -7.1193729391965781e-015 ;
	setAttr ".rst" -type "double3" 0 -2.1684043449710089e-019 2.8398992587956425e-029 ;
	setAttr -k on ".w0";
createNode transform -n "C_Noce_Grp" -p "facial__Ctrl";
	rename -uid "A883E62D-44F1-54E4-8CDD-0BBC798382F3";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_Noce_bridge_Ctrl_Gro" -p "C_Noce_Grp";
	rename -uid "AF783230-42E2-1351-3B7E-17A65827A0E9";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.8330379277131641e-029 9.6043521718124509 22.866424185053525 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_Noce_bridge_Ctrl" -p "C_Noce_bridge_Ctrl_Gro";
	rename -uid "82DEB6A4-4883-0DA7-58F9-1083F3E976E9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Noce_bridge_Ctrl_Shape" -p "C_Noce_bridge_Ctrl";
	rename -uid "88707EE2-48D9-B203-6709-21BAB1BC05A0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
		21
		-2.3255542750401452 -3.4635092744917086 -1.391438592790418
		-2.5435054397579271 -3.0096842987828643 -1.1407779890966661
		-2.6358359687385833 -2.5558593231094093 -0.89011738542250085
		-2.5894718937736121 -2.115823666442334 -0.64707301975123488
		-2.4617860101327502 -1.7029428802343181 -0.41902707106189058
		-2.2364972152031179 -1.3297749826519203 -0.21291569444356284
		-1.909454309905124 -1.0076416908496777 -0.034992200332480738
		-1.492815285110159 -0.74635090951941652 0.10932622305432516
		-1.0211422009370497 -0.55382296546821852 0.21566495112544937
		-0.51844751942252798 -0.43591435034549614 0.28078927488306005
		1.5761980976635555e-008 -0.39620896202936295 0.30271970431716322
		0.5184475509464902 -0.43591435034549614 0.28078927488306005
		1.0211422324610102 -0.55382296546821985 0.21566495112544937
		1.4928153166341214 -0.74635090951941918 0.1093262230543276
		1.9094543410281064 -1.0076416908496566 -0.034992200332466417
		2.2364972449648897 -1.329774982651901 -0.21291569444356773
		2.4617860378439329 -1.7029428802343132 -0.41902707106187154
		2.5894719191658706 -2.1158236664423113 -0.64707301975122111
		2.6358359920200698 -2.5558593231094093 -0.89011738542250085
		2.5435054595171711 -3.0096842987146077 -1.1407779890589664
		2.3255542899469943 -3.4635092742844007 -1.3914385926759121
		;
createNode transform -n "C_Noce_A_loc" -p "C_Noce_bridge_Ctrl";
	rename -uid "4EE48431-4961-797F-A589-F888EE096081";
	setAttr ".v" no;
createNode transform -n "C_Noce_bridge_loc" -p "C_Noce_A_loc";
	rename -uid "7CEE5E44-4483-D1F8-A3DE-2F90DDAAF8BD";
	setAttr ".t" -type "double3" -4.1616093546681826e-018 -0.031341664011268477 0.79578833564387086 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 0.99999999999999989 ;
createNode locator -n "C_Noce_bridge_loc_Shape" -p "C_Noce_bridge_loc";
	rename -uid "09C9B0A9-4470-E2B1-8B3D-3CB5800397C6";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "C_Noce_Main_loc" -p "C_Noce_A_loc";
	rename -uid "196F85F4-4770-5A17-3F5B-AABB93BDDC98";
	setAttr ".t" -type "double3" -4.1616093546681796e-018 -0.031341664011268477 0.79578833564387086 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999967 0.99999999999999967 ;
createNode locator -n "C_Noce_Main_loc_Shape" -p "C_Noce_Main_loc";
	rename -uid "B7EB9761-430E-B379-E0FB-F5A746DB60D8";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "C_Noce_Main_Ctrl_Gro" -p "C_Noce_Grp";
	rename -uid "622DF97A-49FC-CBD6-7081-A89DE99BE1BC";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 7.8886090522101303e-031 2.4936532334698711 25.796603648087029 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 13.142753340505894 0 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_Noce_Main_Ctrl_G" -p "C_Noce_Main_Ctrl_Gro";
	rename -uid "B6D7A674-42F6-A2B5-AF38-8492F4C5AF8E";
	setAttr ".rp" -type "double3" 1.6618684566931167e-026 6.1223981477414924 -4.6143440229029835 ;
	setAttr ".sp" -type "double3" 1.6618684566931167e-026 6.1223981477414924 -4.6143440229029835 ;
createNode transform -n "C_Noce_Main_Ctrl" -p "C_Noce_Main_Ctrl_G";
	rename -uid "22CBDAA1-4B04-E2EB-9CB9-E3BDA64348FF";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Noce_Main_Ctrl_Shape" -p "C_Noce_Main_Ctrl";
	rename -uid "50879157-4CDB-2C02-1468-3DA2A63E43C3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		7.5791374802292431e-006 2.8649518336875026 0.94052175002046756
		0.49725227791111082 2.8214476307177629 0.94052175002046756
		0.9793883640549792 2.6922581040132969 0.94052175002046756
		1.4317715363962624 2.4813100410284874 0.94052175002046756
		1.8406422878659183 2.1950202534912409 0.94052175002046756
		2.1935956955568932 1.8420668458002685 0.94052175002046756
		2.4798854830941304 1.4331960943306168 0.94052175002046756
		2.6908335460789439 0.98081292198932923 0.94052175002046756
		2.820023072783413 0.49867683584546224 0.94052175002047189
		2.8635272757531527 0.0014321370718273253 0.94052175002047189
		2.820023072783413 -0.49581256170180416 0.94052175002047189
		2.6908335460789439 -0.97794864784567281 0.94052175002047189
		2.4798854830941304 -1.430331820186955 0.94052175002047189
		2.1935956955568932 -1.8392025716566096 0.94052175002047189
		1.8406422878659183 -2.1921559793475787 0.94052175002047189
		1.4317715363962624 -2.4784457668848332 0.94052175002047189
		0.9793883640549792 -2.6893938298696423 0.94052175002047189
		0.49725227791111082 -2.8185833565741074 0.94052175002047189
		7.5791374802292431e-006 -2.8620875595438435 0.94052175002047189
		-0.49723711963615103 -2.8185833565741074 0.94052175002047189
		-0.97937320578001885 -2.6893938298696423 0.94052175002047189
		-1.4317563781213012 -2.4784457668848332 0.94052175002047189
		-1.8406271295909604 -2.1921559793475787 0.94052175002047189
		-2.1935805372819317 -1.8392025716566096 0.94052175002047189
		-2.4798703248191765 -1.430331820186955 0.94052175002047189
		-2.6908183878039855 -0.97794864784567281 0.94052175002047189
		-2.8200079145084573 -0.49581256170180416 0.94052175002047189
		-2.8635121174781837 0.0014321370718273253 0.94052175002047189
		-2.8200079145084573 0.49867683584546224 0.94052175002047189
		-2.6908183878039855 0.98081292198932923 0.94052175002046756
		-2.4798703248191765 1.4331960943306168 0.94052175002046756
		-2.1935805372819317 1.8420668458002685 0.94052175002046756
		-1.8406271295909604 2.1950202534912409 0.94052175002046756
		-1.4317563781213012 2.4813100410284874 0.94052175002046756
		-0.97937320578001885 2.6922581040132969 0.94052175002046756
		-0.49723711963615103 2.8214476307177629 0.94052175002046756
		7.5791374802292431e-006 2.8649518336875026 0.94052175002046756
		;
createNode transform -n "C_Noce_B_loc" -p "C_Noce_Main_Ctrl";
	rename -uid "D32F2CCA-4BF2-0170-19FF-67ABDFA28006";
	setAttr -l on ".v" no;
createNode transform -n "C_Noce_Top_loc" -p "C_Noce_B_loc";
	rename -uid "AA1A06FB-4579-5074-C9A2-19B8011FA920";
	setAttr ".t" -type "double3" 0 0.27023819147894379 0.45488525119687873 ;
createNode locator -n "C_Noce_Top_loc_Shape" -p "C_Noce_Top_loc";
	rename -uid "47FB46B7-44A8-C0C7-2608-07B1DDFCFD32";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_Noce_wing_loc" -p "C_Noce_B_loc";
	rename -uid "C17EDD94-4541-4E2D-3354-DCBC9FAC1455";
	setAttr ".t" -type "double3" 1.5 -0.4 7.105427357601278e-015 ;
createNode locator -n "L_Noce_wing_loc_Shape" -p "L_Noce_wing_loc";
	rename -uid "DD63D87B-4931-9654-BF4F-BE94EE49D5C3";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "R_Noce_wing_loc" -p "C_Noce_B_loc";
	rename -uid "86CECAA6-4420-17E9-5F00-54B794B4CA99";
	setAttr ".t" -type "double3" -1.5 -0.4 0 ;
createNode locator -n "R_Noce_wing_loc_Shape" -p "R_Noce_wing_loc";
	rename -uid "BE1BA864-44CD-B352-CEC1-8A8AA4776952";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "C_Mouth_Grp" -p "facial__Ctrl";
	rename -uid "FBC9DFD5-4B2A-F8A7-A3F9-A0AEA814E373";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" 6.1506546498872197e-022 -2.909086863606245 27.324721055461644 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 2 2 2 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_Mouth_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "2B005B15-45EE-B68E-D57E-808A98514339";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -2.4385112404495845e-017 -7.7715611723760958e-016 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 180 180 -180 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -0.0078548580164287118 0 ;
	setAttr ".sp" -type "double3" 0 -0.0078548580164287118 0 ;
createNode transform -n "C_Mouth_Ctrl" -p "C_Mouth_Ctrl_Gro";
	rename -uid "10FDC068-49E1-0B32-DB16-0C8617D8BDF7";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "C_Mouth_Ctrl_Shape" -p "C_Mouth_Ctrl";
	rename -uid "D4B2FAE8-4F7C-CAA7-2C32-7FA076A7F068";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 50 0 no 3
		55 0 0 0 0.02 0.040000000000000001 0.059999999999999998 0.080000000000000002
		 0.10000000000000001 0.12 0.14000000000000001 0.16 0.17999999999999999 0.20000000000000001
		 0.22 0.23999999999999999 0.26000000000000001 0.28000000000000003 0.29999999999999999
		 0.32000000000000001 0.34000000000000002 0.35999999999999999 0.38 0.40000000000000002
		 0.41999999999999998 0.44 0.46000000000000002 0.47999999999999998 0.5 0.52000000000000002
		 0.54000000000000004 0.56000000000000005 0.57999999999999996 0.59999999999999998 0.62
		 0.64000000000000001 0.66000000000000003 0.68000000000000005 0.69999999999999996 0.71999999999999997
		 0.73999999999999999 0.76000000000000001 0.78000000000000003 0.80000000000000004 0.81999999999999995
		 0.83999999999999997 0.85999999999999999 0.88 0.90000000000000002 0.92000000000000004
		 0.93999999999999995 0.95999999999999996 0.97999999999999998 1 1 1
		53
		1.9914456605911257 -0.13061311841011047 0
		1.9780749280399188 -0.19783289809186677 0
		1.951246459721264 -0.33245231761046173 0
		1.8604610168454645 -0.51909284128981847 0
		1.7377316759761201 -0.68386377983549096 0
		1.5817390306079404 -0.82070522086223197 0
		1.4023629630660053 -0.92077558323553899 0
		1.2054089786707467 -0.98663443580137211 0
		1.0001570747165147 -0.98663443580137211 0
		0.79403133547421412 -0.98663443580137211 0
		0.58890286113483648 -0.98663443580137211 0
		0.38315425318702534 -0.98663443580137211 0
		0.1776693727217829 -0.98663443580137211 0
		0 -0.98663443580137211 0
		-0.23357162985061511 -0.98663443580137211 0
		-0.43860605025478178 -0.98663443580137211 0
		-0.64489752462781036 -0.98663443580137211 0
		-0.84932876497711296 -0.98663443580137211 0
		-1.0564295505224754 -0.98663443580137211 0
		-1.2597800340499363 -0.97092642553211805 0
		-1.4532346379022387 -0.89821107587666427 0
		-1.6263069110061239 -0.78639041390937803 0
		-1.7750634537389869 -0.64200979990025675 0
		-1.8873801971675537 -0.47026343768474066 0
		-1.9693110262117244 -0.27884590117885399 0
		-1.9968814535708057 -0.075624074543989533 0
		-2.0001508927760785 0.075557835832390369 0
		-1.9677739159690024 0.27887446901703972 0
		-1.888178620255069 0.47024895287603657 0
		-1.7746353998104565 0.64201750577235395 0
		-1.6265429919840879 0.7863861987745927 0
		-1.4530943371453224 0.8982135263772153 0
		-1.2598832518366074 0.9709247197685148 0
		-1.0001069532059634 0.9709247197685148 0
		-0.79406639989712879 0.9709247197685148 0
		-0.58888212702537146 0.9709247197685148 0
		-0.38316264868292593 0.9709247197685148 0
		-0.17767242475897144 0.9709247197685148 0
		0 0.9709247197685148 0
		0.23354342677209949 0.9709247197685148 0
		0.4386506552886823 0.9709247197685148 0
		0.64483178987355905 0.9709247197685148 0
		0.84942197032602929 0.9709247197685148 0
		1.0563067583472381 0.9709247197685148 0
		1.2598832518366074 0.9709247197685148 0
		1.4530943371453224 0.8982135263772153 0
		1.6265429919840879 0.7863861987745927 0
		1.7746353998104565 0.64201750577235395 0
		1.888178620255069 0.47024895287603657 0
		1.9677739159690024 0.27887446901703972 0
		2.0001508927760785 0.075557835832390369 0
		1.9914456605911257 -0.062326494347651709 0
		1.9914456605911257 -0.13061311841011047 0
		;
createNode transform -n "C_Mouth_loc" -p "C_Mouth_Ctrl";
	rename -uid "0FA92F7C-4C79-4E00-9FB8-C6AC55F19D25";
	setAttr -l on ".v" no;
createNode transform -n "C_Upperlip_loc" -p "C_Mouth_loc";
	rename -uid "3BCADD38-4C5C-7E6E-FF0D-9EBC0BDDC2FA";
	setAttr ".t" -type "double3" 0 0.46083477884531027 0 ;
createNode locator -n "C_Upperlip_loc_Shape" -p "C_Upperlip_loc";
	rename -uid "7159CCA5-44E7-E3C7-1CF6-8398F33017A2";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_Upperlip_loc" -p "C_Mouth_loc";
	rename -uid "DF74D8A2-4825-FEEB-BBEF-5298BA70F00B";
	setAttr ".t" -type "double3" 1.0960864424705503 0.46083477884531027 0 ;
createNode locator -n "L_Upperlip_loc_Shape" -p "L_Upperlip_loc";
	rename -uid "42F528E4-4EC5-CE29-BAFE-45B57E7899AD";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "R_Upperlip_loc" -p "C_Mouth_loc";
	rename -uid "04673894-4AD6-515A-F714-1A8EFC38E8A5";
	setAttr ".t" -type "double3" -1.09609 0.460835 0 ;
createNode locator -n "R_Upperlip_loc_Shape" -p "R_Upperlip_loc";
	rename -uid "53506E30-498B-C2A2-8E65-A6A8FDDD6E9B";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "R_lowerlip_loc" -p "C_Mouth_loc";
	rename -uid "BD174929-481A-0905-AD40-5484BA508A01";
	setAttr ".t" -type "double3" -1.09609 -0.460835 0 ;
createNode locator -n "R_lowerlip_loc_Shape" -p "R_lowerlip_loc";
	rename -uid "3EAFF4F5-45F5-AAC3-452A-A1B539F013C7";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "C_Lowerlip_loc" -p "C_Mouth_loc";
	rename -uid "F4AE5C9B-4FBD-9A1E-8083-309D776EEFDD";
	setAttr ".t" -type "double3" 0 -0.460835 0 ;
createNode locator -n "C_Lowerlip_loc_Shape" -p "C_Lowerlip_loc";
	rename -uid "2B5574F3-40E0-CB8D-B6E7-8B91D43D37D8";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_lowerlip_loc" -p "C_Mouth_loc";
	rename -uid "BBD9F031-4F28-3144-926D-CE87CEBE4EEB";
	setAttr ".t" -type "double3" 1.09609 -0.460835 0 ;
createNode locator -n "L_lowerlip_loc_Shape" -p "L_lowerlip_loc";
	rename -uid "05FBE291-42E7-7197-912F-2BA34B251072";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_Mouth_loc" -p "C_Mouth_loc";
	rename -uid "9924A629-4D3F-A4CB-F5A4-88875C031AD7";
	setAttr ".t" -type "double3" 2.8253689750374007 -5.5511151231257827e-017 0 ;
createNode locator -n "L_Mouth_loc_Shape" -p "L_Mouth_loc";
	rename -uid "ECA5BAD9-4848-1648-EDA8-AD9A7EB77218";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "R_Mouth_loc" -p "C_Mouth_loc";
	rename -uid "ED9929E4-4C69-BADA-65B6-2293195FDD21";
	setAttr ".t" -type "double3" -2.825 -5.5511199999999995e-017 0 ;
createNode locator -n "R_Mouth_loc_Shape" -p "R_Mouth_loc";
	rename -uid "3BFE22DD-447F-FA3B-A25B-84B692657BFC";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "U_Mouth_loc" -p "C_Mouth_loc";
	rename -uid "297EB55E-4ECA-933B-0F40-6BB344D3FC03";
	setAttr ".t" -type "double3" 0 1.5 0 ;
createNode locator -n "U_Mouth_loc_Shape" -p "U_Mouth_loc";
	rename -uid "15EEA432-4A5A-8489-2811-76A2CDE2ED3D";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "D_Mouth_loc" -p "C_Mouth_loc";
	rename -uid "9A365B7D-4ACC-F093-7269-1AA5FE142006";
	setAttr ".t" -type "double3" 0 -1.5 0 ;
createNode locator -n "D_Mouth_loc_Shape" -p "D_Mouth_loc";
	rename -uid "AA943144-420D-8006-FD7C-3480F27AC2EE";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "U_Mouth_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "843C1A33-4536-1211-AE61-7FAB35B1C9E3";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.5 0.5 0.5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "U_Mouth_Ctrl" -p "U_Mouth_Ctrl_Gro";
	rename -uid "5C5640DA-4509-8FE4-04A9-4C82A9A48A59";
	setAttr -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".tx";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "U_Mouth_Ctrl_Shape" -p "U_Mouth_Ctrl";
	rename -uid "007A2BE2-4DDA-0EE1-30C7-07B208B9EA03";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
		21
		-0.49821463896135626 0.3057035006268834 0
		-0.29918820852593653 0.32008440007059236 0
		-0.099772656913338836 0.32727942264506138 0
		0.099772656913338836 0.32727942264506138 0
		0.29918820852593653 0.32008440007059236 0
		0.49821463896135626 0.3057035006268834 0
		0.69659310821510434 0.28415549707730009 0
		0.95068895863001412 0.25190990652688122 0
		0.43993116545401578 -0.32727942264506138 0
		0.21994359091607865 -0.26695050012936639 0
		0.15802737710563672 -0.25249114016184804 0
		0.095187432024757726 -0.24280415358884885 0
		0.031791088110447029 -0.23794658072982552 0
		-0.031791088110447029 -0.23794658072982552 0
		-0.095187432024757726 -0.24280415358884885 0
		-0.15802737710563672 -0.25249114016184804 0
		-0.21994359091607865 -0.26695050012936639 0
		-0.43993116545401578 -0.32727942264506138 0
		-0.95068895863001412 0.25190990652688122 0
		-0.69659310821510434 0.28415549707730009 0
		-0.49821463896135626 0.3057035006268834 0
		;
createNode parentConstraint -n "U_Mouth_Ctrl_Gro_parentConstraint1" -p "U_Mouth_Ctrl_Gro";
	rename -uid "DC60D14C-42FE-7913-7B1E-0EA342E6412E";
	addAttr -ci true -k true -sn "w0" -ln "U_Mouth_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 1.3234889800848449e-023 0 -3.5527136788005009e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" 1.3234889800848449e-023 2 -1.7763568394002505e-015 ;
	setAttr -k on ".w0";
createNode transform -n "D_Mouth_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "DCCFFA52-4C93-5C00-41B8-448FF4D058E8";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.5 0.5 0.5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "D_Mouth_Ctrl" -p "D_Mouth_Ctrl_Gro";
	rename -uid "106D8C06-48B8-FF80-F92A-6290C580DE31";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "D_Mouth_Ctrl_Shape" -p "D_Mouth_Ctrl";
	rename -uid "8E305242-439C-56E9-7016-FEB2AC66B5DF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
		21
		-0.49821463896135626 -0.3057035006268834 -3.620003576629239e-015
		-0.29918820852593653 -0.32008440007059236 -3.620003576629239e-015
		-0.099772656913338836 -0.32727942264506138 -3.620003576629239e-015
		0.099772656913338836 -0.32727942264506138 -3.620003576629239e-015
		0.29918820852593653 -0.32008440007059236 -3.620003576629239e-015
		0.49821463896135626 -0.3057035006268834 -3.620003576629239e-015
		0.69659310821510434 -0.28415549707730009 -3.620003576629239e-015
		0.95068895863001412 -0.25190990652688122 -3.620003576629239e-015
		0.43993116545401578 0.32727942264506138 -3.620003576629239e-015
		0.21994359091607865 0.26695050012936639 -3.620003576629239e-015
		0.15802737710563672 0.25249114016184804 -3.620003576629239e-015
		0.095187432024757726 0.24280415358884885 -3.620003576629239e-015
		0.031791088110447029 0.23794658072982552 -3.620003576629239e-015
		-0.031791088110447029 0.23794658072982552 -3.620003576629239e-015
		-0.095187432024757726 0.24280415358884885 -3.620003576629239e-015
		-0.15802737710563672 0.25249114016184804 -3.620003576629239e-015
		-0.21994359091607865 0.26695050012936639 -3.620003576629239e-015
		-0.43993116545401578 0.32727942264506138 -3.620003576629239e-015
		-0.95068895863001412 -0.25190990652688122 -3.620003576629239e-015
		-0.69659310821510434 -0.28415549707730009 -3.620003576629239e-015
		-0.49821463896135626 -0.3057035006268834 -3.620003576629239e-015
		;
createNode parentConstraint -n "D_Mouth_Ctrl_Gro_parentConstraint1" -p "D_Mouth_Ctrl_Gro";
	rename -uid "BA7E8128-4914-A3CC-27C8-63A7E721BC23";
	addAttr -ci true -k true -sn "w0" -ln "D_Mouth_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 -1.7763568394002505e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" 0 -2 0 ;
	setAttr -k on ".w0";
createNode transform -n "L_Mouth_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "9F80B925-44EF-87DF-E1A3-DDABFF18C146";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Mouth_Ctrl" -p "L_Mouth_Ctrl_Gro";
	rename -uid "8BB9A130-4035-1F68-F340-B7887B127E18";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "L_Mouth_Ctrl_Shape" -p "L_Mouth_Ctrl";
	rename -uid "C5520864-4E8F-F9C1-C6A8-C3B07F31CB84";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 18 0 no 3
		19 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
		19
		-0.21664130687713623 0.07635345309972752 0
		-0.23207175731658936 0.15272217988967884 0
		0.23207175731658936 0.47088509798049927 0
		0.23207175731658936 -3.9809936407298819e-018 0
		0.23207175731658936 -0.47088509798049927 0
		-0.23207175731658936 -0.15272217988967909 0
		-0.21664130687713623 -0.076353453099727742 0
		-0.21431314945220947 -0.063757099211216084 0
		-0.21240508556365967 -0.051090352237224683 0
		-0.21091854572296145 -0.03836720064282427 0
		-0.20985567569732663 -0.025601688772440061 0
		-0.20921742916107175 -0.01280791498720656 0
		-0.20900475978851321 5.4809922101855799e-017 0
		-0.20921742916107175 0.012807914987206357 0
		-0.20985567569732663 0.025601688772439853 0
		-0.21091854572296145 0.038367200642824083 0
		-0.21240508556365967 0.051090352237224475 0
		-0.21431314945220947 0.063757099211215862 0
		-0.21664130687713623 0.07635345309972752 0
		;
createNode parentConstraint -n "L_Mouth_Ctrl_Gro_parentConstraint1" -p "L_Mouth_Ctrl_Gro";
	rename -uid "ED7DA7AF-4CC7-2F21-E2B2-8ABA041D407E";
	addAttr -ci true -k true -sn "w0" -ln "L_Mouth_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 -1.7763568394002505e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" 2.8253689750374011 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "R_Mouth_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "96DD8E12-4DAB-288E-5DA3-FDBA811B198C";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Mouth_Ctrl" -p "R_Mouth_Ctrl_Gro";
	rename -uid "F957B8CA-4F5C-2E9C-F8DC-0EAE288E456B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "R_Mouth_Ctrl_Shape" -p "R_Mouth_Ctrl";
	rename -uid "E261B049-4663-2975-2C9A-B4AAC79404E8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 18 0 no 3
		19 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
		19
		-0.21664130687713623 0.07635345309972752 0
		-0.23207175731658936 0.15272217988967884 0
		0.23207175731658936 0.47088509798049927 0
		0.23207175731658936 -3.9809936407298819e-018 0
		0.23207175731658936 -0.47088509798049927 0
		-0.23207175731658936 -0.15272217988967909 0
		-0.21664130687713623 -0.076353453099727742 0
		-0.21431314945220947 -0.063757099211216084 0
		-0.21240508556365967 -0.051090352237224683 0
		-0.21091854572296145 -0.03836720064282427 0
		-0.20985567569732663 -0.025601688772440061 0
		-0.20921742916107175 -0.01280791498720656 0
		-0.20900475978851321 5.4809922101855799e-017 0
		-0.20921742916107175 0.012807914987206357 0
		-0.20985567569732663 0.025601688772439853 0
		-0.21091854572296145 0.038367200642824083 0
		-0.21240508556365967 0.051090352237224475 0
		-0.21431314945220947 0.063757099211215862 0
		-0.21664130687713623 0.07635345309972752 0
		;
createNode parentConstraint -n "R_Mouth_Ctrl_Gro_parentConstraint1" -p "R_Mouth_Ctrl_Gro";
	rename -uid "7191618C-4656-176B-2BFD-49BF4EE1B55A";
	addAttr -ci true -k true -sn "w0" -ln "R_Mouth_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 4.4408920985006262e-016 0 -3.5527136788005009e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" -2.8249999999999997 0 -1.7763568394002505e-015 ;
	setAttr -k on ".w0";
createNode transform -n "C_Upperlip_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "48277D79-4ECC-5437-6A67-D39BC89D99E9";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_Upperlip_Ctrl" -p "C_Upperlip_Ctrl_Gro";
	rename -uid "C5007090-4A10-9DFB-CB77-349E96316A65";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
createNode nurbsCurve -n "C_Upperlip_Ctrl_Shape" -p "C_Upperlip_Ctrl";
	rename -uid "8E43ECBC-4797-8C3C-D862-6DAAA9B3FFDD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 1 2 3 4 5
		5
		-1.0232878030345698 -0.23207177966833115 0
		1.0232878030345698 -0.23207177966833115 0
		0.7484503717429184 0.23207177966833115 0
		-0.7484503717429184 0.23207177966833115 0
		-1.0232878030345698 -0.23207177966833115 0
		;
createNode parentConstraint -n "C_Upperlip_Ctrl_Gro_parentConstraint1" -p "C_Upperlip_Ctrl_Gro";
	rename -uid "9E3F4D5B-4091-84FF-91BC-958527F2E4BB";
	addAttr -ci true -k true -sn "w0" -ln "C_Upperlip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 1.4210854715202004e-014 -5.3290705182007514e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" 0 0.46083477884531726 -3.5527136788005009e-015 ;
	setAttr -k on ".w0";
createNode transform -n "C_Lowerlip_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "384B634C-4925-D8DC-3C35-359820CD5B60";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_Lowerlip_Ctrl" -p "C_Lowerlip_Ctrl_Gro";
	rename -uid "36F5758C-4A7E-1CFD-7F0B-79A61A735A27";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
createNode nurbsCurve -n "C_Lowerlip_Ctrl_Shape" -p "C_Lowerlip_Ctrl";
	rename -uid "414040CA-4BCD-B710-3FB4-64A131F2F186";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 1 2 3 4 5
		5
		-1.0232878030345698 0.23207177966833115 0
		1.0232878030345698 0.23207177966833115 0
		0.7484503717429184 -0.23207177966833115 0
		-0.7484503717429184 -0.23207177966833115 0
		-1.0232878030345698 0.23207177966833115 0
		;
createNode parentConstraint -n "C_Lowerlip_Ctrl_Gro_parentConstraint1" -p "C_Lowerlip_Ctrl_Gro";
	rename -uid "B9A1C976-4CBF-07C4-8268-32811ABDC604";
	addAttr -ci true -k true -sn "w0" -ln "C_Lowerlip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 -1.7763568394002505e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" 0 -0.46083499999999594 0 ;
	setAttr -k on ".w0";
createNode transform -n "L_Upperlip_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "2201BA48-4C54-4BBB-BFF2-F08D4CAE2BD6";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Upperlip_Ctrl" -p "L_Upperlip_Ctrl_Gro";
	rename -uid "16DA4E77-49EF-3DA1-DA2B-65BB6B49F39B";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
createNode nurbsCurve -n "L_Upperlip_Ctrl_Shape" -p "L_Upperlip_Ctrl";
	rename -uid "2EF513C7-4391-F8D6-27EA-7D8EBFB17266";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
	setAttr ".cc" -type "nurbsCurve" 
		1 13 0 no 3
		14 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		14
		-0.26607170897403282 0.23207177966833115 0
		-0.22319263219833377 0.23207177966833115 0
		-0.12415367364883424 0.21831377595663071 0
		-0.028533279895782471 0.1956455335021019 0
		0.062032520771026611 0.16445484012365341 0
		0.14599364995956421 0.12527545541524887 0
		0.22191387414932251 0.078777812421321869 0
		0.2884942889213562 0.025757215917110443 0
		0.34459525346755981 -0.032878853380680084 0
		0.38925737142562866 -0.096127279102802277 0
		0.42171615362167358 -0.16290578991174698 0
		0.44141608476638794 -0.23207177966833115 0
		0.0105995512482241 -0.23207177966833115 0
		-0.26607170897403282 0.23207177966833115 0
		;
createNode parentConstraint -n "L_Upperlip_Ctrl_Gro_parentConstraint1" -p "L_Upperlip_Ctrl_Gro";
	rename -uid "D62368C9-41F8-573A-4076-B794D03C054C";
	addAttr -ci true -k true -sn "w0" -ln "L_Upperlip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 7.1054273576010019e-015 -3.5527136788005009e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" 1.0960864424705503 0.46083477884531726 -1.7763568394002505e-015 ;
	setAttr -k on ".w0";
createNode transform -n "R_Upperlip_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "A2255FB7-4264-38D3-965C-C8A3FC5DF343";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Upperlip_Ctrl" -p "R_Upperlip_Ctrl_Gro";
	rename -uid "58C75A4A-4551-3F50-095E-C38326982AC5";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
createNode nurbsCurve -n "R_Upperlip_Ctrl_Shape" -p "R_Upperlip_Ctrl";
	rename -uid "F8FD48FB-4F9A-2799-76A1-D9B569E52262";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
	setAttr ".cc" -type "nurbsCurve" 
		1 13 0 no 3
		14 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		14
		-0.26607170897403282 0.23207177966833115 0
		-0.22319263219833377 0.23207177966833115 0
		-0.12415367364883424 0.21831377595663071 0
		-0.028533279895782471 0.1956455335021019 0
		0.062032520771026611 0.16445484012365341 0
		0.14599364995956421 0.12527545541524887 0
		0.22191387414932251 0.078777812421321869 0
		0.2884942889213562 0.025757215917110443 0
		0.34459525346755981 -0.032878853380680084 0
		0.38925737142562866 -0.096127279102802277 0
		0.42171615362167358 -0.16290578991174698 0
		0.44141608476638794 -0.23207177966833115 0
		0.0105995512482241 -0.23207177966833115 0
		-0.26607170897403282 0.23207177966833115 0
		;
createNode parentConstraint -n "R_Upperlip_Ctrl_Gro_parentConstraint1" -p "R_Upperlip_Ctrl_Gro";
	rename -uid "70652C1B-4035-F3CE-18B8-2AA498EC0D9C";
	addAttr -ci true -k true -sn "w0" -ln "R_Upperlip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 -3.5527136788005009e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" -1.09609 0.46083500000000294 -1.7763568394002505e-015 ;
	setAttr -k on ".w0";
createNode transform -n "L_lowerlip_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "18EA2ECE-459A-DB51-5917-A68A3CC05E7B";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_lowerlip_Ctrl" -p "L_lowerlip_Ctrl_Gro";
	rename -uid "5238884D-430B-736B-A230-BE82F6849538";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
createNode nurbsCurve -n "L_lowerlip_Ctrl_Shape" -p "L_lowerlip_Ctrl";
	rename -uid "8C865303-417B-7551-D933-6FAE467B4605";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
	setAttr ".cc" -type "nurbsCurve" 
		1 13 0 no 3
		14 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		14
		-0.26607170897403304 -0.23207177966833115 0
		-0.22319263219833377 -0.23207177966833115 0
		-0.12415367364883424 -0.21831377595663071 0
		-0.028533279895782471 -0.1956455335021019 0
		0.062032520771026611 -0.16445484012365341 0
		0.14599364995956421 -0.12527545541524887 0
		0.22191387414932251 -0.078777812421321869 0
		0.2884942889213562 -0.025757215917110443 0
		0.34459525346755981 0.032878853380680084 0
		0.38925737142562866 0.096127279102802277 0
		0.42171615362167358 0.16290578991174698 0
		0.44141608476638794 0.23207177966833115 0
		0.010599551248223879 0.23207177966833115 0
		-0.26607170897403304 -0.23207177966833115 0
		;
createNode parentConstraint -n "L_lowerlip_Ctrl_Gro_parentConstraint1" -p "L_lowerlip_Ctrl_Gro";
	rename -uid "32C6F530-4725-948A-DD0A-4DA1284F9816";
	addAttr -ci true -k true -sn "w0" -ln "L_lowerlip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -2.2204460492503131e-016 0 -1.7763568394002505e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" 1.0960899999999998 -0.46083499999999594 0 ;
	setAttr -k on ".w0";
createNode transform -n "R_lowerlip_Ctrl_Gro" -p "C_Mouth_Grp";
	rename -uid "BA1D41DC-462F-467C-B3E4-D5BA7CBE82B4";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_lowerlip_Ctrl" -p "R_lowerlip_Ctrl_Gro";
	rename -uid "3104706C-45E8-A681-58C7-E9AB96765E88";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
createNode nurbsCurve -n "R_lowerlip_Ctrl_Shape" -p "R_lowerlip_Ctrl";
	rename -uid "7D6112E4-401A-A6AB-5623-5AB039BC69AD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
	setAttr ".cc" -type "nurbsCurve" 
		1 13 0 no 3
		14 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		14
		-0.26607170897403282 -0.23207177966833115 0
		-0.22319263219833377 -0.23207177966833115 0
		-0.12415367364883424 -0.21831377595663071 0
		-0.028533279895782471 -0.1956455335021019 0
		0.062032520771026611 -0.16445484012365341 0
		0.14599364995956421 -0.12527545541524887 0
		0.22191387414932251 -0.078777812421321869 0
		0.2884942889213562 -0.025757215917110443 0
		0.34459525346755981 0.032878853380680084 0
		0.38925737142562866 0.096127279102802277 0
		0.42171615362167358 0.16290578991174698 0
		0.44141608476638794 0.23207177966833115 0
		0.0105995512482241 0.23207177966833115 0
		-0.26607170897403282 -0.23207177966833115 0
		;
createNode parentConstraint -n "R_lowerlip_Ctrl_Gro_parentConstraint1" -p "R_lowerlip_Ctrl_Gro";
	rename -uid "6C681ACD-41EF-7CB5-9CBC-8A906E8AED90";
	addAttr -ci true -k true -sn "w0" -ln "R_lowerlip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 -1.7763568394002505e-015 ;
	setAttr ".tg[0].tor" -type "double3" 3.8166656177562198e-015 0 0 ;
	setAttr ".rst" -type "double3" -1.09609 -0.46083499999999594 0 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_Grp" -p "facial__Ctrl";
	rename -uid "3C33EA7E-4E9E-16A1-E917-C98B7F178672";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" 22.649448655785644 -7.1908853515787285 10.511277501242226 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 8 8 8 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_Tongue_Ctrl_Gro" -p "C_Tongue_Grp";
	rename -uid "0A1FE0F9-4F8C-1964-8285-D79C37724863";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1.2436482061993619 1.2436482061993623 1.2436482061993623 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0 -0.54489443902387225 ;
	setAttr ".rpt" -type "double3" 0 0.082664867093044533 0.0063069629091470451 ;
	setAttr ".sp" -type "double3" 0 0 -0.43814194103096971 ;
	setAttr ".spt" -type "double3" 0 0 -0.10675249799290253 ;
createNode transform -n "Tongue_Main_Ctrl_Gro" -p "C_Tongue_Ctrl_Gro";
	rename -uid "282071F9-49B3-AE0D-C330-E3BF0E9D3CFD";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1.9721522630525306e-030 3.3537654326315964e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 0.75520083763438517 0.75520083763438517 0.75520083763438517 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Tongue_Main_Conn" -p "Tongue_Main_Ctrl_Gro";
	rename -uid "3DD7CBAE-4494-0D50-98B9-4089838BC19C";
createNode transform -n "Tongue_Main_Ctrl" -p "Tongue_Main_Conn";
	rename -uid "A5417EBE-47ED-48E6-1BA1-67BB9A1974C6";
createNode nurbsCurve -n "Tongue_Main_Ctrl_Shape" -p "Tongue_Main_Ctrl";
	rename -uid "F03E47E4-4FF4-0DC1-8DEF-3DAE5367E0B1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 39 0 no 3
		40 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39
		40
		0.017189382226080782 0.1353727151410917 -0.089064157486662188
		0.050946877618093432 0.14187893909323676 -0.089064157486662188
		0.082863020112193292 0.15465623511209514 -0.089064157486662188
		0.11178427716194544 0.17324279842862533 -0.089064157486662188
		0.13666535918397152 0.19696686221774945 -0.089064157486662188
		0.15660699904696865 0.22497097700168336 -0.089064157486662188
		0.17088845392885224 0.25624300110812626 -0.089064157486662188
		0.17899355484022328 0.28965268210740719 -0.089064157486662188
		0.18062936231651033 0.32399250708013738 -0.089064157486662188
		0.17573675401346558 0.35802134528026108 -0.089064157486662188
		0.16449256154272768 0.39050930583395271 -0.089064157486662188
		0.14730317931664688 0.42028218920024635 -0.089064157486662188
		0.12478987639537212 0.44626392580179286 -0.089064157486662188
		0.097766342204317055 0.46751546798305826 -0.089064157486662188
		0.067209277678277946 0.48326872963925827 -0.089064157486662188
		0.03422309474488093 0.49295434684941497 -0.089064157486662188
		-5.1288633287424005e-017 0.49622225617192406 -0.089064157486662188
		-0.034223094744880667 0.49295434684941503 -0.089064157486662188
		-0.067209277678277765 0.48326872963925827 -0.089064157486662188
		-0.097766342204316875 0.46751546798305826 -0.089064157486662188
		-0.12478987639537201 0.44626392580179297 -0.089064157486662188
		-0.14730317931664666 0.4202821892002464 -0.089064157486662188
		-0.16449256154272759 0.39050930583395294 -0.089064157486662188
		-0.1757367540134655 0.3580213452802613 -0.089064157486662188
		-0.18062936231651033 0.3239925070801376 -0.089064157486662188
		-0.17899355484022328 0.28965268210740741 -0.089064157486662188
		-0.1708884539288523 0.25624300110812648 -0.089064157486662188
		-0.15660699904696876 0.22497097700168353 -0.089064157486662188
		-0.13666535918397166 0.19696686221774964 -0.089064157486662188
		-0.11178427716194556 0.17324279842862553 -0.089064157486662188
		-0.082863020112193486 0.15465623511209528 -0.089064157486662188
		-0.05094687761809364 0.14187893909323682 -0.089064157486662188
		-0.01718938222608099 0.13537271514109178 -0.089064157486662188
		-0.020056030019524232 0.37757846759129254 -0.089064157486662188
		-0.10028015009762116 0.37757846759129254 -0.089064157486662188
		-0.10716500856631619 0.44840678322835414 -0.089064157486663076
		0.12093472550370279 0.39772496149163278 -0.08906415748666241
		0.10028015009762116 0.37757846759129254 -0.089064157486662188
		0.020056030019524249 0.37757846759129254 -0.089064157486662188
		0.017189382226080782 0.1353727151410917 -0.089064157486662188
		;
createNode transform -n "C_Tongue_01_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "BFDAA8E4-48D3-71F0-3EB8-459799732F63";
	setAttr ".rp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".sp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
createNode transform -n "C_Tongue_01_Ctrl" -p "C_Tongue_01_Ctrl_Gro";
	rename -uid "F14FC7D4-4A69-B1EE-6CF2-548FB398820C";
	addAttr -ci true -sn "__________" -ln "__________" -min 0 -max 1 -en "Curl:Curl" 
		-at "enum";
	addAttr -ci true -sn "Curl__L" -ln "Curl__L" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Curl__R" -ln "Curl__R" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".__________";
	setAttr -k on ".Curl__L";
	setAttr -k on ".Curl__R";
createNode nurbsCurve -n "C_Tongue_01_Ctrl_Shape" -p "C_Tongue_01_Ctrl";
	rename -uid "E5B9D32B-4FB6-2161-49D9-FB90BCAEE429";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		-0.038123576382990861 0.032427331731529035 8.7101454739189065e-016
		-0.026957439383496287 0.032427331731529035 0.02695743938349671
		-1.1487377588423462e-017 0.032427331731529035 0.038123576382991312
		0.026957439383496266 0.032427331731529035 0.026957439383496724
		0.038123576382990861 0.032427331731529035 9.0253805329538481e-016
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		;
createNode parentConstraint -n "C_Tongue_01_Ctrl_Gro_parentConstraint1" -p "C_Tongue_01_Ctrl_Gro";
	rename -uid "654722BE-4955-A7FA-A2C4-968FBFE61BF6";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".rst" -type "double3" 0 9.0412730232564996e-017 -0.43814194103096971 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_02_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "F24BFF25-4482-6E84-4B45-668525E7DEED";
	setAttr ".rp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".sp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
createNode transform -n "C_Tongue_02_Ctrl" -p "C_Tongue_02_Ctrl_Gro";
	rename -uid "C80FA759-43A4-04E6-CFD9-9B8CA0AA0571";
	addAttr -ci true -sn "__________" -ln "__________" -min 0 -max 1 -en "Curl:Curl" 
		-at "enum";
	addAttr -ci true -sn "Curl__L" -ln "Curl__L" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Curl__R" -ln "Curl__R" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".__________";
	setAttr -k on ".Curl__L";
	setAttr -k on ".Curl__R";
createNode nurbsCurve -n "C_Tongue_02_Ctrl_Shape" -p "C_Tongue_02_Ctrl";
	rename -uid "9D54A5ED-41D1-2F52-E41D-ECAB787361F8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		-0.038123576382990861 0.032427331731529035 8.7101454739189065e-016
		-0.026957439383496287 0.032427331731529035 0.02695743938349671
		-1.1487377588423462e-017 0.032427331731529035 0.038123576382991312
		0.026957439383496266 0.032427331731529035 0.026957439383496724
		0.038123576382990861 0.032427331731529035 9.0253805329538481e-016
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		;
createNode parentConstraint -n "C_Tongue_02_Ctrl_Gro_parentConstraint1" -p "C_Tongue_02_Ctrl_Gro";
	rename -uid "1A377263-46AD-22AB-B2F8-E58807C98557";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".rst" -type "double3" -6.162975822039154e-033 4.4408924955473214e-017 -0.22897163775300017 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_03_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "C4F34745-42FC-644F-A4BD-E281FDF5E56D";
	setAttr ".rp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".sp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
createNode transform -n "C_Tongue_03_Ctrl" -p "C_Tongue_03_Ctrl_Gro";
	rename -uid "92BABED6-43BA-49AA-140F-7B98D1A85115";
	addAttr -ci true -sn "__________" -ln "__________" -min 0 -max 1 -en "Curl:Curl" 
		-at "enum";
	addAttr -ci true -sn "Curl__L" -ln "Curl__L" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Curl__R" -ln "Curl__R" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".__________";
	setAttr -k on ".Curl__L";
	setAttr -k on ".Curl__R";
createNode nurbsCurve -n "C_Tongue_03_Ctrl_Shape" -p "C_Tongue_03_Ctrl";
	rename -uid "51CE9E53-49C6-A005-7C2F-F1921341F083";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		-0.038123576382990861 0.032427331731529035 8.7101454739189065e-016
		-0.026957439383496287 0.032427331731529035 0.02695743938349671
		-1.1487377588423462e-017 0.032427331731529035 0.038123576382991312
		0.026957439383496266 0.032427331731529035 0.026957439383496724
		0.038123576382990861 0.032427331731529035 9.0253805329538481e-016
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		;
createNode parentConstraint -n "C_Tongue_03_Ctrl_Gro_parentConstraint1" -p "C_Tongue_03_Ctrl_Gro";
	rename -uid "D54031E3-41F7-528F-97C5-92A1889FA258";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -3.8518598887744717e-034 0 ;
	setAttr ".rst" -type "double3" 0 4.4408924955473202e-017 -0.03042083250365599 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_04_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "EBB95E02-4246-2FB8-B64F-EC9F53B155D1";
	setAttr ".rp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".sp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
createNode transform -n "C_Tongue_04_Ctrl" -p "C_Tongue_04_Ctrl_Gro";
	rename -uid "E451FB89-4D80-D5B6-F973-9C9749826C50";
	addAttr -ci true -sn "__________" -ln "__________" -min 0 -max 1 -en "Curl:Curl" 
		-at "enum";
	addAttr -ci true -sn "Curl__L" -ln "Curl__L" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Curl__R" -ln "Curl__R" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".__________";
	setAttr -k on ".Curl__L";
	setAttr -k on ".Curl__R";
createNode nurbsCurve -n "C_Tongue_04_Ctrl_Shape" -p "C_Tongue_04_Ctrl";
	rename -uid "9440471A-49C4-DAC6-2006-F995F2EF8158";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		-0.038123576382990861 0.032427331731529035 8.7101454739189065e-016
		-0.026957439383496287 0.032427331731529035 0.02695743938349671
		-1.1487377588423462e-017 0.032427331731529035 0.038123576382991312
		0.026957439383496266 0.032427331731529035 0.026957439383496724
		0.038123576382990861 0.032427331731529035 9.0253805329538481e-016
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		;
createNode parentConstraint -n "C_Tongue_04_Ctrl_Gro_parentConstraint1" -p "C_Tongue_04_Ctrl_Gro";
	rename -uid "55E60954-421D-C0F1-3B07-E78782315EDC";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 3.4694469519536142e-018 ;
	setAttr ".rst" -type "double3" 0 3.3087224505972967e-024 0.16957916302599566 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_05_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "2EFDA633-4EFB-C06F-B122-C4B946D0C1BB";
	setAttr ".rp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".sp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
createNode transform -n "C_Tongue_05_Ctrl" -p "C_Tongue_05_Ctrl_Gro";
	rename -uid "4BFE2861-40A2-6DFB-9846-41A302A5BF23";
	addAttr -ci true -sn "__________" -ln "__________" -min 0 -max 1 -en "Curl:Curl" 
		-at "enum";
	addAttr -ci true -sn "Curl__L" -ln "Curl__L" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Curl__R" -ln "Curl__R" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".__________";
	setAttr -k on ".Curl__L";
	setAttr -k on ".Curl__R";
createNode nurbsCurve -n "C_Tongue_05_Ctrl_Shape" -p "C_Tongue_05_Ctrl";
	rename -uid "8FC97603-4147-38AB-30BC-318BE957BCC7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		-0.038123576382990861 0.032427331731529035 8.7101454739189065e-016
		-0.026957439383496287 0.032427331731529035 0.02695743938349671
		-1.1487377588423462e-017 0.032427331731529035 0.038123576382991312
		0.026957439383496266 0.032427331731529035 0.026957439383496724
		0.038123576382990861 0.032427331731529035 9.0253805329538481e-016
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		;
createNode parentConstraint -n "C_Tongue_05_Ctrl_Gro_parentConstraint1" -p "C_Tongue_05_Ctrl_Gro";
	rename -uid "3DECEA00-45D9-95D4-8237-D2828CA489C2";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_05_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".rst" -type "double3" 0 -4.4408920819570133e-017 0.36957922561087264 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_06_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "4ECFB2AB-4327-33BD-D0DC-B79AC2CB85E1";
	setAttr ".rp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".sp" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
createNode transform -n "C_Tongue_06_Ctrl" -p "C_Tongue_06_Ctrl_Gro";
	rename -uid "B2BA4451-4EE4-7161-2192-6B904C62C7F5";
	addAttr -ci true -sn "__________" -ln "__________" -min 0 -max 1 -en "Curl:Curl" 
		-at "enum";
	addAttr -ci true -sn "Curl__L" -ln "Curl__L" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Curl__R" -ln "Curl__R" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".__________";
	setAttr -k on ".Curl__L";
	setAttr -k on ".Curl__R";
createNode nurbsCurve -n "C_Tongue_06_Ctrl_Shape" -p "C_Tongue_06_Ctrl";
	rename -uid "C01C292E-4F7B-2F68-017D-7A8D8BC75CE4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		-0.038123576382990861 0.032427331731529035 8.7101454739189065e-016
		-0.026957439383496287 0.032427331731529035 0.02695743938349671
		-1.1487377588423462e-017 0.032427331731529035 0.038123576382991312
		0.026957439383496266 0.032427331731529035 0.026957439383496724
		0.038123576382990861 0.032427331731529035 9.0253805329538481e-016
		0.026957439383496304 0.032427331731529042 -0.026957439383494937
		-4.3494442201909421e-018 0.032427331731529042 -0.038123576382989542
		-0.026957439383496283 0.032427331731529042 -0.026957439383494961
		;
createNode parentConstraint -n "C_Tongue_06_Ctrl_Gro_parentConstraint1" -p "C_Tongue_06_Ctrl_Gro";
	rename -uid "5FE3A80E-4606-3153-BEA1-21BB5390E521";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_06_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -3.8518598887744717e-034 3.4694469519536142e-018 ;
	setAttr ".rst" -type "double3" 0 -9.0226253943993467e-017 0.56783352755746075 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_Main_01_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "C9E33777-41D0-C2AC-7B28-949EFF7BD226";
createNode transform -n "C_Tongue_Main_01_Ctrl" -p "C_Tongue_Main_01_Ctrl_Gro";
	rename -uid "4F1E5C13-4C6D-708A-601B-4E86440A6DB3";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Tongue_Main_01_Ctrl_Shape" -p "C_Tongue_Main_01_Ctrl";
	rename -uid "26D48847-4404-2443-37C7-73BE37023771";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 67 2 no 3
		68 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68
		68
		0.28285342314552114 -1.6543621811398503e-017 0.17987488113065958
		0.035008724147531908 -1.6543621811398503e-017 0.17987488113065958
		0.03245942932972487 -1.7090181116231096e-017 0.17696796555422006
		0.027944926930567812 -1.7090181116231096e-017 0.17300885029985005
		0.022952283573250808 -1.7090181116231096e-017 0.16967285734267895
		0.01756691873137654 -1.7090181116231096e-017 0.16701709325897093
		0.011880978233152312 -1.7090181116231096e-017 0.16508697906336872
		0.005991751994507531 -1.025410866973866e-017 0.16391554555191218
		6.1562732770159455e-009 -1.025410866973866e-017 0.163522816727178
		-0.0059917400667200728 -1.025410866973866e-017 0.16391554555191218
		-0.011880966305364851 -1.7090181116231096e-017 0.16508697906336872
		-0.017566904051022746 -1.7090181116231096e-017 0.16701709325897093
		-0.022952268892897015 -2.3926253562723532e-017 0.16967285734267895
		-0.027944915920302463 -1.7090181116231096e-017 0.17300885029985005
		-0.032459410979282628 -1.7090181116231096e-017 0.17696793619351242
		-0.035008731487708805 -1.6543621811398503e-017 0.17987488113065958
		-0.28285342314552114 -1.6543621811398503e-017 0.17987488113065958
		-0.28222977235558555 9.8526578744599873e-018 0.060996605773459889
		-0.28036953664404946 1.1929252047978601e-017 0.051644457027401731
		-0.27730448429652604 1.393415904515365e-017 0.042615158622011651
		-0.27308711225818755 1.5833086891852067e-017 0.034063147879217215
		-0.26778955978758462 1.7593536445288046e-017 0.026134787926358427
		-0.26150246338904992 1.9185388138827612e-017 0.018965725232504504
		-0.254333400695196 2.058140397476586e-017 0.012678628833969752
		-0.24640504074233713 2.1757696920170505e-017 0.007381076363366823
		-0.23785305936025028 2.2694141628245244e-017 0.0031637043250283825
		-0.22882374627450647 2.337471996582562e-017 9.8651977504971011e-005
		-0.21947161220880212 2.3787775269461102e-017 -0.0017615837340312357
		-0.045804436123351736 2.3735744044070207e-017 -0.001527255926749238
		-0.045904537785794029 2.3926253562723519e-017 0
		-0.045511816301236761 2.3926253562723519e-017 0.0059917276801714769
		-0.044340379119691707 2.3926253562723519e-017 0.011880957130143701
		-0.042410261254001103 1.7090181116231071e-017 0.01756689304075737
		-0.039754493500204581 1.7090181116231071e-017 0.022952263387764293
		-0.0364185152233873 1.7090181116231071e-017 0.027944904910037038
		-0.032459410979282628 1.7090181116231071e-017 0.03245940730919411
		-0.027944908580125567 1.7090181116231071e-017 0.036418522563564093
		-0.02295226705785279 1.7090181116231071e-017 0.039754486160027629
		-0.017566904051022746 1.7090181116231071e-017 0.042410250243735681
		-0.011880967222886963 1.0254108669738649e-017 0.044340364439337865
		-0.0059917455718527454 1.0254108669738649e-017 0.045511797950794464
		-0.0016786321655297659 1.3228200735082775e-017 0.045794512204185955
		-3.4201520150126968e-009 1.0254108669738649e-017 0.045904526775528587
		0.0059917382316758477 1.0254108669738649e-017 0.045511797950794464
		0.011880958965187954 1.0254108669738649e-017 0.044340364439337865
		0.017566893040757401 1.7090181116231071e-017 0.042410250243735681
		0.022952254212543217 1.7090181116231071e-017 0.039754486160027629
		0.027944892064727545 1.7090181116231071e-017 0.036418493202856561
		0.032459388958751931 1.7090181116231071e-017 0.03245940730919411
		0.03641849320285661 1.7090181116231071e-017 0.027944904910037038
		0.039754467809585435 1.7090181116231071e-017 0.022952263387764293
		0.042410231893293515 1.7090181116231071e-017 0.01756689304075737
		0.044340346088895664 2.3926253562723519e-017 0.011880957130143701
		0.04551177960035227 2.3926253562723519e-017 0.0059917276801714769
		0.045904501084909538 2.3926253562723519e-017 0
		0.045804182887248766 2.3736532889863025e-017 -0.0015308085723676479
		0.21947161220880212 2.3787775269461102e-017 -0.0017615837340312357
		0.22882374627450647 2.337471996582562e-017 9.8651977504971011e-005
		0.23785305936025028 2.2694141628245244e-017 0.0031637043250283825
		0.24640504074233713 2.1757696920170505e-017 0.007381076363366823
		0.254333400695196 2.058140397476586e-017 0.012678628833969752
		0.26150246338904992 1.9185388138827612e-017 0.018965725232504504
		0.26778955978758462 1.7593536445288046e-017 0.026134787926358427
		0.27308711225818755 1.5833086891852067e-017 0.034063147879217215
		0.27730448429652604 1.393415904515365e-017 0.042615158622011651
		0.28036953664404946 1.1929252047978601e-017 0.051644457027401731
		0.28222977235558555 9.8526578744599873e-018 0.060996605773459889
		0.28285342314552114 -1.6543621811398503e-017 0.17987488113065958
		;
createNode transform -n "C_Tongue_01_loc_Gro" -p "C_Tongue_Main_01_Ctrl";
	rename -uid "11FA1840-421E-E5E7-8AF9-979460D3079F";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -9.0412730232564996e-017 0.42618162551454342 ;
	setAttr ".rp" -type "double3" 0 5.5511151231257827e-017 -0.42618162551454342 ;
	setAttr ".sp" -type "double3" 0 5.5511151231257827e-017 -0.42618162551454342 ;
createNode transform -n "C_Tongue_01_loc" -p "C_Tongue_01_loc_Gro";
	rename -uid "5A56E0EE-4AE8-E3C8-3414-128E2E81C3AD";
	setAttr ".t" -type "double3" 0 9.0412730232564996e-017 -0.42618162551454342 ;
createNode locator -n "C_Tongue_01_loc_Shape" -p "C_Tongue_01_loc";
	rename -uid "16CB3ECB-44B6-9658-EC65-28A2AC5A7BEC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "C_Tongue_Main_02_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "BCA161C3-4B71-F4F0-7346-27BF3A4901F6";
createNode transform -n "C_Tongue_Main_02_Ctrl" -p "C_Tongue_Main_02_Ctrl_Gro";
	rename -uid "A86B8CE6-434F-B18D-C032-A5A60F3E2F6E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Tongue_Main_02_Ctrl_Shape" -p "C_Tongue_Main_02_Ctrl";
	rename -uid "8125E1FE-468B-F630-AFD6-E987E6A7F50D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 44 2 no 3
		45 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
		45
		-0.0059917455718527454 2.5990093442766305e-014 0.045511797950794519
		-3.4201520150126968e-009 2.5990093442766305e-014 0.04590452677552867
		0.0059917382316758477 2.5990093442766305e-014 0.045511797950794519
		0.011880958965187954 2.5990093442766305e-014 0.044340364439337893
		0.017566893040757401 2.5990093442766305e-014 0.042410235563381943
		0.022952254212543217 2.5990093442766305e-014 0.03975447147967387
		0.027944892064727545 2.5990093442766305e-014 0.036418493202856589
		0.032459388958751931 2.5990093442766305e-014 0.032459377948486579
		0.03641849320285661 2.5990093442766305e-014 0.027944904910037097
		0.039754467809585435 2.5990093442766305e-014 0.022952263387764321
		0.042410231893293515 2.5996929515212801e-014 0.01756689304075737
		0.044340346088895664 2.5996929515212801e-014 0.011880957130143728
		0.04551177960035227 2.5996929515212801e-014 0.0059917276801715325
		0.045888459128299627 2.5997695823485709e-014 0.00024478021918425408
		0.28285342314552114 2.599775017561277e-014 0
		0.27661074949757131 -2.599775017561277e-014 0.16748386244807212
		0.035257732308609242 2.5960504498796323e-014 0.16773961623171843
		0.03245942932972487 2.5962749152980335e-014 0.16454876793252235
		0.027944926930567812 2.5962749152980335e-014 0.16058965267815231
		0.022952283573250808 2.5962749152980335e-014 0.15725367440133506
		0.01756691873137654 2.5962749152980335e-014 0.15459789563727316
		0.011880978233152312 2.5962749152980335e-014 0.15266778144167101
		0.005991751994507531 2.5962749152980335e-014 0.15149634793021441
		6.1562732770159455e-009 2.5962749152980335e-014 0.15110363378583405
		-0.0059917400667200728 2.5962749152980335e-014 0.15149634793021441
		-0.011880966305364851 2.5962749152980335e-014 0.15266778144167101
		-0.017566904051022746 2.5962749152980335e-014 0.15459789563727316
		-0.022952268892897015 2.5962749152980335e-014 0.15725367440133506
		-0.027944915920302463 2.5962749152980335e-014 0.16058965267815231
		-0.032459410979282628 2.5962749152980335e-014 0.16454876059234544
		-0.035260393122734657 2.5960503820780106e-014 0.16774266974530783
		-0.27661074949757131 -2.599775017561277e-014 0.16748386244807212
		-0.28285342314552114 2.599775017561277e-014 0
		-0.04588830498458478 2.5997695178066418e-014 0.00024768692923574087
		-0.045511816301236761 2.5996929515212801e-014 0.0059917276801715325
		-0.044340379119691707 2.5996929515212801e-014 0.011880957130143728
		-0.042410261254001103 2.5996929515212801e-014 0.01756689304075737
		-0.039754493500204581 2.5990093442766305e-014 0.022952263387764321
		-0.0364185152233873 2.5990093442766305e-014 0.027944904910037097
		-0.032459410979282628 2.5990093442766305e-014 0.032459407309194166
		-0.027944908580125567 2.5990093442766305e-014 0.036418507883210355
		-0.02295226705785279 2.5990093442766305e-014 0.039754486160027663
		-0.017566904051022746 2.5990093442766305e-014 0.042410250243735736
		-0.011880967222886963 2.5990093442766305e-014 0.044340364439337893
		-0.0059917455718527454 2.5990093442766305e-014 0.045511797950794519
		;
createNode transform -n "C_Tongue_02_loc_Gro" -p "C_Tongue_Main_02_Ctrl";
	rename -uid "EF07BB20-49F3-F2D8-1493-BA8C69332EC4";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 6.162975822039154e-033 -4.4408924955473214e-017 0.22897163775300017 ;
	setAttr ".rp" -type "double3" 0 0 -0.22897163775300017 ;
	setAttr ".sp" -type "double3" 0 0 -0.22897163775300017 ;
createNode transform -n "C_Tongue_02_loc" -p "C_Tongue_02_loc_Gro";
	rename -uid "BBFD0D5B-4799-935E-4BCC-A48BC0001A19";
	setAttr ".t" -type "double3" -6.162975822039154e-033 4.4408924955473214e-017 -0.22897163775300017 ;
createNode locator -n "C_Tongue_02_loc_Shape" -p "C_Tongue_02_loc";
	rename -uid "E6B0DC5F-41A7-33F4-A049-3EAC02B456AC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1" -p "C_Tongue_Main_02_Ctrl_Gro";
	rename -uid "0E4A8399-47DD-53FB-44CE-7A89B70D3623";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -6.162975822039154e-033 -4.6003805277091788e-017 
		0.20917030327796957 ;
	setAttr ".rst" -type "double3" -6.162975822039154e-033 4.4408924955473214e-017 -0.22897163775300017 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_Main_03_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "20AAC32C-43F4-E122-887E-5585DC6B5EDC";
createNode transform -n "C_Tongue_Main_03_Ctrl" -p "C_Tongue_Main_03_Ctrl_Gro";
	rename -uid "94B6F52D-44B5-87CE-64E8-658D272854CE";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Tongue_Main_03_Ctrl_Shape" -p "C_Tongue_Main_03_Ctrl";
	rename -uid "1E81C263-4AD0-D2BE-FF70-D286144BA429";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 44 2 no 3
		45 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
		45
		-0.0059917455718527454 1.9020880907243308e-014 0.045511797950794519
		-3.4201520150126968e-009 1.9020880907243308e-014 0.045904519435351787
		0.0059917382316758477 1.9020880907243308e-014 0.045511797950794519
		0.011880958965187954 1.9020880907243308e-014 0.04434035709916101
		0.017566893040757401 1.9020880907243308e-014 0.042410239233470419
		0.022952254212543217 1.9020880907243308e-014 0.039754475149762339
		0.027944892064727545 1.9027716979689801e-014 0.036418500543033507
		0.032459388958751931 1.9027716979689801e-014 0.032459392628840386
		0.03641849320285661 1.9027716979689801e-014 0.027944893899771769
		0.039754467809585435 1.9027716979689801e-014 0.022952256047587445
		0.042410231893293515 1.9027716979689801e-014 0.017566893040757404
		0.044340346088895664 1.9027716979689801e-014 0.011880957130143734
		0.04551177960035227 1.903455305213629e-014 0.0059917423605253504
		0.045888466468476531 1.9032591226876393e-014 0.00024461873529251291
		0.27475330305325629 -1.903455305213629e-014 0
		0.26249931813317179 1.9017103815796607e-014 0.16754023500664639
		0.035354273985256153 1.899538771908308e-014 0.16779431522996002
		0.03245942932972487 1.8993536617457341e-014 0.16449338629782925
		0.027944926930567812 1.9000372689903833e-014 0.16053427104345919
		0.022952283573250808 1.9000372689903833e-014 0.15719829276664199
		0.01756691873137654 1.9000372689903833e-014 0.15454252134275701
		0.011880978233152312 1.9000372689903833e-014 0.15261240714715485
		0.005991751994507531 1.9000372689903833e-014 0.15144096629552131
		6.1562732770159455e-009 1.9000372689903833e-014 0.15104825215114095
		-0.0059917400667200728 1.9000372689903833e-014 0.15144096629552131
		-0.011880966305364851 1.9000372689903833e-014 0.15261240714715485
		-0.017566904051022746 1.9000372689903833e-014 0.15454252134275701
		-0.022952268892897015 1.9000372689903833e-014 0.15719829276664199
		-0.027944915920302463 1.9000372689903833e-014 0.16053427104345919
		-0.032459410979282628 1.8993536617457341e-014 0.16449337895765237
		-0.035357026551592785 1.8995387018249008e-014 0.16779747884620297
		-0.26249931813317179 1.9017103815796607e-014 0.16754023500664639
		-0.27475330305325629 -1.903455305213629e-014 0
		-0.045888312324761683 1.9032590576567568e-014 0.00024754746587470067
		-0.045511816301236761 1.903455305213629e-014 0.0059917350203484571
		-0.044340379119691707 1.9027716979689801e-014 0.01188096447032063
		-0.042410261254001103 1.9027716979689801e-014 0.017566900380934301
		-0.039754493500204581 1.9027716979689801e-014 0.022952263387764345
		-0.0364185152233873 1.9027716979689801e-014 0.027944904910037122
		-0.032459410979282628 1.9027716979689801e-014 0.032459399969017283
		-0.027944908580125567 1.9027716979689801e-014 0.036418507883210403
		-0.02295226705785279 1.9020880907243308e-014 0.039754482489939229
		-0.017566904051022746 1.9020880907243308e-014 0.042410246573647309
		-0.011880967222886963 1.9020880907243308e-014 0.044340364439337913
		-0.0059917455718527454 1.9020880907243308e-014 0.045511797950794519
		;
createNode transform -n "C_Tongue_03_loc_Gro" -p "C_Tongue_Main_03_Ctrl";
	rename -uid "B8C7301B-4258-9896-A58D-A8979380F487";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -4.4408924955473202e-017 0.030420832503655987 ;
	setAttr ".rp" -type "double3" 0 0 -0.030420832503655959 ;
	setAttr ".sp" -type "double3" 0 0 -0.030420832503655959 ;
createNode transform -n "C_Tongue_03_loc" -p "C_Tongue_03_loc_Gro";
	rename -uid "3C8BC465-46B3-169D-AB34-B0B7DDD1FEF8";
	setAttr ".t" -type "double3" 0 4.4408924955473202e-017 -0.030420832503655987 ;
createNode locator -n "C_Tongue_03_loc_Shape" -p "C_Tongue_03_loc";
	rename -uid "F600C576-4D5B-12CE-8F05-7A808E6F3932";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1" -p "C_Tongue_Main_03_Ctrl_Gro";
	rename -uid "A01D60E7-4995-6BE8-A83C-1193984E75BD";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 6.162975822039154e-033 -6.162975822039154e-033 
		0.19855080524934415 ;
	setAttr ".rst" -type "double3" 0 4.4408924955473202e-017 -0.030420832503655987 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_Main_04_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "790514A4-4745-5D6E-2777-CCB6E4AC0AC1";
createNode transform -n "C_Tongue_Main_04_Ctrl" -p "C_Tongue_Main_04_Ctrl_Gro";
	rename -uid "9F677A06-41BB-9799-5A6B-D69AAA2CAC08";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Tongue_Main_04_Ctrl_Shape" -p "C_Tongue_Main_04_Ctrl";
	rename -uid "75C6C643-4440-1975-9DA4-31A9EEFDBE67";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 44 2 no 3
		45 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
		45
		-0.0059917455718527454 1.9020880907243308e-014 0.045511797950794519
		-3.4201520150126968e-009 1.9020880907243308e-014 0.045904519435351787
		0.0059917382316758477 1.9020880907243308e-014 0.045511797950794519
		0.011880958965187954 1.9020880907243308e-014 0.04434035709916101
		0.017566893040757401 1.9020880907243308e-014 0.042410239233470426
		0.022952254212543217 1.9020880907243308e-014 0.039754475149762325
		0.027944892064727545 1.9027716979689801e-014 0.0364185005430335
		0.032459388958751931 1.9027716979689801e-014 0.032459392628840372
		0.03641849320285661 1.9027716979689801e-014 0.027944893899771756
		0.039754467809585435 1.9027716979689801e-014 0.022952256047587442
		0.042410231893293515 1.9027716979689801e-014 0.017566893040757398
		0.044340346088895664 1.9027716979689801e-014 0.011880957130143728
		0.04551177960035227 1.903455305213629e-014 0.0059917423605253539
		0.045888466468476531 1.9032591226876393e-014 0.00024461873529252331
		0.26304583166726009 -1.903455305213629e-014 0
		0.25079184674717558 1.9017103815796607e-014 0.16754023500664636
		0.035354273985256153 1.899538771908308e-014 0.16779431522995999
		0.03245942932972487 1.8993536617457341e-014 0.16449338629782925
		0.027944926930567812 1.9000372689903833e-014 0.16053427104345919
		0.022952283573250808 1.9000372689903833e-014 0.15719829276664196
		0.01756691873137654 1.9000372689903833e-014 0.15454252134275701
		0.011880978233152312 1.9000372689903833e-014 0.15261240714715482
		0.005991751994507531 1.9000372689903833e-014 0.15144096629552131
		6.1562732770159455e-009 1.9000372689903833e-014 0.15104825215114095
		-0.0059917400667200728 1.9000372689903833e-014 0.15144096629552131
		-0.011880966305364851 1.9000372689903833e-014 0.15261240714715482
		-0.017566904051022746 1.9000372689903833e-014 0.15454252134275701
		-0.022952268892897015 1.9000372689903833e-014 0.15719829276664196
		-0.027944915920302463 1.9000372689903833e-014 0.16053427104345919
		-0.032459410979282628 1.8993536617457341e-014 0.16449337895765234
		-0.035357026551592785 1.8995387018249008e-014 0.16779747884620297
		-0.25079184674717558 1.9017103815796607e-014 0.16754023500664636
		-0.26304583166726009 -1.903455305213629e-014 0
		-0.045888312324761683 1.9032590576567568e-014 0.00024754746587468679
		-0.045511816301236761 1.903455305213629e-014 0.0059917350203484432
		-0.044340379119691707 1.9027716979689801e-014 0.011880964470320636
		-0.042410261254001103 1.9027716979689801e-014 0.017566900380934308
		-0.039754493500204581 1.9027716979689801e-014 0.022952263387764349
		-0.0364185152233873 1.9027716979689801e-014 0.027944904910037122
		-0.032459410979282628 1.9027716979689801e-014 0.032459399969017283
		-0.027944908580125567 1.9027716979689801e-014 0.03641850788321041
		-0.02295226705785279 1.9020880907243308e-014 0.039754482489939229
		-0.017566904051022746 1.9020880907243308e-014 0.042410246573647309
		-0.011880967222886963 1.9020880907243308e-014 0.04434036443933792
		-0.0059917455718527454 1.9020880907243308e-014 0.045511797950794519
		;
createNode transform -n "C_Tongue_04_loc_Gro" -p "C_Tongue_Main_04_Ctrl";
	rename -uid "860313E7-4ED8-B5CE-1A3A-67A43F73759D";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -3.3087224502121107e-024 -0.16957916302599566 ;
	setAttr ".rp" -type "double3" 0 0 0.16957916302599568 ;
	setAttr ".sp" -type "double3" 0 0 0.16957916302599568 ;
createNode transform -n "C_Tongue_04_loc" -p "C_Tongue_04_loc_Gro";
	rename -uid "8DCFD58F-45BA-D001-CAB8-9EB96744E41C";
	setAttr ".t" -type "double3" 0 3.3087224502121107e-024 0.16957916302599566 ;
createNode locator -n "C_Tongue_04_loc_Shape" -p "C_Tongue_04_loc";
	rename -uid "8550F67E-4D98-E520-6CF2-36ACE537AFCC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1" -p "C_Tongue_Main_04_Ctrl_Gro";
	rename -uid "9D4CA690-4619-C17C-C020-59BF46D831DE";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -4.4408921646750752e-017 0.19999999552965164 ;
	setAttr ".rst" -type "double3" 0 3.3087224502121107e-024 0.16957916302599566 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_Main_05_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "509EA094-4203-8FC8-386D-58896B9B231D";
createNode transform -n "C_Tongue_Main_05_Ctrl" -p "C_Tongue_Main_05_Ctrl_Gro";
	rename -uid "B3E4399F-4265-4E47-4396-AC9B5A3584C2";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Tongue_Main_05_Ctrl_Shape" -p "C_Tongue_Main_05_Ctrl";
	rename -uid "76D5138B-4D53-6E80-3C89-988E93B6B6BF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 44 2 no 3
		45 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
		45
		-0.0059917455718527454 4.5037809990724512e-018 0.045511790610617608
		-3.4201520150126968e-009 4.5037809990724512e-018 0.045904519435351725
		0.0059917382316758477 4.5037809990724512e-018 0.045511790610617608
		0.011880958965187954 4.5037809990724512e-018 0.044340357099160954
		0.017566893040757401 4.5037809990724512e-018 0.042410242903558826
		0.022952254212543217 4.5037809990724512e-018 0.03975447881985078
		0.027944892064727545 4.5037809990724512e-018 0.036418500543033472
		0.032459388958751931 4.5037809990724512e-018 0.032459399969017255
		0.03641849320285661 4.5037809990724512e-018 0.027944897569860183
		0.039754467809585435 1.1339853445564887e-017 0.022952256047587383
		0.042410231893293515 1.1339853445564887e-017 0.017566900380934281
		0.044340346088895664 1.1339853445564887e-017 0.01188096447032061
		0.04551177960035227 1.1339853445564887e-017 0.0059917423605253539
		0.045888624282279834 1.349875650623624e-017 0.00024223317780075471
		0.25045037359143851 3.4634920359401728e-017 0
		0.2251434254959557 -3.4634920359401734e-017 0.16770750295779102
		0.036260961996366768 -2.3741331565948628e-017 0.16795668728311386
		0.03245942932972487 -2.2840508786897304e-017 0.16362187241441239
		0.027944926930567812 -2.2840508786897304e-017 0.1596627571600423
		0.022952283573250808 -2.2840508786897304e-017 0.15632676420287128
		0.01756691873137654 -2.2840508786897304e-017 0.15367100011916313
		0.011880978233152312 -2.2840508786897304e-017 0.15174088592356105
		0.005991751994507531 -2.2840508786897304e-017 0.15056945241210451
		6.1562732770159455e-009 -2.2840508786897304e-017 0.15017672358737022
		-0.0059917400667200728 -2.2840508786897304e-017 0.15056945241210451
		-0.011880966305364851 -2.2840508786897304e-017 0.15174088592356105
		-0.017566904051022746 -2.2840508786897304e-017 0.15367100011916313
		-0.022952268892897015 -2.2840508786897304e-017 0.15632676420287128
		-0.027944915920302463 -2.2840508786897304e-017 0.1596627571600423
		-0.032459410979282628 -2.2840508786897304e-017 0.16362187241441239
		-0.03626394210818723 -2.3742081295421138e-017 0.16796009312519444
		-0.2251434254959557 -3.4634920359401734e-017 0.16770750295779102
		-0.25045037359143851 3.4634920359401728e-017 0
		-0.045888459128299627 1.3498080119864323e-017 0.00024527935121326783
		-0.045511816301236761 1.1339853445564887e-017 0.0059917350203484432
		-0.044340379119691707 1.1339853445564887e-017 0.01188096447032061
		-0.042410261254001103 1.1339853445564887e-017 0.017566900380934281
		-0.039754493500204581 1.1339853445564887e-017 0.022952256047587383
		-0.0364185152233873 4.5037809990724512e-018 0.027944897569860183
		-0.032459410979282628 4.5037809990724512e-018 0.032459399969017255
		-0.027944908580125567 4.5037809990724512e-018 0.036418515223387238
		-0.02295226705785279 4.5037809990724512e-018 0.03975447881985078
		-0.017566904051022746 4.5037809990724512e-018 0.042410242903558826
		-0.011880967222886963 4.5037809990724512e-018 0.044340357099160954
		-0.0059917455718527454 4.5037809990724512e-018 0.045511790610617608
		;
createNode transform -n "C_Tongue_05_loc_Gro" -p "C_Tongue_Main_05_Ctrl";
	rename -uid "1738847C-4966-6726-E23F-5494A2178238";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 4.4408920819570133e-017 -0.36957922561087264 ;
	setAttr ".rp" -type "double3" 0 0 0.36957922561087259 ;
	setAttr ".sp" -type "double3" 0 0 0.36957922561087259 ;
createNode transform -n "C_Tongue_05_loc" -p "C_Tongue_05_loc_Gro";
	rename -uid "23686982-47D4-3191-070A-2C8111F3B1FE";
	setAttr ".t" -type "double3" 0 -4.4408920819570133e-017 0.36957922561087264 ;
createNode locator -n "C_Tongue_05_loc_Shape" -p "C_Tongue_05_loc";
	rename -uid "DFBCEEDD-40B2-5C15-2A4C-C48E3E9728F5";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1" -p "C_Tongue_Main_05_Ctrl_Gro";
	rename -uid "D49ED358-43F7-D43C-86FA-2D8492C1BFFD";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -4.4408924128292595e-017 0.20000006258487699 ;
	setAttr ".rst" -type "double3" 0 -4.4408920819570133e-017 0.36957922561087264 ;
	setAttr -k on ".w0";
createNode transform -n "C_Tongue_Main_06_Ctrl_Gro" -p "Tongue_Main_Ctrl";
	rename -uid "EE96EC3D-4077-9403-2A82-048CDDCACB7C";
createNode transform -n "C_Tongue_Main_06_Ctrl" -p "C_Tongue_Main_06_Ctrl_Gro";
	rename -uid "90D353A1-41AA-BE1D-098A-E0BEA5904E21";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_Tongue_Main_06_Ctrl_Shape" -p "C_Tongue_Main_06_Ctrl";
	rename -uid "71390B7B-4917-3BC8-8280-E98EC6961E63";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 49 2 no 3
		50 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
		50
		-0.0059917455718527454 3.2835412752680697e-018 0.045511797950794519
		-3.4201520150126968e-009 3.2835412752680697e-018 0.045904526775528587
		0.0059917382316758477 3.2835412752680697e-018 0.045511797950794519
		0.011880958965187954 1.0119613721760506e-017 0.044340364439337865
		0.017566893040757401 1.0119613721760506e-017 0.042410250243735681
		0.022952254212543217 1.0119613721760506e-017 0.039754486160027629
		0.027944892064727545 1.0119613721760506e-017 0.036418493202856617
		0.032459388958751931 1.0119613721760506e-017 0.032459407309194166
		0.03641849320285661 1.0119613721760506e-017 0.027944904910037097
		0.039754467809585435 1.0119613721760506e-017 0.022952263387764349
		0.042410231893293515 1.0119613721760506e-017 0.017566893040757425
		0.044340346088895664 1.6955686168252938e-017 0.011880957130143701
		0.04551177960035227 2.3791758614745362e-017 0.0059917276801715325
		0.045889020651832299 1.6593586391199982e-017 0.00023617753186022661
		0.22353792947667131 6.7199817272172554e-018 0
		0.21229570847007956 -1.4871047071525141e-018 0.02820511818423066
		0.20175144159406708 -4.4426621560593255e-018 0.049310182014629222
		0.1892791891737528 -6.8201260265818916e-018 0.069086585744422502
		0.17517646325915398 -8.5962873020065965e-018 0.087340578064219021
		0.15800150630402579 -1.1389420750238269e-017 0.10389320546125325
		0.13842597385521474 -1.4651050366749456e-017 0.11858227938679355
		0.11749396937553312 -1.7466923435851135e-017 0.13126384429152249
		0.095410643469094558 -1.9809436874182196e-017 0.14181358693950064
		0.07239242125172754 -2.1655635921110984e-017 0.15012812827930089
		0.048664884709940431 -2.2987429278496968e-017 0.15612599234735891
		0.024460576152984789 -2.3791758614745374e-017 0.1597483696463704
		-0.024460576152984789 -2.3791758614745374e-017 0.1597483696463704
		-0.048664884709940431 -2.2987429278496968e-017 0.15612599234735891
		-0.07239242125172754 -2.1655635921110984e-017 0.15012812827930089
		-0.095410643469094558 -1.9809436874182196e-017 0.14181358693950064
		-0.11749396937553312 -1.7466923435851135e-017 0.13126384429152249
		-0.13842597385521474 -1.4651050366749456e-017 0.11858227938679355
		-0.15800150630402579 -1.1389420750238269e-017 0.10389320546125325
		-0.17517646325915398 -8.5962873020065965e-018 0.087340578064219021
		-0.1892791891737528 -6.8201260265818916e-018 0.069086585744422502
		-0.20175144159406708 -4.4426621560593255e-018 0.049310182014629222
		-0.21229570847007956 -1.4871047071525141e-018 0.02820511818423066
		-0.22353792947667131 6.7199817272172554e-018 0
		-0.045888840817498312 1.659284970050093e-017 0.00023949529181788165
		-0.045511816301236761 1.6955686168252938e-017 0.0059917276801715325
		-0.044340379119691707 1.6955686168252938e-017 0.011880957130143701
		-0.042410261254001103 1.0119613721760506e-017 0.017566893040757425
		-0.039754493500204581 1.0119613721760506e-017 0.022952263387764349
		-0.0364185152233873 1.0119613721760506e-017 0.027944904910037097
		-0.032459410979282628 1.0119613721760506e-017 0.032459407309194166
		-0.027944908580125567 1.0119613721760506e-017 0.036418522563564155
		-0.02295226705785279 1.0119613721760506e-017 0.039754486160027629
		-0.017566904051022746 1.0119613721760506e-017 0.042410250243735681
		-0.011880967222886963 1.0119613721760506e-017 0.044340364439337865
		-0.0059917455718527454 3.2835412752680697e-018 0.045511797950794519
		;
createNode transform -n "C_Tongue_06_loc_Gro" -p "C_Tongue_Main_06_Ctrl";
	rename -uid "8287204A-4790-627E-8685-61918BEC6B9F";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 9.0226253943993467e-017 -0.57592220215119982 ;
	setAttr ".rp" -type "double3" 0 -5.5511151231257827e-017 0.57592220215119982 ;
	setAttr ".sp" -type "double3" 0 -5.5511151231257827e-017 0.57592220215119982 ;
createNode transform -n "C_Tongue_06_loc" -p "C_Tongue_06_loc_Gro";
	rename -uid "9251BDCA-4592-EEBC-89C2-02A1436C127E";
	setAttr ".t" -type "double3" 0 -9.0226253943993467e-017 0.57592220215119982 ;
createNode locator -n "C_Tongue_06_loc_Shape" -p "C_Tongue_06_loc";
	rename -uid "E0285DBA-4147-4316-08A8-B6BC44E6948D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1" -p "C_Tongue_Main_06_Ctrl_Gro";
	rename -uid "FD00038F-427C-C0D7-0C99-67A5FAEEA7FB";
	addAttr -ci true -k true -sn "w0" -ln "C_Tongue_05_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -4.5817333124423353e-017 0.19825430194658811 ;
	setAttr ".rst" -type "double3" 0 -9.0226253943993467e-017 0.56783352755746075 ;
	setAttr -k on ".w0";
createNode transform -n "L_Brow_Grp" -p "facial__Ctrl";
	rename -uid "DA58E06F-45CF-66CB-7E13-3B9AE9971645";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 0 -1.387778780781446e-017 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 0 -1.387778780781446e-017 ;
createNode transform -n "L_BrowInn_Ctrl_Gro" -p "L_Brow_Grp";
	rename -uid "4C210838-42B3-4517-5133-8CBF412F29A3";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 3.1096109606585407 14.906929464000989 25.193015934770944 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 5 5 5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
createNode transform -n "L_BrowInn_Ctrl" -p "L_BrowInn_Ctrl_Gro";
	rename -uid "1331C7AB-477E-5A51-AF5E-7695D2462E99";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "L_BrowInn_Ctrl_Shape" -p "L_BrowInn_Ctrl";
	rename -uid "4AEF4FE8-446B-A987-457A-428F74F16394";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.24865598652863091 0 3.5172994471363646e-014
		-0.24487826482468353 0.043178634763993959 3.5172994471363646e-014
		-0.23365999059740045 0.08504530125937533 3.5172994471363646e-014
		-0.21534214952587116 0.12432835006829972 3.5172994471363646e-014
		-0.19048195050671571 0.15983296356530458 3.5172994471363646e-014
		-0.15983296356530458 0.19048195050670955 3.5172994471363646e-014
		-0.12432835006830316 0.21534214952586869 3.5172994471363646e-014
		-0.085045301259376913 0.23365999059739909 3.5172994471363646e-014
		-0.043178634763999961 0.24487826482467884 3.5172994471363646e-014
		1.6534904702528982e-015 0.24865598652863255 3.5172994471363646e-014
		0.043178634763998879 0.24487826482467884 3.5172994471363646e-014
		0.085045301259379077 0.23365999059739909 3.5172994471363646e-014
		0.1243283500683046 0.21534214952586869 3.5172994471363646e-014
		0.15983296356530732 0.19048195050670955 3.5172994471363646e-014
		0.1904819505067146 0.15983296356530458 3.5172994471363646e-014
		0.21534214952587244 0.12432835006829972 3.5172994471363646e-014
		0.23365999059739967 0.08504530125937533 3.5172994471363646e-014
		0.24487826482468611 0.043178634763993959 3.5172994471363646e-014
		0.24865598652863005 0 3.5172994471363646e-014
		0.24487826482468611 -0.04317863476400495 3.5172994471363646e-014
		0.23365999059739967 -0.085045301259379716 3.5172994471363646e-014
		0.21534214952587244 -0.12432835006830197 3.5172994471363646e-014
		0.1904819505067146 -0.15983296356531224 3.5172994471363646e-014
		0.15983296356530732 -0.19048195050671665 3.5172994471363646e-014
		0.1243283500683046 -0.21534214952587749 3.5172994471363646e-014
		0.085045301259379077 -0.23365999059740125 3.5172994471363646e-014
		0.043178634763998879 -0.24487826482468855 3.5172994471363646e-014
		1.6534904702528982e-015 -0.24865598652863255 3.5172994471363646e-014
		-0.043178634763999961 -0.24487826482468855 3.5172994471363646e-014
		-0.085045301259376913 -0.23365999059740125 3.5172994471363646e-014
		-0.12432835006830316 -0.21534214952587749 3.5172994471363646e-014
		-0.15983296356530458 -0.19048195050671665 3.5172994471363646e-014
		-0.19048195050671571 -0.15983296356531224 3.5172994471363646e-014
		-0.21534214952587116 -0.12432835006830197 3.5172994471363646e-014
		-0.23365999059740045 -0.085045301259379716 3.5172994471363646e-014
		-0.24487826482468353 -0.04317863476400495 3.5172994471363646e-014
		-0.24865598652863091 0 3.5172994471363646e-014
		0.24865598652863005 0 3.5172994471363646e-014
		;
createNode transform -n "L_BrowMid_Ctrl_Gro" -p "L_Brow_Grp";
	rename -uid "CAD0F58B-4F99-FDC9-835F-0791CB7451EA";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 7.7249390405114609 14.71562159012435 24.420803012010968 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 5 5 5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
createNode transform -n "L_BrowMid_Ctrl" -p "L_BrowMid_Ctrl_Gro";
	rename -uid "A062B690-4F11-5EF7-98E2-1BA268A4543C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "L_BrowMid_Ctrl_Shape" -p "L_BrowMid_Ctrl";
	rename -uid "E70C29C8-4E24-F628-620C-48A438A1C515";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.20872309931200481 -3.1827355510400879e-016 1.9943005661804683e-014
		-0.20555206050697733 0.036244365550254239 1.9943005661804683e-014
		-0.19613538408450093 0.071387458265505688 1.9943005661804683e-014
		-0.18075929515726469 0.10436184915908558 1.9943005661804683e-014
		-0.15989151770604804 0.13416460224146187 1.9943005661804683e-014
		-0.13416460224146595 0.15989151770604609 1.9943005661804683e-014
		-0.10436184915908216 0.18075929515726305 1.9943005661804683e-014
		-0.071387458265505577 0.19613538408450321 1.9943005661804683e-014
		-0.036244365550258055 0.20555206050697544 1.9943005661804683e-014
		2.0080189743054912e-015 0.20872309931200417 1.9943005661804683e-014
		0.036244365550259595 0.20555206050697544 1.9943005661804683e-014
		0.071387458265508213 0.19613538408450321 1.9943005661804683e-014
		0.10436184915908724 0.18075929515726305 1.9943005661804683e-014
		0.13416460224147134 0.15989151770604609 1.9943005661804683e-014
		0.15989151770605084 0.13416460224146187 1.9943005661804683e-014
		0.18075929515726827 0.10436184915908558 1.9943005661804683e-014
		0.19613538408450337 0.071387458265505688 1.9943005661804683e-014
		0.20555206050697605 0.036244365550254239 1.9943005661804683e-014
		0.20872309931200836 -3.1827355510400879e-016 1.9943005661804683e-014
		0.20555206050697605 -0.036244365550260761 1.9943005661804683e-014
		0.19613538408450337 -0.07138745826551067 1.9943005661804683e-014
		0.18075929515726827 -0.10436184915908718 1.9943005661804683e-014
		0.15989151770605084 -0.13416460224147389 1.9943005661804683e-014
		0.13416460224147134 -0.15989151770605725 1.9943005661804683e-014
		0.10436184915908724 -0.18075929515726877 1.9943005661804683e-014
		0.071387458265508213 -0.1961353840845074 1.9943005661804683e-014
		0.036244365550259595 -0.20555206050697689 1.9943005661804683e-014
		2.0080189743054912e-015 -0.2087230993120095 1.9943005661804683e-014
		-0.036244365550258055 -0.20555206050697689 1.9943005661804683e-014
		-0.071387458265505577 -0.1961353840845074 1.9943005661804683e-014
		-0.10436184915908216 -0.18075929515726877 1.9943005661804683e-014
		-0.13416460224146595 -0.15989151770605725 1.9943005661804683e-014
		-0.15989151770604804 -0.13416460224147389 1.9943005661804683e-014
		-0.18075929515726469 -0.10436184915908718 1.9943005661804683e-014
		-0.19613538408450093 -0.07138745826551067 1.9943005661804683e-014
		-0.20555206050697733 -0.036244365550260761 1.9943005661804683e-014
		-0.20872309931200481 -3.1827355510400879e-016 1.9943005661804683e-014
		0.20872309931200836 -3.1827355510400879e-016 1.9943005661804683e-014
		;
createNode transform -n "L_BrowOut_Ctrl_Gro" -p "L_Brow_Grp";
	rename -uid "32BFBA5C-4C13-F6B7-B59B-21B64CD96420";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 10.924188864435727 14.716 23.400340975458818 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 5 5 5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
createNode transform -n "L_BrowOut_Ctrl" -p "L_BrowOut_Ctrl_Gro";
	rename -uid "CE87871F-4477-0C04-DC9E-A7B6BC0C775C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 0 -2.3153308008458742e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "L_BrowOut_Ctrl_Shape" -p "L_BrowOut_Ctrl";
	rename -uid "DACA8AA6-43D6-5F2F-B348-8E9BA983C096";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.13916187636391142 0 -2.1156347779233511e-014
		-0.13704765081060202 0.024165192708510821 -2.1156347779233511e-014
		-0.13076927355201068 0.04759613417884058 -2.1156347779233511e-014
		-0.12051757935378483 0.06958113786953446 -2.1156347779233511e-014
		-0.10660441365613336 0.089451516631756198 -2.1156347779233511e-014
		-0.089451516631759806 0.1066044136561347 -2.1156347779233511e-014
		-0.069581137869536749 0.12051757935378656 -2.1156347779233511e-014
		-0.047596134178844209 0.13076927355201032 -2.1156347779233511e-014
		-0.02416519270851257 0.13704765081060116 -2.1156347779233511e-014
		1.7799382317611913e-015 0.13916187636390723 -2.1156347779233511e-014
		0.024165192708516133 0.13704765081060116 -2.1156347779233511e-014
		0.047596134178845943 0.13076927355201032 -2.1156347779233511e-014
		0.06958113786953983 0.12051757935378656 -2.1156347779233511e-014
		0.089451516631760514 0.1066044136561347 -2.1156347779233511e-014
		0.1066044136561366 0.089451516631756198 -2.1156347779233511e-014
		0.1205175793537893 0.06958113786953446 -2.1156347779233511e-014
		0.13076927355201531 0.04759613417884058 -2.1156347779233511e-014
		0.13704765081060635 0.024165192708510821 -2.1156347779233511e-014
		0.1391618763639153 0 -2.1156347779233511e-014
		0.13704765081060635 -0.024165192708517032 -2.1156347779233511e-014
		0.13076927355201531 -0.047596134178848573 -2.1156347779233511e-014
		0.1205175793537893 -0.069581137869538748 -2.1156347779233511e-014
		0.1066044136561366 -0.089451516631760514 -2.1156347779233511e-014
		0.089451516631760514 -0.10660441365613572 -2.1156347779233511e-014
		0.06958113786953983 -0.12051757935379286 -2.1156347779233511e-014
		0.047596134178845943 -0.13076927355201748 -2.1156347779233511e-014
		0.024165192708516133 -0.13704765081060308 -2.1156347779233511e-014
		1.7799382317611913e-015 -0.13916187636391447 -2.1156347779233511e-014
		-0.02416519270851257 -0.13704765081060308 -2.1156347779233511e-014
		-0.047596134178844209 -0.13076927355201748 -2.1156347779233511e-014
		-0.069581137869536749 -0.12051757935379286 -2.1156347779233511e-014
		-0.089451516631759806 -0.10660441365613572 -2.1156347779233511e-014
		-0.10660441365613336 -0.089451516631760514 -2.1156347779233511e-014
		-0.12051757935378483 -0.069581137869538748 -2.1156347779233511e-014
		-0.13076927355201068 -0.047596134178848573 -2.1156347779233511e-014
		-0.13704765081060202 -0.024165192708517032 -2.1156347779233511e-014
		-0.13916187636391142 0 -2.1156347779233511e-014
		0.1391618763639153 0 -2.1156347779233511e-014
		;
createNode transform -n "R_Brow_Grp" -p "facial__Ctrl";
	rename -uid "74A45871-4A2D-6F11-6347-F6B1E1D456F2";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 -13.141963 -0.14325200000000024 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 -13.141963 -0.14325200000000024 ;
createNode transform -n "R_BrowInn_Ctrl_Gro" -p "R_Brow_Grp";
	rename -uid "07C2F971-440B-AD63-8CF0-AB9A3C7A8CDF";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -3.1096100979670629 14.907031822149968 25.192908234701747 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -5 5 5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
createNode transform -n "R_BrowInn_Ctrl" -p "R_BrowInn_Ctrl_Gro";
	rename -uid "D6D6BE6C-4412-132F-D157-C4A028BAA5C4";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "R_BrowInn_Ctrl_Shape" -p "R_BrowInn_Ctrl";
	rename -uid "0C7AAE8C-4849-B342-C4CB-3EBF91E347B3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.24865598652863369 -1.7763568394002505e-015 -2.3006982114864345e-015
		-0.24487826482468611 0.043178634763994077 -2.3006982114864345e-015
		-0.23365999059740125 0.085045301259377995 -2.3006982114864345e-015
		-0.2153421495258741 0.12432835006830184 -2.3006982114864345e-015
		-0.19048195050671704 0.15983296356530655 -2.3006982114864345e-015
		-0.15983296356530621 0.19048195050670988 -2.3006982114864345e-015
		-0.1243283500683058 0.21534214952586844 -2.3006982114864345e-015
		-0.08504530125937966 0.23365999059739967 -2.3006982114864345e-015
		-0.043178634764000787 0.24487826482467917 -2.3006982114864345e-015
		-9.9667782083632672e-016 0.24865598652863083 -2.3006982114864345e-015
		0.043178634763996283 0.24487826482467917 -2.3006982114864345e-015
		0.08504530125937694 0.23365999059739967 -2.3006982114864345e-015
		0.12432835006830135 0.21534214952586844 -2.3006982114864345e-015
		0.15983296356530621 0.19048195050670988 -2.3006982114864345e-015
		0.19048195050671243 0.15983296356530655 -2.3006982114864345e-015
		0.21534214952587083 0.12432835006830184 -2.3006982114864345e-015
		0.23365999059739628 0.085045301259377995 -2.3006982114864345e-015
		0.24487826482468408 0.043178634763994077 -2.3006982114864345e-015
		0.24865598652862764 -1.7763568394002505e-015 -2.3006982114864345e-015
		0.24487826482468408 -0.043178634764003632 -2.3006982114864345e-015
		0.23365999059739628 -0.085045301259378814 -2.3006982114864345e-015
		0.21534214952587083 -0.12432835006830199 -2.3006982114864345e-015
		0.19048195050671243 -0.15983296356531104 -2.3006982114864345e-015
		0.15983296356530621 -0.19048195050671535 -2.3006982114864345e-015
		0.12432835006830135 -0.2153421495258768 -2.3006982114864345e-015
		0.08504530125937694 -0.23365999059739859 -2.3006982114864345e-015
		0.043178634763996283 -0.24487826482468811 -2.3006982114864345e-015
		-9.9667782083632672e-016 -0.24865598652863108 -2.3006982114864345e-015
		-0.043178634764000787 -0.24487826482468811 -2.3006982114864345e-015
		-0.08504530125937966 -0.23365999059739859 -2.3006982114864345e-015
		-0.1243283500683058 -0.2153421495258768 -2.3006982114864345e-015
		-0.15983296356530621 -0.19048195050671535 -2.3006982114864345e-015
		-0.19048195050671704 -0.15983296356531104 -2.3006982114864345e-015
		-0.2153421495258741 -0.12432835006830199 -2.3006982114864345e-015
		-0.23365999059740125 -0.085045301259378814 -2.3006982114864345e-015
		-0.24487826482468611 -0.043178634764003632 -2.3006982114864345e-015
		-0.24865598652863369 -1.7763568394002505e-015 -2.3006982114864345e-015
		0.24865598652862764 -1.7763568394002505e-015 -2.3006982114864345e-015
		;
createNode transform -n "R_BrowMid_Ctrl_Gro" -p "R_Brow_Grp";
	rename -uid "E4AD9F90-4CDD-C03E-6CD5-B38202B724F1";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -7.7249369690325471 14.715521168867918 24.420802403657103 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -5 5 5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
createNode transform -n "R_BrowMid_Ctrl" -p "R_BrowMid_Ctrl_Gro";
	rename -uid "960BFE60-45A5-5326-D857-16A92A5A79EC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "R_BrowMid_Ctrl_Shape" -p "R_BrowMid_Ctrl";
	rename -uid "361F6C0C-4108-A8E3-F8A8-30AC1C6B2D5B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.2087230993120128 -7.0490831062189068e-015 1.5350470914273206e-015
		-0.20555206050698199 0.036244365550248278 1.5350470914273206e-015
		-0.19613538408450609 0.071387458265502093 1.5350470914273206e-015
		-0.1807592951572711 0.10436184915907629 1.5350470914273206e-015
		-0.15989151770605226 0.13416460224145729 1.5350470914273206e-015
		-0.13416460224147114 0.15989151770604138 1.5350470914273206e-015
		-0.10436184915909084 0.18075929515725719 1.5350470914273206e-015
		-0.071387458265511503 0.19613538408449652 1.5350470914273206e-015
		-0.036244365550261289 0.20555206050697053 1.5350470914273206e-015
		-2.7229745536080961e-015 0.20872309931199751 1.5350470914273206e-015
		0.036244365550253239 0.20555206050697053 1.5350470914273206e-015
		0.071387458265503356 0.19613538408449652 1.5350470914273206e-015
		0.1043618491590808 0.18075929515725719 1.5350470914273206e-015
		0.13416460224146556 0.15989151770604138 1.5350470914273206e-015
		0.15989151770604534 0.13416460224145729 1.5350470914273206e-015
		0.18075929515726111 0.10436184915907629 1.5350470914273206e-015
		0.19613538408449696 0.071387458265502093 1.5350470914273206e-015
		0.20555206050697128 0.036244365550248278 1.5350470914273206e-015
		0.2087230993120017 -7.0490831062189068e-015 1.5350470914273206e-015
		0.20555206050697128 -0.036244365550266736 1.5350470914273206e-015
		0.19613538408449696 -0.071387458265516374 1.5350470914273206e-015
		0.18075929515726111 -0.10436184915909429 1.5350470914273206e-015
		0.15989151770604534 -0.13416460224147897 1.5350470914273206e-015
		0.13416460224146556 -0.15989151770606 1.5350470914273206e-015
		0.1043618491590808 -0.18075929515727041 1.5350470914273206e-015
		0.071387458265503356 -0.19613538408451017 1.5350470914273206e-015
		0.036244365550253239 -0.20555206050698385 1.5350470914273206e-015
		-2.7229745536080961e-015 -0.20872309931201655 1.5350470914273206e-015
		-0.036244365550261289 -0.20555206050698385 1.5350470914273206e-015
		-0.071387458265511503 -0.19613538408451017 1.5350470914273206e-015
		-0.10436184915909084 -0.18075929515727041 1.5350470914273206e-015
		-0.13416460224147114 -0.15989151770606 1.5350470914273206e-015
		-0.15989151770605226 -0.13416460224147897 1.5350470914273206e-015
		-0.1807592951572711 -0.10436184915909429 1.5350470914273206e-015
		-0.19613538408450609 -0.071387458265516374 1.5350470914273206e-015
		-0.20555206050698199 -0.036244365550266736 1.5350470914273206e-015
		-0.2087230993120128 -7.0490831062189068e-015 1.5350470914273206e-015
		0.2087230993120017 -7.0490831062189068e-015 1.5350470914273206e-015
		;
createNode transform -n "R_BrowOut_Ctrl_Gro" -p "R_Brow_Grp";
	rename -uid "4B12CDE3-40A5-B5A3-2211-2D99FCE9E238";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -10.924189141436583 14.716 23.400340644105817 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -5 5 5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
createNode transform -n "R_BrowOut_Ctrl" -p "R_BrowOut_Ctrl_Gro";
	rename -uid "118EA999-43BB-8469-83FC-40BC381B17B4";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".sp" -type "double3" -4.4408920985006271e-016 -1.7763568394002509e-015 
		-4.1633363423443389e-017 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "R_BrowOut_Ctrl_Shape" -p "R_BrowOut_Ctrl";
	rename -uid "70AD3057-4C53-C529-D8D9-3BAAB16B3B9A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.13916187636391403 -4.3801983040078794e-014 3.4743862560147748e-016
		-0.13704765081060383 0.02416519270847322 3.4743862560147748e-016
		-0.13076927355201398 0.047596134178801194 3.4743862560147748e-016
		-0.12051757935378822 0.069581137869496018 3.4743862560147748e-016
		-0.1066044136561371 0.089451516631716091 3.4743862560147748e-016
		-0.089451516631761721 0.10660441365609524 3.4743862560147748e-016
		-0.069581137869540857 0.12051757935374303 3.4743862560147748e-016
		-0.047596134178845971 0.13076927355197004 3.4743862560147748e-016
		-0.024165192708516317 0.13704765081056089 3.4743862560147748e-016
		-7.1495557930260218e-016 0.13916187636387065 3.4743862560147748e-016
		0.024165192708513306 0.13704765081056089 3.4743862560147748e-016
		0.047596134178842439 0.13076927355197004 3.4743862560147748e-016
		0.069581137869536083 0.12051757935374303 3.4743862560147748e-016
		0.089451516631756739 0.10660441365609524 3.4743862560147748e-016
		0.10660441365613212 0.089451516631716091 3.4743862560147748e-016
		0.12051757935378583 0.069581137869496018 3.4743862560147748e-016
		0.13076927355201165 0.047596134178801194 3.4743862560147748e-016
		0.13704765081060363 0.02416519270847322 3.4743862560147748e-016
		0.13916187636391217 -4.3801983040078794e-014 3.4743862560147748e-016
		0.13704765081060363 -0.024165192708555525 3.4743862560147748e-016
		0.13076927355201165 -0.047596134178888097 3.4743862560147748e-016
		0.12051757935378583 -0.06958113786958009 3.4743862560147748e-016
		0.10660441365613212 -0.089451516631803341 3.4743862560147748e-016
		0.089451516631756739 -0.10660441365617591 3.4743862560147748e-016
		0.069581137869536083 -0.1205175793538303 3.4743862560147748e-016
		0.047596134178842439 -0.13076927355205145 3.4743862560147748e-016
		0.024165192708513306 -0.13704765081064671 3.4743862560147748e-016
		-7.1495557930260218e-016 -0.13916187636395633 3.4743862560147748e-016
		-0.024165192708516317 -0.13704765081064671 3.4743862560147748e-016
		-0.047596134178845971 -0.13076927355205145 3.4743862560147748e-016
		-0.069581137869540857 -0.1205175793538303 3.4743862560147748e-016
		-0.089451516631761721 -0.10660441365617591 3.4743862560147748e-016
		-0.1066044136561371 -0.089451516631803341 3.4743862560147748e-016
		-0.12051757935378822 -0.06958113786958009 3.4743862560147748e-016
		-0.13076927355201398 -0.047596134178888097 3.4743862560147748e-016
		-0.13704765081060383 -0.024165192708555525 3.4743862560147748e-016
		-0.13916187636391403 -4.3801983040078794e-014 3.4743862560147748e-016
		0.13916187636391217 -4.3801983040078794e-014 3.4743862560147748e-016
		;
createNode transform -n "L_Eye_Grp" -p "facial__Ctrl";
	rename -uid "99ED28F2-4DCA-E946-3938-A5A102F48494";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 7.410998730947238 8.553039419633869 22.842712006369212 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 2.5 2.5 2.5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.1813870274692648e-017 0 -7.5994933073855746e-017 ;
	setAttr ".sp" -type "double3" -6.9036343652815321e-017 0 -4.4408920985006291e-016 ;
	setAttr ".spt" -type "double3" 5.7222473378122681e-017 0 3.680942767762072e-016 ;
createNode transform -n "L_Eye_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "C50DD826-45B6-9383-E6AB-178F86AC45DD";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.035866977447034917 -0.49489086445509051 -1.643130076445232e-015 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 179.99999999999997 -179.99999999999997 -180.00000000000003 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.035866977447034917 0.4948908644550763 -1.3322676295501883e-016 ;
	setAttr ".sp" -type "double3" 0.3586697744703492 4.9489086445507615 -1.3322676295501878e-015 ;
	setAttr ".spt" -type "double3" -0.32280279702331427 -4.4540177800956853 1.1990408665951693e-015 ;
createNode transform -n "L_Eye_Ctrl" -p "L_Eye_Ctrl_Gro";
	rename -uid "EA84078B-42D6-2568-A27C-A585EC54E139";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".t" -type "double3" 0 0 9.0087032138032208e-031 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr ".rp" -type "double3" 0.35866977447034853 4.9489086445507482 -1.3322676295501776e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034853 4.9489086445507482 -1.3322676295501776e-015 ;
	setAttr ".mnsl" -type "double3" 0.5 0.5 -1 ;
	setAttr ".mxsl" -type "double3" 2 2 1 ;
createNode nurbsCurve -n "L_Eye_Ctrl_Shape" -p "L_Eye_Ctrl";
	rename -uid "2F78FC35-4EB5-F616-5C9E-83B30DA0A87B";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.5712440431118198 6.1614829131922111 1.2642787689053412e-015
		0.35866977447035214 6.6637476206481603 1.2642787689053412e-015
		-0.8539044941711158 6.1614829131922111 1.2642787689053412e-015
		-1.3561692016270472 4.9489086445507295 1.2642787689053412e-015
		-0.85390449417111547 3.7363343759092857 1.2642787689053412e-015
		0.35866977447035142 3.2340696684533623 1.2642787689053412e-015
		1.5712440431118184 3.7363343759092857 1.2642787689053412e-015
		2.0735087505677448 4.9489086445507295 1.2642787689053412e-015
		1.5712440431118198 6.1614829131922111 1.2642787689053412e-015
		0.35866977447035214 6.6637476206481603 1.2642787689053412e-015
		-0.8539044941711158 6.1614829131922111 1.2642787689053412e-015
		;
createNode transform -n "L_Eye_loc" -p "L_Eye_Ctrl";
	rename -uid "CE87B6CA-4084-9939-7428-E9ACCD66569F";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
createNode transform -n "L_TLid_loc" -p "L_Eye_loc";
	rename -uid "E1EA46B9-4E5F-82A8-8DF6-E2BC5C0FBDB0";
	setAttr ".t" -type "double3" -0.0026912611862278408 -1.4961531860495725 -1.7763569021837655e-015 ;
	setAttr ".rp" -type "double3" 0.36405229684280327 6.9827301911465582 -2.9422099554972518e-007 ;
	setAttr ".sp" -type "double3" 0.36405229684280327 6.9827301911465582 -2.9422099554972518e-007 ;
createNode locator -n "L_TLid_loc_Shape" -p "L_TLid_loc";
	rename -uid "5725B66C-41F5-1EFF-A0BD-6699ADA44FD9";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0.36405229684280327 6.9827301911465511 -2.9422099554972518e-007 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_BLid_loc" -p "L_Eye_loc";
	rename -uid "612F2975-401F-2993-B93A-98BA85A065D8";
	setAttr ".t" -type "double3" -0.0026912611862278408 1.4679246858600206 -1.7763569021837655e-015 ;
	setAttr ".rp" -type "double3" 0.36405229684280327 2.9326866054082714 -2.9422099554972545e-007 ;
	setAttr ".sp" -type "double3" 0.36405229684280327 2.9326866054082714 -2.9422099554972545e-007 ;
createNode locator -n "L_BLid_loc_Shape" -p "L_BLid_loc";
	rename -uid "E126C3E9-4BFF-A330-044F-33A6D7A12EDC";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0.36405229684280327 2.9326866054082714 -2.9422099554972545e-007 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_EyeOutCorner_loc" -p "L_Eye_loc";
	rename -uid "5DC0E13D-4F13-A15E-803A-259D8A04AD83";
	setAttr ".t" -type "double3" -0.716134324470317 0 0 ;
	setAttr ".rp" -type "double3" 2.2420457789237691 4.9489087006797519 -1.8873791418627709e-015 ;
	setAttr ".sp" -type "double3" 2.2420457789237691 4.9489087006797519 -1.8873791418627709e-015 ;
createNode locator -n "L_EyeOutCorner_loc_Shape" -p "L_EyeOutCorner_loc";
	rename -uid "DBDF7FCD-4794-6861-89E8-29A2D51A4F39";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 2.2420457789237691 4.9489087006797519 -1.8873791418627693e-015 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_EyeInnCorner_loc" -p "L_Eye_loc";
	rename -uid "AE03AF41-492F-2AF1-E516-23BA30409447";
	setAttr ".t" -type "double3" 0.73606642750821916 0 1.4723771071048274e-015 ;
	setAttr ".rp" -type "double3" -1.5247062299830707 4.9489087006797519 -1.8873791418627709e-015 ;
	setAttr ".sp" -type "double3" -1.5247062299830707 4.9489087006797519 -1.8873791418627709e-015 ;
createNode locator -n "L_EyeInnCorner_loc_Shape" -p "L_EyeInnCorner_loc";
	rename -uid "48CDDA18-4B14-3E75-111F-009599A8CCF5";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -1.5247062299830707 4.9489087006797519 -1.8873791418627693e-015 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_Pupil_loc" -p "L_Eye_loc";
	rename -uid "BD07C022-415B-94F1-C034-97B60C624C78";
	setAttr ".rp" -type "double3" 0.35866977447034998 4.9489086445507837 -1.3322676295501926e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034998 4.9489086445507837 -1.3322676295501926e-015 ;
createNode locator -n "L_Pupil_loc_Shape" -p "L_Pupil_loc";
	rename -uid "FD57D4DC-4C70-1E2E-B461-02A5ACF7F249";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0.35866977447034998 4.9489086445507837 -1.332267629550191e-015 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "L_BLid_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "A39150AB-4C02-D29B-6078-2695A556C0FC";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 1 -1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.017960401335379735 0.23736432203182556 1.4711050377006651e-009 ;
	setAttr ".rpt" -type "double3" 0 -0.47472864406365112 -2.9422100463325843e-009 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 4.7472864406365121 -2.9422100754013413e-008 ;
	setAttr ".spt" -type "double3" -0.34124762537221487 -4.5099221186046865 3.0893205791714079e-008 ;
createNode transform -n "L_BLid_Ctrl" -p "L_BLid_Ctrl_Gro";
	rename -uid "88F9D593-46B6-BD78-3F54-14944256BF2A";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".t" -type "double3" 1.1368683772161595e-013 1 1.323488980084844e-022 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35920802670759461 4.7472864406365121 -2.9422100754013413e-008 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 4.7472864406365121 -2.9422100754013413e-008 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "L_BLid_Ctrl_Shape" -p "L_BLid_Ctrl";
	rename -uid "B4ACE91A-4E83-B7A1-B961-8596D382D1AB";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		3 27 2 no 3
		32 -2 -1 0 1 2 3 4 5 6 8 9 10 11 12 13 13.999999999999998 15.000000000000002
		 16 17 18 19 20 22 23 24 25 26 27 27.999999999999996 29 30.000000000000004 30.999999999999996
		
		30
		0.35580008650377831 4.8511035306878174 1.4714371513818224e-008
		0.11400882776974192 4.8299414655716371 1.4714371513818224e-008
		-0.120436545866891 4.7670902004486528 1.4714371513818272e-008
		-0.34041092533403061 4.6644613532022303 1.4714371513818272e-008
		-0.53923217522017985 4.5251704058352047 1.471437168956352e-008
		-0.70867967265368337 4.3593955159593953 -7.355857516571175e-008
		-0.70867967265368337 4.3593955159593953 -7.355857516571175e-008
		-0.55918337902596793 4.2223616082625703 -5.6751991481026257e-008
		-0.55918337902596793 4.2223616082625703 -5.6751991481026257e-008
		-0.4107450776368014 4.3719701626309666 1.471437168956355e-008
		-0.2404657750495561 4.4912619457608844 1.471437168956352e-008
		-0.052069901735661547 4.5791599566273513 1.471437168956352e-008
		0.14871899848302464 4.6329879301936607 1.471437168956352e-008
		0.35580008650377831 4.6511118883166072 1.4714371513818224e-008
		0.56288145884651997 4.6329879301936607 -5.6366125772714687e-008
		0.76367078554819301 4.579157680891778 -5.6366125772714687e-008
		0.95206651670109044 4.4912619457608844 -5.6366125772714687e-008
		1.1223449663223699 4.3719701626309666 -5.6366125772714687e-008
		1.2636056854061823 4.2258347221977317 -6.025583372687285e-008
		1.2636056854061823 4.2258347221977317 -6.0255833726872797e-008
		1.4270957260688462 4.3557013694766393 -6.9877510252394849e-008
		1.4270957260688462 4.3557013694766393 -6.9877510252394849e-008
		1.2508323482277357 4.5251704058352047 -5.6366125772714687e-008
		1.0520116669855679 4.6644613532022303 -5.6366125948459975e-008
		0.83203686103544283 4.7670856489775026 -5.6366125948459975e-008
		0.59759205604279231 4.8299414655716371 -5.6366125948460067e-008
		0.3558000865037782 4.8511035306878245 1.4714371513818909e-008
		0.35580008650377831 4.8511035306878174 1.4714371513818224e-008
		0.11400882776974192 4.8299414655716371 1.4714371513818224e-008
		-0.120436545866891 4.7670902004486528 1.4714371513818272e-008
		;
createNode transform -n "L_BLid_lowOrb_loc" -p "L_BLid_Ctrl";
	rename -uid "E80818AD-4688-455A-0444-20BC5C9F15E8";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0.35651676552137068 4.1989890873540423 2.6479889535576872e-007 ;
	setAttr ".r" -type "double3" 180 0 0 ;
	setAttr ".s" -type "double3" 1.2436482061993626 1.2436482061993626 -1.2436482061993626 ;
createNode transform -n "L_lowOrb_loc" -p "L_BLid_lowOrb_loc";
	rename -uid "2363370F-47C5-CA11-DCBD-FFB7BF875C2B";
	setAttr ".t" -type "double3" -6.0397163055983716e-031 -0.877 0 ;
createNode locator -n "L_lowOrb_loc_Shape" -p "L_lowOrb_loc";
	rename -uid "CEFE066E-4119-0FB2-29E9-87ABEAB6E898";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "L_BLid_Ctrl_Gro_parentConstraint1" -p "L_BLid_Ctrl_Gro";
	rename -uid "B835BB69-41F8-1F30-F1CE-98AF799CE518";
	addAttr -ci true -k true -sn "w0" -ln "L_BLid_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -4.4408920985006262e-016 0 1.0587911840678754e-022 ;
	setAttr ".tg[0].tor" -type "double3" 1.4415055300262408e-030 -8.1609577290022391e-030 
		3.8073983268542248e-014 ;
	setAttr ".rst" -type "double3" -1.1102230246251563e-016 0 3.3087224502121107e-024 ;
	setAttr -k on ".w0";
createNode transform -n "L_TLid_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "8417498C-4FB6-F179-C37E-899CA947FB52";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.017960401335379735 0.25761453996051636 -1.4711050377006676e-009 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 5.1522907992103386 -2.9422100754013413e-008 ;
	setAttr ".spt" -type "double3" -0.34124762537221487 -4.8946762592498221 2.7950995716312743e-008 ;
createNode transform -n "L_TLid_Ctrl" -p "L_TLid_Ctrl_Gro";
	rename -uid "61380861-4C3B-AD2C-EE57-9986394B1641";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".t" -type "double3" -1.2621774483536189e-029 1 5.2939559203393771e-022 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35920802670759461 5.1522907992103386 -2.9422100754013413e-008 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 5.1522907992103386 -2.9422100754013413e-008 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "L_TLid_Ctrl_Shape" -p "L_TLid_Ctrl";
	rename -uid "C74A559B-45D6-FC1D-0627-4D87F87E12D8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 27 2 no 3
		32 -2 -1 0 1 2 3 4 5 6 8 9 10 11 12 13 13.999999999999998 15.000000000000002
		 16 17 18 19 20 22 23 24 25 26 27 27.999999999999996 29 30.000000000000004 30.999999999999996
		
		30
		0.35579735422194508 5.2653517029250363 1.4749757537448367e-008
		0.11381224177455204 5.2441834636094731 1.4749757537448367e-008
		-0.1208210960858353 5.1813138611342371 1.4749757537448387e-008
		-0.34097183780248813 5.078655071112296 1.4749757537448387e-008
		-0.53995249062895279 4.9393234845129044 1.4749757713334557e-008
		-0.70953584089174204 4.77350022850566 -7.3593961090548174e-008
		-0.70953584089174204 4.77350022850566 -7.3593961090548174e-008
		-0.55991969011201848 4.6364263400855998 -5.6773902896183574e-008
		-0.55991969011201848 4.6364263400855998 -5.6773902896183574e-008
		-0.4113623798054955 4.7860785439295723 1.4749757713334557e-008
		-0.2409465574975308 4.9054051313779636 1.4749757713334557e-008
		-0.052399639684287062 4.9933287871822731 1.4749757713334557e-008
		0.148550241018607 5.0471724654843495 1.4749757713334557e-008
		0.35579735422194508 5.0653017114150041 1.4749757537448367e-008
		0.5630447519752263 5.0471724654843495 -5.6387727823915768e-008
		0.76399505950303315 4.993326510782734 -5.6387727823915768e-008
		0.95254183504130852 4.9054051313779636 -5.6387727823915768e-008
		1.1229568036994415 4.7860785439295723 -5.6387727823915768e-008
		1.2643307771460928 4.6399004673291397 -6.0280554312361418e-008
		1.2643307771460928 4.6399004673291397 -6.0280554312361365e-008
		1.4279518943069107 4.7698050042265274 -6.9909944920406519e-008
		1.4279518943069107 4.7698050042265274 -6.9909944920406519e-008
		1.2515471990728455 4.9393234845129044 -5.6387727823915768e-008
		1.0525671153462626 5.078655071112296 -5.6387727999801855e-008
		0.83241594680469533 5.1813093083351456 -5.6387727999801855e-008
		0.59778317804419523 5.2441834636094731 -5.6387727999801881e-008
		0.35579735422194508 5.265351702925039 1.4749757537448367e-008
		0.35579735422194508 5.2653517029250363 1.4749757537448367e-008
		0.11381224177455204 5.2441834636094731 1.4749757537448367e-008
		-0.1208210960858353 5.1813138611342371 1.4749757537448387e-008
		;
createNode transform -n "L_TLid_UppOrb_loc" -p "L_TLid_Ctrl";
	rename -uid "356BD60C-41C8-1634-3370-569A818AF366";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0.35651676552136929 4.6146224386641315 2.6479889535576829e-007 ;
	setAttr ".s" -type "double3" 1.2436482061993623 1.2436482061993623 1.2436482061993623 ;
createNode transform -n "L_UppOrb_loc" -p "L_TLid_UppOrb_loc";
	rename -uid "DFA50958-430C-4C94-946A-DB8950842E9F";
	setAttr ".t" -type "double3" -6.0397163055983716e-031 0.87676250980551984 0 ;
createNode locator -n "L_UppOrb_loc_Shape" -p "L_UppOrb_loc";
	rename -uid "E2BF38B9-47F9-319F-ED2D-35847D13086A";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "L_TLid_Ctrl_Gro_parentConstraint1" -p "L_TLid_Ctrl_Gro";
	rename -uid "5359E5DE-45DB-C770-F7D8-9EAE6339A007";
	addAttr -ci true -k true -sn "w0" -ln "L_TLid_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 8.8817841970012523e-016 -1.4210854715202004e-014 
		-1.5881867761018131e-022 ;
	setAttr ".tg[0].tor" -type "double3" 1.4415055300262408e-030 -8.1609577290022391e-030 
		3.8073983268542248e-014 ;
	setAttr ".rst" -type "double3" 5.5511151231257827e-017 8.8817841970012523e-016 3.3087224502121107e-024 ;
	setAttr -k on ".w0";
createNode transform -n "L_Eyeball_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "B35BE94F-4975-05E2-2BA9-8AA59E4B3E06";
	setAttr -l on -k off ".v";
	setAttr -k off ".tz";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.028693581957627844 0.39591269156406095 -1.0658141036401512e-016 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".spt" -type "double3" -0.32997619251272137 -4.5529959529867012 1.2256862191861727e-015 ;
createNode transform -n "L_Eyeball_Ctrl" -p "L_Eyeball_Ctrl_Gro";
	rename -uid "AE4D0D37-4A2D-3C6F-0D11-898ABCAEBCFF";
	addAttr -ci true -sn "______________" -ln "______________" -min 0 -max 1 -en "Pupil:Pupil" 
		-at "enum";
	addAttr -ci true -sn "Pupil_Inn" -ln "Pupil_Inn" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Pupil_Out" -ln "Pupil_Out" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Bulge__FB" -ln "Bulge__FB" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mnsl" -type "double3" 0.5 0.5 -1 ;
	setAttr ".mxsl" -type "double3" 2 2 1 ;
	setAttr ".msxe" yes;
	setAttr ".msye" yes;
	setAttr ".xsxe" yes;
	setAttr ".xsye" yes;
	setAttr -l on -k on ".______________";
	setAttr -k on ".Pupil_Inn";
	setAttr -k on ".Pupil_Out";
	setAttr -k on ".Bulge__FB";
createNode nurbsCurve -n "L_Eyeball_Ctrl_Shape" -p "L_Eyeball_Ctrl";
	rename -uid "386CE7F3-404E-6022-E539-9B8BF0D095B9";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.67849308085448912 5.2687319509349146 -1.9906762306882797e-015
		0.35866977447034365 5.4012071020022248 -1.9906762306882797e-015
		0.038846468086198606 5.2687319509349146 -1.9906762306882797e-015
		-0.093628682981120551 4.9489086445507517 -1.9906762306882797e-015
		0.038846468086198606 4.6290853381666084 -1.9906762306882797e-015
		0.35866977447034293 4.4966101870992956 -1.9906762306882797e-015
		0.67849308085448912 4.6290853381666084 -1.9906762306882797e-015
		0.81096823192180656 4.9489086445507517 -1.9906762306882797e-015
		0.67849308085448912 5.2687319509349146 -1.9906762306882797e-015
		0.35866977447034365 5.4012071020022248 -1.9906762306882797e-015
		0.038846468086198606 5.2687319509349146 -1.9906762306882797e-015
		;
createNode transform -n "L_pupil_Inn_Gro" -p "L_Eyeball_Ctrl";
	rename -uid "CCD13999-4EE9-0288-DAB1-BE8682030E1A";
	setAttr ".t" -type "double3" -8.8817841970012523e-016 0 0 ;
	setAttr ".rp" -type "double3" 0.35866977447034909 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
createNode transform -n "L_pupil_Inn_Ctrl" -p "L_pupil_Inn_Gro";
	rename -uid "96AF06FD-4DFC-3BCA-5BFB-2AB6AA8D273D";
	setAttr -l on -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".mntl" -type "double3" -2 -2 -1 ;
	setAttr ".mxtl" -type "double3" 2 2 1 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mnsl" -type "double3" 0.5 0.5 -1 ;
	setAttr ".mxsl" -type "double3" 2 2 1 ;
createNode nurbsCurve -n "L_pupil_Inn_Ctrl_Shape" -p "L_pupil_Inn_Ctrl";
	rename -uid "EC915711-4892-38E2-0BD4-7880F1090434";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.42063748581297167 5.0108763558933873 -1.2085323504891327e-015
		0.35866977447034754 5.0365442223607255 -1.2085323504891327e-015
		0.29670206312772385 5.0108763558933873 -1.2085323504891327e-015
		0.27103419666038781 4.9489086445507606 -1.2085323504891327e-015
		0.29670206312772385 4.8869409332081393 -1.2085323504891327e-015
		0.35866977447034742 4.861273066740802 -1.2085323504891327e-015
		0.42063748581297167 4.8869409332081393 -1.2085323504891327e-015
		0.44630535228030782 4.9489086445507606 -1.2085323504891327e-015
		0.42063748581297167 5.0108763558933873 -1.2085323504891327e-015
		0.35866977447034754 5.0365442223607255 -1.2085323504891327e-015
		0.29670206312772385 5.0108763558933873 -1.2085323504891327e-015
		;
createNode transform -n "L_pupil_Out_Gro" -p "L_Eyeball_Ctrl";
	rename -uid "2BD739E6-4E95-3D05-095C-53A9FB53722A";
	setAttr ".r" -type "double3" 0 0 -7.9513867036587919e-016 ;
	setAttr ".rp" -type "double3" 0.35866977447034909 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
createNode transform -n "L_pupil_Out_Ctrl" -p "L_pupil_Out_Gro";
	rename -uid "2E470EE9-49EF-72CF-ADCD-98A41438564F";
	setAttr -l on -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".mntl" -type "double3" -2 -2 -1 ;
	setAttr ".mxtl" -type "double3" 2 2 1 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mnsl" -type "double3" 0.5 0.5 -1 ;
	setAttr ".mxsl" -type "double3" 2 2 1 ;
createNode nurbsCurve -n "L_pupil_Out_Ctrl_Shape" -p "L_pupil_Out_Ctrl";
	rename -uid "A827DECC-4380-C0C7-492D-14A4E80C91F4";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.4631142544641883 5.0533531245446008 -1.3373755685152341e-015
		0.35866977447034709 5.0966154446730556 -1.3373755685152341e-015
		0.25422529447650621 5.0533531245446008 -1.3373755685152341e-015
		0.21096297434805183 4.9489086445507597 -1.3373755685152341e-015
		0.25422529447650621 4.8444641645569204 -1.3373755685152341e-015
		0.35866977447034676 4.8012018444284719 -1.3373755685152341e-015
		0.4631142544641883 4.8444641645569204 -1.3373755685152341e-015
		0.50637657459264196 4.9489086445507597 -1.3373755685152341e-015
		0.4631142544641883 5.0533531245446008 -1.3373755685152341e-015
		0.35866977447034709 5.0966154446730556 -1.3373755685152341e-015
		0.25422529447650621 5.0533531245446008 -1.3373755685152341e-015
		;
createNode parentConstraint -n "L_Eyeball_Ctrl_Gro_parentConstraint1" -p "L_Eyeball_Ctrl_Gro";
	rename -uid "B36B0372-41A0-900F-5D79-62B63614BE0D";
	addAttr -ci true -k true -sn "w0" -ln "L_Pupil_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -1.3322676295501878e-015 -7.1054273576010019e-015 
		3.1554436208840493e-030 ;
	setAttr ".tg[0].tor" -type "double3" 1.4415055300262408e-030 -8.1609577290022391e-030 
		3.8073983268542248e-014 ;
	setAttr ".rst" -type "double3" -1.1102230246251563e-016 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "L_UppOrb_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "FF25C63B-4D82-B990-2A1A-11A27FF007A0";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
createNode transform -n "L_UppOrb_Ctrl" -p "L_UppOrb_Ctrl_Gro";
	rename -uid "E030B4C9-4590-F412-CBB0-049216FB7643";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "L_UppOrb_Ctrl_Shape" -p "L_UppOrb_Ctrl";
	rename -uid "831B1502-4C90-1233-303B-118FD8226C48";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		-0.36644984550366994 1.0618799737568336e-016 0
		-0.25911917072040769 -0.25911917072040752 0
		-5.5209245064404264e-017 -0.36644984550366994 0
		0.25911917072040747 -0.25911917072040763 0
		0.36644984550366994 -1.968209268663648e-016 0
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		;
createNode scaleConstraint -n "L_UppOrb_Ctrl_Gro_scaleConstraint1" -p "L_UppOrb_Ctrl_Gro";
	rename -uid "2885D608-49F2-C79E-A6FE-B9AD9B2BA945";
	addAttr -ci true -k true -sn "w0" -ln "L_UppOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0.40204295516014094 0.40204295516014094 0.40204295516014094 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "L_UppOrb_Ctrl_Gro_parentConstraint1" -p "L_UppOrb_Ctrl_Gro";
	rename -uid "3DA5E31C-4465-9F79-1EE9-948C23AF374D";
	addAttr -ci true -k true -sn "w0" -ln "L_UppOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 8.8817841970012523e-016 2.8421709430404007e-014 
		1.7763568394002505e-015 ;
	setAttr ".tg[0].tor" -type "double3" 2.5154015479521509e-015 1.7034912821776445e-014 
		-1.3038451241281015e-013 ;
	setAttr ".rst" -type "double3" 2.6645352591003757e-015 1.0903841225825062 5.3290705182007514e-015 ;
	setAttr -k on ".w0";
createNode transform -n "L_lowOrb_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "439E6C7F-4197-9A1A-F9EA-83AF7A0A47FF";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
createNode transform -n "L_lowOrb_Ctrl" -p "L_lowOrb_Ctrl_Gro";
	rename -uid "C72EFF2B-4414-AA2B-A757-A4817C1EA5FC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "L_lowOrb_Ctrl_Shape" -p "L_lowOrb_Ctrl";
	rename -uid "60EB9CEC-4156-61A3-88DD-23B61CACDD46";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		-0.36644984550366994 1.0618799737568338e-016 0
		-0.25911917072040769 -0.25911917072040752 0
		-5.5209245064404264e-017 -0.36644984550366994 0
		0.25911917072040747 -0.25911917072040763 0
		0.36644984550366994 -1.968209268663648e-016 0
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		;
createNode scaleConstraint -n "L_lowOrb_Ctrl_Gro_scaleConstraint1" -p "L_lowOrb_Ctrl_Gro";
	rename -uid "E28F4D84-44CD-A029-BAA3-8BB759DC715F";
	addAttr -ci true -k true -sn "w0" -ln "L_lowOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0.40204295516014094 -0.40204295516014094 0.40204295516014094 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "L_lowOrb_Ctrl_Gro_parentConstraint1" -p "L_lowOrb_Ctrl_Gro";
	rename -uid "B22DFF4F-416B-41A0-C944-4EA3D5ACA1E9";
	addAttr -ci true -k true -sn "w0" -ln "L_lowOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 8.8817841970012523e-016 4.2632564145606011e-014 
		-1.7763568394002505e-015 ;
	setAttr ".tg[0].tor" -type "double3" -8.314756955327001e-015 -7.3477293604092943e-015 
		-4.1136117496624562e-014 ;
	setAttr ".rst" -type "double3" 8.8817841970012523e-016 -1.09067947683684 0 ;
	setAttr -k on ".w0";
createNode transform -n "L_EyeOutCorner_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "07CB4386-4F24-03E7-7BA2-C39D6510ED48";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".rp" -type "double3" 0.027350368745784344 0.24744543250818252 -6.9388939039072284e-017 ;
	setAttr ".sp" -type "double3" 0.54700737491569118 4.9489086501636601 -1.3877787807814457e-015 ;
	setAttr ".spt" -type "double3" -0.51965700616990673 -4.7014632176554771 1.3183898417423734e-015 ;
createNode transform -n "L_EyeOutCorner_Ctrl" -p "L_EyeOutCorner_Ctrl_Gro";
	rename -uid "76B43097-4AB5-DAC3-D6CB-61ABE2FF3378";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.54700737491569118 4.9489086501636601 -1.3877787807814457e-015 ;
	setAttr ".sp" -type "double3" 0.54700737491569118 4.9489086501636601 -1.3877787807814457e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "L_EyeOutCorner_Ctrl_Shape" -p "L_EyeOutCorner_Ctrl";
	rename -uid "923E8142-44EF-0712-EA2D-CB97E33649FB";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.77430631539928629 5.3520222266514583 -2.6277473358814501e-015
		0.77430631539928541 5.352022226651445 -2.6277473358814501e-015
		0.22555813057075105 4.9816854909014383 -2.6277473358814501e-015
		0.22555813057075075 4.9489086501635287 -2.6277473358814501e-015
		0.22555813057075105 4.9161318094256057 -2.6277473358814501e-015
		0.77430631539928541 4.5457950736754444 -2.6277473358814501e-015
		0.77430631539928629 4.5457950736754622 -2.6277473358814501e-015
		0.86845661926061923 4.9489086501634247 -2.6277473358814501e-015
		0.77430631539928629 5.3520222266514583 -2.6277473358814501e-015
		0.77430631539928541 5.352022226651445 -2.6277473358814501e-015
		0.22555813057075105 4.9816854909014383 -2.6277473358814501e-015
		;
createNode scaleConstraint -n "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1" -p "L_EyeOutCorner_Ctrl_Gro";
	rename -uid "E9466EC0-4EE2-9366-A24C-7FBDEA695ADC";
	addAttr -ci true -k true -sn "w0" -ln "L_EyeOutCorner_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0.5 0.5 0.5 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "L_EyeOutCorner_Ctrl_Gro_parentConstraint1" -p "L_EyeOutCorner_Ctrl_Gro";
	rename -uid "E97653D9-4F3C-40CB-96CA-4EAA34330ACB";
	addAttr -ci true -k true -sn "w0" -ln "L_EyeOutCorner_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -7.1054273576010019e-015 -1.577721810442025e-030 ;
	setAttr ".tg[0].tor" -type "double3" 1.4415055300262408e-030 -8.1609577290022391e-030 
		3.8073983268542248e-014 ;
	setAttr ".rst" -type "double3" 0 -8.8817841970012523e-016 -3.9443045261050739e-031 ;
	setAttr -k on ".w0";
createNode transform -n "L_EyeInnCorner_Ctrl_Gro" -p "L_Eye_Grp";
	rename -uid "6D17917F-47CD-A0AB-6F8D-99898FC33038";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".rp" -type "double3" 0.0085166087012503201 0.24744543250818249 -6.9388939039072284e-017 ;
	setAttr ".sp" -type "double3" 0.17033217402500719 4.9489086501636592 -1.3877787807814457e-015 ;
	setAttr ".spt" -type "double3" -0.16181556532375685 -4.7014632176554763 1.3183898417423734e-015 ;
createNode transform -n "L_EyeInnCorner_Ctrl" -p "L_EyeInnCorner_Ctrl_Gro";
	rename -uid "30DECD7E-4204-C1D1-5376-E2806CF5C717";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.17033217402500719 4.9489086501636592 -1.3877787807814457e-015 ;
	setAttr ".sp" -type "double3" 0.17033217402500719 4.9489086501636592 -1.3877787807814457e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "L_EyeInnCorner_Ctrl_Shape" -p "L_EyeInnCorner_Ctrl";
	rename -uid "0867D92C-4273-899E-4494-E6B74BB78C86";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.4917814183699511 4.981685490901449 -2.6277473358814545e-015
		-0.056966766458584499 5.3520222266514841 -2.6277473358814545e-015
		-0.056966766458584416 5.3520222266514734 -2.6277473358814545e-015
		-0.15111707031994026 4.9489086501636539 -2.6277473358814501e-015
		-0.056966766458583694 4.5457950736754551 -2.6277473358814545e-015
		-0.05696676645858377 4.545795073675456 -2.6277473358814545e-015
		0.49178141836995104 4.9161318094256137 -2.6277473358814545e-015
		0.49178141836993394 4.9489086501636539 -2.6277473358814501e-015
		0.4917814183699511 4.981685490901449 -2.6277473358814545e-015
		-0.056966766458584499 5.3520222266514841 -2.6277473358814545e-015
		-0.056966766458584416 5.3520222266514734 -2.6277473358814545e-015
		;
createNode scaleConstraint -n "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1" -p "L_EyeInnCorner_Ctrl_Gro";
	rename -uid "4B956B6C-4F90-515D-7A45-D697D5C39744";
	addAttr -ci true -k true -sn "w0" -ln "L_EyeInnCorner_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0.5 0.5 0.5 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "L_EyeInnCorner_Ctrl_Gro_parentConstraint1" -p "L_EyeInnCorner_Ctrl_Gro";
	rename -uid "FF657F46-4F3C-1113-B89B-9CB8218B9F68";
	addAttr -ci true -k true -sn "w0" -ln "L_EyeInnCorner_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -6.6613381477509392e-016 -1.4210854715202004e-014 
		3.1554436208840493e-030 ;
	setAttr ".tg[0].tor" -type "double3" 1.4415055300262408e-030 -8.1609577290022391e-030 
		3.8073983268542248e-014 ;
	setAttr ".rst" -type "double3" -8.3266726846886741e-017 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "R_Eye_Grp" -p "facial__Ctrl";
	rename -uid "2F94BA82-40B6-E15E-8293-7391FCFDABA6";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -7.4109926732486668 8.5531044390031568 22.842820742995315 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -2.5 2.5 -2.5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 9.4510962197541182e-017 0 ;
	setAttr ".sp" -type "double3" 0 5.5229074922252256e-016 0 ;
	setAttr ".spt" -type "double3" 0 -4.5777978702498144e-016 0 ;
createNode transform -n "R_Eye_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "7C23ECA6-4087-010D-C46B-7097B9CC2E03";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.035866977447034917 -0.49489086445507546 1.3322676295501883e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.035866977447034917 0.4948908644550763 -1.3322676295501883e-016 ;
	setAttr ".sp" -type "double3" 0.3586697744703492 4.9489086445507615 -1.3322676295501878e-015 ;
	setAttr ".spt" -type "double3" -0.32280279702331427 -4.4540177800956853 1.1990408665951693e-015 ;
createNode transform -n "R_Eye_Ctrl" -p "R_Eye_Ctrl_Gro";
	rename -uid "7CB54B5C-44D2-7940-BE56-EEA1B7DEC1CD";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 0 0 9.0087032138032208e-031 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr ".rp" -type "double3" 0.3586697744703492 4.9489086445507615 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.3586697744703492 4.9489086445507615 -1.3322676295501878e-015 ;
	setAttr ".mnsl" -type "double3" 0.5 0.5 -1 ;
	setAttr ".mxsl" -type "double3" 2 2 1 ;
createNode nurbsCurve -n "R_Eye_Ctrl_Shape" -p "R_Eye_Ctrl";
	rename -uid "21A616AA-4CBB-604C-9D8F-2387D6498DA0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.5712440431118193 6.161482913192212 5.2962797444894833e-015
		0.3586697744703502 6.6637476206481523 5.2962797444894833e-015
		-0.85390449417111691 6.161482913192212 5.2962797444894833e-015
		-1.3561692016270486 4.9489086445507464 5.2962797444894833e-015
		-0.85390449417111813 3.7363343759092782 5.2962797444894833e-015
		0.35866977447034998 3.2340696684533601 5.2962797444894833e-015
		1.5712440431118189 3.7363343759092782 5.2962797444894833e-015
		2.0735087505677456 4.9489086445507464 5.2962797444894833e-015
		1.5712440431118193 6.161482913192212 5.2962797444894833e-015
		0.3586697744703502 6.6637476206481523 5.2962797444894833e-015
		-0.85390449417111691 6.161482913192212 5.2962797444894833e-015
		;
createNode transform -n "R_Eye_loc" -p "R_Eye_Ctrl";
	rename -uid "C3A989D8-48EF-C53D-2BA8-E8920F4224C0";
	setAttr -l on ".v" no;
createNode transform -n "R_TLid_loc" -p "R_Eye_loc";
	rename -uid "741AA8B9-4EF0-4E62-5585-2DB400FAF527";
	setAttr ".t" -type "double3" -0.0031923082325571173 -1.4963340527131663 -3.7172984670874598e-005 ;
	setAttr ".rp" -type "double3" 0.36405229684280327 6.9827301911465582 -2.9422099554972518e-007 ;
	setAttr ".sp" -type "double3" 0.36405229684280327 6.9827301911465582 -2.9422099554972518e-007 ;
createNode locator -n "R_TLid_loc_Shape" -p "R_TLid_loc";
	rename -uid "106516AE-46F5-84C1-A861-4BB277F0E71B";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0.36405229684280327 6.9827301911465511 -2.9422099554972518e-007 ;
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "R_BLid_loc" -p "R_Eye_loc";
	rename -uid "C185B3C2-4AAC-D581-32AA-5E910B333160";
	setAttr ".t" -type "double3" -0.0031923082325571173 1.4679558932403154 -3.7172984670874598e-005 ;
	setAttr ".rp" -type "double3" 0.36405229684280327 2.9326866054082714 -2.9422099554972545e-007 ;
	setAttr ".sp" -type "double3" 0.36405229684280327 2.9326866054082714 -2.9422099554972545e-007 ;
createNode locator -n "R_BLid_loc_Shape" -p "R_BLid_loc";
	rename -uid "F50C5560-42EA-5AF3-DCD8-58956C661A76";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0.36405229684280327 2.9326866054082714 -2.9422099554972545e-007 ;
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "R_EyeOutCorner_loc" -p "R_Eye_loc";
	rename -uid "4403CD8E-405C-4830-AED7-0ABFF011D24D";
	setAttr ".t" -type "double3" -0.71660106010515801 -0.0001300803314023824 -3.7467205665109304e-005 ;
	setAttr ".rp" -type "double3" 2.2420457789237691 4.9489087006797519 -1.8873791418627709e-015 ;
	setAttr ".sp" -type "double3" 2.2420457789237691 4.9489087006797519 -1.8873791418627709e-015 ;
createNode locator -n "R_EyeOutCorner_loc_Shape" -p "R_EyeOutCorner_loc";
	rename -uid "F66198F3-4765-ABB0-875B-95A212E21392";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 2.2420457789237691 4.9489087006797519 -1.8873791418627693e-015 ;
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "R_EyeInnCorner_loc" -p "R_Eye_loc";
	rename -uid "C4150787-460D-F7A6-73C4-23818EDAC7AE";
	setAttr ".t" -type "double3" 0.73559066007204332 -0.0001300803314023824 -3.7467205665109304e-005 ;
	setAttr ".rp" -type "double3" -1.5247062299830707 4.9489087006797519 -1.8873791418627709e-015 ;
	setAttr ".sp" -type "double3" -1.5247062299830707 4.9489087006797519 -1.8873791418627709e-015 ;
createNode locator -n "R_EyeInnCorner_loc_Shape" -p "R_EyeInnCorner_loc";
	rename -uid "D0F360E3-4000-B8C2-B0FD-8D9EFA249A0F";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -1.5247062299830707 4.9489087006797519 -1.8873791418627693e-015 ;
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "R_Pupil_loc" -p "R_Eye_loc";
	rename -uid "88C8DB96-4EB9-5ADF-FCB7-BABC13D642E5";
	setAttr ".rp" -type "double3" 0.35866977447034998 4.9489086445507837 -1.3322676295501926e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034998 4.9489086445507837 -1.3322676295501926e-015 ;
createNode locator -n "R_Pupil_loc_Shape" -p "R_Pupil_loc";
	rename -uid "42F88940-428B-E2B4-9895-2FBFC8111184";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0.35866977447034998 4.9489086445507837 -1.332267629550191e-015 ;
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "R_BLid_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "C5F313CD-4493-F246-046E-9F8FCE7AA580";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 1 -1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.017960401335379735 0.23736432203182559 1.4711050377006651e-009 ;
	setAttr ".rpt" -type "double3" 0 -0.47472864406365117 -2.9422100463325843e-009 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 4.7472864406365121 -2.9422100754013413e-008 ;
	setAttr ".spt" -type "double3" -0.34124762537221487 -4.5099221186046865 3.0893205791714079e-008 ;
createNode transform -n "R_BLid_Ctrl" -p "R_BLid_Ctrl_Gro";
	rename -uid "E336EA79-493C-0B80-D95E-64BAAD62CFC4";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 1.1368683772161597e-013 1 1.323488980084844e-022 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35920802670759461 4.7472864406365121 -2.9422100754013413e-008 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 4.7472864406365121 -2.9422100754013413e-008 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "R_BLid_Ctrl_Shape" -p "R_BLid_Ctrl";
	rename -uid "86EB8DE8-4844-8A90-743B-A3B4D1BD7A6B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		3 27 2 no 3
		32 -2 -1 0 1 2 3 4 5 6 8 9 10 11 12 13 13.999999999999998 15.000000000000002
		 16 17 18 19 20 22 23 24 25 26 27 27.999999999999996 29 30.000000000000004 30.999999999999996
		
		30
		0.35580008650377809 4.8523308527658662 1.4714372758332279e-008
		0.11400882776974176 4.8311687876496823 1.4714372758332279e-008
		-0.12043654586689126 4.7683175225266963 1.4714372758332317e-008
		-0.34041092533403072 4.6656886752802817 1.4714372758332317e-008
		-0.53923217522017963 4.5263977279132463 1.4714372934077436e-008
		-0.70867967265368381 4.3606228380374432 -7.3558573921197713e-008
		-0.70867967265368381 4.3606228380374432 -7.3558573921197713e-008
		-0.55918337902596793 4.2235889303406191 -5.6751990236512399e-008
		-0.55918337902596793 4.2235889303406191 -5.6751990236512399e-008
		-0.41074507763680129 4.3731974847090189 1.4714372934077494e-008
		-0.24046577504955641 4.4924892678389226 1.4714372934077451e-008
		-0.052069901735661651 4.5803872787054054 1.4714372934077451e-008
		0.14871899848302447 4.6342152522716926 1.4714372934077436e-008
		0.35580008650377809 4.652339210394647 1.4714372758332279e-008
		0.56288145884651997 4.6342152522716926 -5.6366124528200842e-008
		0.76367078554819301 4.5803850029698285 -5.6366124528200868e-008
		0.95206651670109077 4.4924892678389226 -5.6366124528200842e-008
		1.1223449663223697 4.3731974847090189 -5.6366124528200868e-008
		1.2636056854061817 4.2270620442757716 -6.02558324823588e-008
		1.2636056854061817 4.2270620442757716 -6.0255832482358774e-008
		1.4270957260688453 4.3569286915546774 -6.9877509007881037e-008
		1.4270957260688453 4.3569286915546774 -6.9877509007881037e-008
		1.250832348227735 4.5263977279132463 -5.6366124528200868e-008
		1.0520116669855679 4.6656886752802817 -5.6366124703945858e-008
		0.83203686103544261 4.7683129710555505 -5.6366124703945858e-008
		0.59759205604279142 4.8311687876496823 -5.6366124703945924e-008
		0.35580008650377809 4.8523308527658751 1.4714372758332873e-008
		0.35580008650377809 4.8523308527658662 1.4714372758332279e-008
		0.11400882776974176 4.8311687876496823 1.4714372758332279e-008
		-0.12043654586689126 4.7683175225266963 1.4714372758332317e-008
		;
createNode transform -n "R_BLid_lowOrb_loc" -p "R_BLid_Ctrl";
	rename -uid "D7D8F76A-405F-4023-76E5-FEA9882A0E44";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0.3570178125676986 4.1990202947343391 3.7437783564454017e-005 ;
	setAttr ".s" -type "double3" 1.2436482061993626 -1.244 1.244 ;
createNode transform -n "R_lowOrb_loc" -p "R_BLid_lowOrb_loc";
	rename -uid "283E85CE-4C38-802C-4757-81AC3A760C5F";
	setAttr ".t" -type "double3" -6.0397163055983716e-031 -0.877 0 ;
createNode locator -n "R_lowOrb_loc_Shape" -p "R_lowOrb_loc";
	rename -uid "1D3D4B97-4DFE-5348-C3F0-0785E9D5B480";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "R_BLid_Ctrl_Gro_parentConstraint1" -p "R_BLid_Ctrl_Gro";
	rename -uid "F4182BFF-4311-2818-5E79-078855B6EB6E";
	addAttr -ci true -k true -sn "w0" -ln "R_BLid_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -8.8817841970012523e-016 0 0 ;
	setAttr ".tg[0].tor" -type "double3" 3.3482102233306935e-030 2.853391132930927e-029 
		7.6148046557426831e-014 ;
	setAttr ".rst" -type "double3" -1.1102230246251563e-016 -8.8817841970012523e-016 
		-3.3087224502121107e-024 ;
	setAttr -k on ".w0";
createNode transform -n "R_TLid_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "C6247BD3-422C-07E9-A313-D3A5D4D2F8EB";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.017960401335379735 0.25761453996051648 -1.4711050377006676e-009 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 5.1522907992103386 -2.9422100754013413e-008 ;
	setAttr ".spt" -type "double3" -0.34124762537221487 -4.8946762592498221 2.7950995716312743e-008 ;
createNode transform -n "R_TLid_Ctrl" -p "R_TLid_Ctrl_Gro";
	rename -uid "94AFAB47-4CBB-3D01-53F2-84B157728031";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -3.7865323450608567e-029 1 5.2939559203393771e-022 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35920802670759461 5.1522907992103386 -2.9422100754013413e-008 ;
	setAttr ".sp" -type "double3" 0.35920802670759461 5.1522907992103386 -2.9422100754013413e-008 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode nurbsCurve -n "R_TLid_Ctrl_Shape" -p "R_TLid_Ctrl";
	rename -uid "345DEE98-41EF-D7E2-1890-A2BF80D42729";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 27 2 no 3
		32 -2 -1 0 1 2 3 4 5 6 8 9 10 11 12 13 13.999999999999998 15.000000000000002
		 16 17 18 19 20 22 23 24 25 26 27 27.999999999999996 29 30.000000000000004 30.999999999999996
		
		30
		0.35579735422194531 5.265351702925047 1.4749757537448367e-008
		0.11381224177455224 5.2441834636094873 1.4749757537448367e-008
		-0.12082109608583493 5.1813138611342504 1.4749757537448387e-008
		-0.34097183780248769 5.0786550711123102 1.4749757537448387e-008
		-0.53995249062895256 4.9393234845129177 1.4749757713334557e-008
		-0.70953584089174204 4.7735002285056751 -7.3593961090548174e-008
		-0.70953584089174204 4.7735002285056751 -7.3593961090548174e-008
		-0.55991969011201848 4.6364263400856132 -5.6773902896183574e-008
		-0.55991969011201848 4.6364263400856132 -5.6773902896183574e-008
		-0.4113623798054955 4.7860785439295812 1.4749757713334557e-008
		-0.24094655749753041 4.9054051313779734 1.4749757713334557e-008
		-0.052399639684286702 4.9933287871822856 1.4749757713334557e-008
		0.14855024101860723 5.0471724654843584 1.4749757713334557e-008
		0.35579735422194531 5.0653017114150165 1.4749757537448367e-008
		0.5630447519752263 5.0471724654843584 -5.6387727823915768e-008
		0.76399505950303359 4.9933265107827447 -5.6387727823915768e-008
		0.95254183504130896 4.9054051313779734 -5.6387727823915768e-008
		1.1229568036994415 4.7860785439295812 -5.6387727823915768e-008
		1.2643307771460932 4.6399004673291495 -6.0280554312361418e-008
		1.2643307771460932 4.6399004673291495 -6.0280554312361365e-008
		1.4279518943069107 4.7698050042265416 -6.9909944920406519e-008
		1.4279518943069107 4.7698050042265416 -6.9909944920406519e-008
		1.2515471990728466 4.9393234845129177 -5.6387727823915768e-008
		1.0525671153462637 5.0786550711123102 -5.6387727999801855e-008
		0.83241594680469611 5.1813093083351545 -5.6387727999801855e-008
		0.59778317804419523 5.2441834636094873 -5.6387727999801881e-008
		0.35579735422194531 5.2653517029250487 1.4749757537448367e-008
		0.35579735422194531 5.265351702925047 1.4749757537448367e-008
		0.11381224177455224 5.2441834636094873 1.4749757537448367e-008
		-0.12082109608583493 5.1813138611342504 1.4749757537448387e-008
		;
createNode transform -n "R_TLid_UppOrb_loc" -p "R_TLid_Ctrl";
	rename -uid "652E9B62-4F5E-BD9B-EBFD-C9BC8F29E12D";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0.35701781256769582 4.6148033053277233 3.7437783564454004e-005 ;
	setAttr ".s" -type "double3" 1.2436482061993619 1.2436482061993619 1.2436482061993619 ;
createNode transform -n "R_UppOrb_loc" -p "R_TLid_UppOrb_loc";
	rename -uid "7DCC6181-4876-5A61-B3F3-F288E0FADDED";
	setAttr ".t" -type "double3" -6.0397163055983716e-031 0.87676250980551984 0 ;
createNode locator -n "R_UppOrb_loc_Shape" -p "R_UppOrb_loc";
	rename -uid "9B55403B-40D1-F78D-D414-F08FF13CE39F";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode parentConstraint -n "R_TLid_Ctrl_Gro_parentConstraint1" -p "R_TLid_Ctrl_Gro";
	rename -uid "4AD7D191-4C71-AA3F-3EB6-8C85647A6E46";
	addAttr -ci true -k true -sn "w0" -ln "R_TLid_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 1.7763568394002505e-015 -1.4210854715202004e-014 
		-2.1175823681357508e-022 ;
	setAttr ".tg[0].tor" -type "double3" 3.3482102233306935e-030 2.853391132930927e-029 
		7.6148046557426831e-014 ;
	setAttr ".rst" -type "double3" 1.1102230246251563e-016 8.8817841970012523e-016 0 ;
	setAttr -k on ".w0";
createNode transform -n "R_Eyeball_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "BB84C36D-4A65-A1ED-0545-3B99D4D9AC11";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.028693581957627844 0.39591269156406123 -1.0658141036401512e-016 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".spt" -type "double3" -0.32997619251272137 -4.5529959529867012 1.2256862191861727e-015 ;
createNode transform -n "R_Eyeball_Ctrl" -p "R_Eyeball_Ctrl_Gro";
	rename -uid "6E39A8DE-45C7-AF54-C5D6-D6A35BFE3613";
	addAttr -ci true -sn "______________" -ln "______________" -min 0 -max 1 -en "Pupil:Pupil" 
		-at "enum";
	addAttr -ci true -sn "Pupil_Inn" -ln "Pupil_Inn" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Pupil_Out" -ln "Pupil_Out" -min -10 -max 10 -at "double";
	addAttr -ci true -sn "Bulge__FB" -ln "Bulge__FB" -min -10 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr -l on -k on ".______________";
	setAttr -k on ".Pupil_Inn";
	setAttr -k on ".Pupil_Out";
	setAttr -k on ".Bulge__FB";
createNode nurbsCurve -n "R_Eyeball_Ctrl_Shape" -p "R_Eyeball_Ctrl";
	rename -uid "26462B0C-4D07-3BCB-C343-F38904278E6A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.67849308085448912 5.2687319509349262 3.2860313478144585e-015
		0.35866977447034376 5.4012071020022399 3.2860313478144585e-015
		0.038846468086198738 5.2687319509349262 3.2860313478144585e-015
		-0.093628682981120481 4.948908644550766 3.2860313478144585e-015
		0.038846468086198738 4.6290853381666146 3.2860313478144585e-015
		0.35866977447034304 4.4966101870993072 3.2860313478144585e-015
		0.67849308085448912 4.6290853381666146 3.2860313478144585e-015
		0.81096823192180667 4.948908644550766 3.2860313478144585e-015
		0.67849308085448912 5.2687319509349262 3.2860313478144585e-015
		0.35866977447034376 5.4012071020022399 3.2860313478144585e-015
		0.038846468086198738 5.2687319509349262 3.2860313478144585e-015
		;
createNode transform -n "R_pupil_Inn_Ctrl_Gro" -p "R_Eyeball_Ctrl";
	rename -uid "62229A4C-49DE-B0ED-1B21-BB871DF7A3A8";
	setAttr ".t" -type "double3" 2.6645352591003757e-015 0 -2.6645352591003757e-014 ;
	setAttr ".r" -type "double3" 0 -1.2130227706871529e-015 -8.3861293423844699e-014 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1.0000000000000011 ;
	setAttr ".rp" -type "double3" 0.35866977447034903 4.9489086445507615 -1.332267629550189e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".spt" -type "double3" -5.5511151231257827e-017 -8.8817841970012504e-016 
		-1.5777218104420257e-030 ;
createNode transform -n "R_pupil_Inn_Ctrl" -p "R_pupil_Inn_Ctrl_Gro";
	rename -uid "D6EFD199-4D92-C1F3-0867-D889799ADBC2";
	setAttr -l on -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".mntl" -type "double3" -2 -2 -1 ;
	setAttr ".mxtl" -type "double3" 2 2 1 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "R_pupil_Inn_Ctrl_Shape" -p "R_pupil_Inn_Ctrl";
	rename -uid "8ABE7ABF-48A2-A3DF-A24F-3BABBB81F831";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.42063748581297233 5.0108763558933918 -2.8149235648364081e-015
		0.3586697744703482 5.0365442223607335 -2.8149235648364081e-015
		0.29670206312772446 5.0108763558933918 -2.8149235648364081e-015
		0.2710341966603883 4.9489086445507642 -2.8149235648364081e-015
		0.29670206312772446 4.8869409332081455 -2.8149235648364081e-015
		0.35866977447034792 4.8612730667408073 -2.8149235648364081e-015
		0.42063748581297233 4.8869409332081455 -2.8149235648364081e-015
		0.44630535228030799 4.9489086445507642 -2.8149235648364081e-015
		0.42063748581297233 5.0108763558933918 -2.8149235648364081e-015
		0.3586697744703482 5.0365442223607335 -2.8149235648364081e-015
		0.29670206312772446 5.0108763558933918 -2.8149235648364081e-015
		;
createNode transform -n "R_pupil_Out_Ctrl_Gro" -p "R_Eyeball_Ctrl";
	rename -uid "578D7B01-482F-0C55-69EC-A2B015D2306D";
	setAttr ".t" -type "double3" 8.8817841970012523e-016 0 -1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" 3.1805546814635176e-015 -3.975693351829398e-014 -1.8288189418415224e-014 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1.0000000000000004 ;
	setAttr ".rp" -type "double3" 0.35866977447034903 4.9489086445507615 -1.3322676295501882e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".spt" -type "double3" -5.5511151231257827e-017 -8.8817841970012504e-016 
		-5.9164567891576069e-031 ;
createNode transform -n "R_pupil_Out_Ctrl" -p "R_pupil_Out_Ctrl_Gro";
	rename -uid "464FC080-4E04-236F-EABA-2AA71AF58C06";
	setAttr -l on -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".sp" -type "double3" 0.35866977447034926 4.9489086445507624 -1.3322676295501878e-015 ;
	setAttr ".mntl" -type "double3" -2 -2 -1 ;
	setAttr ".mxtl" -type "double3" 2 2 1 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "R_pupil_Out_Ctrl_Shape" -p "R_pupil_Out_Ctrl";
	rename -uid "FF0CD2A3-41F0-9B46-9FF8-9BB02C4A765E";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.46311425446418919 5.0533531245446071 -2.9930606787438089e-015
		0.35866977447034759 5.09661544467306 -2.9930606787438089e-015
		0.25422529447650694 5.0533531245446071 -2.9930606787438089e-015
		0.21096297434805245 4.948908644550766 -2.9930606787438089e-015
		0.25422529447650694 4.8444641645569249 -2.9930606787438089e-015
		0.35866977447034742 4.8012018444284763 -2.9930606787438089e-015
		0.46311425446418919 4.8444641645569249 -2.9930606787438089e-015
		0.50637657459264263 4.948908644550766 -2.9930606787438089e-015
		0.46311425446418919 5.0533531245446071 -2.9930606787438089e-015
		0.35866977447034759 5.09661544467306 -2.9930606787438089e-015
		0.25422529447650694 5.0533531245446071 -2.9930606787438089e-015
		;
createNode parentConstraint -n "R_Eyeball_Ctrl_Gro_parentConstraint1" -p "R_Eyeball_Ctrl_Gro";
	rename -uid "F053AF57-4D0B-AB36-087B-E8A31854735B";
	addAttr -ci true -k true -sn "w0" -ln "R_Pupil_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -2.2204460492503131e-015 -2.1316282072803009e-014 
		7.8886090522101223e-030 ;
	setAttr ".tg[0].tor" -type "double3" 3.3482102233306935e-030 2.853391132930927e-029 
		7.6148046557426831e-014 ;
	setAttr ".rst" -type "double3" -2.2204460492503131e-016 -1.7763568394002505e-015 
		3.9443045261050739e-031 ;
	setAttr -k on ".w0";
createNode transform -n "R_UppOrb_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "48B0664B-4097-5BF2-7ECD-5BAE79DAE525";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
createNode transform -n "R_UppOrb_Ctrl" -p "R_UppOrb_Ctrl_Gro";
	rename -uid "C8BE59F6-4A87-83FE-6878-A7846BFFFF2F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "R_UppOrb_Ctrl_Shape" -p "R_UppOrb_Ctrl";
	rename -uid "2B5C9C68-4548-A448-7FCB-42B3E52D03FB";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		-0.36644984550366994 1.0618799737568336e-016 0
		-0.25911917072040769 -0.25911917072040752 0
		-5.5209245064404264e-017 -0.36644984550366994 0
		0.25911917072040747 -0.25911917072040763 0
		0.36644984550366994 -1.968209268663648e-016 0
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		;
createNode parentConstraint -n "R_UppOrb_Ctrl_Gro_parentConstraint1" -p "R_UppOrb_Ctrl_Gro";
	rename -uid "7A1B271F-4651-CE36-061A-CF9E4ECC498F";
	addAttr -ci true -k true -sn "w0" -ln "R_UppOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -8.7581154020301067e-047 -9.9920072216264089e-016 
		1.5407439555097894e-033 ;
	setAttr ".rst" -type "double3" -7.5112823494104648e-031 1.0903841225824855 -1.725908591320383e-017 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "R_UppOrb_Ctrl_Gro_scaleConstraint1" -p "R_UppOrb_Ctrl_Gro";
	rename -uid "1FA3B89E-45FE-F3BF-5703-3B95DE8E6EA3";
	addAttr -ci true -k true -sn "w0" -ln "R_UppOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0.4020429551601411 0.4020429551601411 0.4020429551601411 ;
	setAttr -k on ".w0";
createNode transform -n "R_lowOrb_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "EBBED2C7-4A41-00A8-1E9C-B497557B6F4B";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
createNode transform -n "R_lowOrb_Ctrl" -p "R_lowOrb_Ctrl_Gro";
	rename -uid "459E1063-4E81-F7A5-F82E-E9A4955D216D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "R_lowOrb_Ctrl_Shape" -p "R_lowOrb_Ctrl";
	rename -uid "869DCA29-4B3E-9842-4F4E-E38D6BF1BFAE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		-0.36644984550366994 1.0618799737568336e-016 0
		-0.25911917072040769 -0.25911917072040752 0
		-5.5209245064404264e-017 -0.36644984550366994 0
		0.25911917072040747 -0.25911917072040763 0
		0.36644984550366994 -1.968209268663648e-016 0
		0.25911917072040785 0.25911917072040747 0
		-2.09037728583476e-017 0.36644984550366994 0
		-0.25911917072040758 0.25911917072040758 0
		;
createNode parentConstraint -n "R_lowOrb_Ctrl_Gro_parentConstraint1" -p "R_lowOrb_Ctrl_Gro";
	rename -uid "4A20BD66-4FA1-F2F2-0FAF-F39A545205B7";
	addAttr -ci true -k true -sn "w0" -ln "R_lowOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -5.5511151231257827e-017 0.00024800897360144347 
		-6.7743473018927993e-021 ;
	setAttr ".rst" -type "double3" -7.5112823494104648e-031 -1.0906794768368409 -1.725908591320383e-017 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "R_lowOrb_Ctrl_Gro_scaleConstraint1" -p "R_lowOrb_Ctrl_Gro";
	rename -uid "BF78641E-4E53-628E-A9B4-7CBF78FDB9AC";
	addAttr -ci true -k true -sn "w0" -ln "R_lowOrb_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0.40204295516014094 -0.4019292604501607 0.4019292604501607 ;
	setAttr -k on ".w0";
createNode transform -n "R_EyeOutCorner_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "9420DAF6-4AB0-C8DF-7279-A98EDD0657C7";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.5 0.50000000000000011 0.5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.027350368745784344 0.2474454325081826 -6.9388939039072284e-017 ;
	setAttr ".sp" -type "double3" 0.54700737491569118 4.9489086501636601 -1.3877787807814457e-015 ;
	setAttr ".spt" -type "double3" -0.51965700616990673 -4.7014632176554771 1.3183898417423734e-015 ;
createNode transform -n "R_EyeOutCorner_Ctrl" -p "R_EyeOutCorner_Ctrl_Gro";
	rename -uid "14D47750-4E57-F972-843E-A3A65D1A6ED8";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.54700737491569118 4.9489086501636601 -1.3877787807814457e-015 ;
	setAttr ".sp" -type "double3" 0.54700737491569118 4.9489086501636601 -1.3877787807814457e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "R_EyeOutCorner_Ctrl_Shape" -p "R_EyeOutCorner_Ctrl";
	rename -uid "52B1BA94-442B-9C06-3086-449E87E0B9C7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.77430631539928629 5.3520222266514583 -5.9292714289677147e-016
		0.77430631539928541 5.352022226651445 -5.9292714289677147e-016
		0.22555813057075105 4.9816854909014383 -5.9292714289677147e-016
		0.22555813057075075 4.9489086501635287 -5.9292714289677147e-016
		0.22555813057075105 4.9161318094256057 -5.9292714289677147e-016
		0.77430631539928541 4.5457950736754444 -5.9292714289677147e-016
		0.77430631539928629 4.5457950736754622 -5.9292714289677147e-016
		0.86845661926061923 4.9489086501634247 -5.9292714289677147e-016
		0.77430631539928629 5.3520222266514583 -5.9292714289677147e-016
		0.77430631539928541 5.352022226651445 -5.9292714289677147e-016
		0.22555813057075105 4.9816854909014383 -5.9292714289677147e-016
		;
createNode parentConstraint -n "R_EyeOutCorner_Ctrl_Gro_parentConstraint1" -p "R_EyeOutCorner_Ctrl_Gro";
	rename -uid "EA57595C-4061-DB53-A9EA-228B7B855B0F";
	addAttr -ci true -k true -sn "w0" -ln "R_EyeOutCorner_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -3.5527136788005009e-015 -1.4210854715202004e-014 
		0 ;
	setAttr ".tg[0].tor" -type "double3" 3.3482102233306935e-030 2.853391132930927e-029 
		7.6148046557426831e-014 ;
	setAttr ".rst" -type "double3" -4.4408920985006262e-016 -1.7763568394002505e-015 
		-1.9721522630525365e-031 ;
	setAttr -k on ".w0";
createNode transform -n "R_EyeInnCorner_Ctrl_Gro" -p "R_Eye_Grp";
	rename -uid "7B24BDC3-4D48-E60D-C095-CFA652D16F0A";
	setAttr -l on -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.5 0.50000000000000011 0.5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.0085166087012503201 0.24744543250818257 -6.9388939039072284e-017 ;
	setAttr ".sp" -type "double3" 0.17033217402500719 4.9489086501636592 -1.3877787807814457e-015 ;
	setAttr ".spt" -type "double3" -0.16181556532375685 -4.7014632176554763 1.3183898417423734e-015 ;
createNode transform -n "R_EyeInnCorner_Ctrl" -p "R_EyeInnCorner_Ctrl_Gro";
	rename -uid "6B8E6E91-46F1-E322-C286-90895985903E";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.17033217402500719 4.9489086501636592 -1.3877787807814457e-015 ;
	setAttr ".sp" -type "double3" 0.17033217402500719 4.9489086501636592 -1.3877787807814457e-015 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "R_EyeInnCorner_Ctrl_Shape" -p "R_EyeInnCorner_Ctrl";
	rename -uid "F060B8F3-4F24-DBDE-AA95-35AE49731FAC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.49178141836995215 4.9816854909014436 -2.6277473358814545e-015
		-0.056966766458583659 5.3520222266514788 -2.6277473358814545e-015
		-0.056966766458583562 5.352022226651469 -2.6277473358814545e-015
		-0.15111707031993946 4.9489086501636486 -2.6277473358814501e-015
		-0.056966766458582743 4.5457950736754524 -2.6277473358814545e-015
		-0.056966766458582813 4.5457950736754524 -2.6277473358814545e-015
		0.49178141836995182 4.916131809425611 -2.6277473358814545e-015
		0.49178141836993466 4.9489086501636486 -2.6277473358814501e-015
		0.49178141836995215 4.9816854909014436 -2.6277473358814545e-015
		-0.056966766458583659 5.3520222266514788 -2.6277473358814545e-015
		-0.056966766458583562 5.352022226651469 -2.6277473358814545e-015
		;
createNode parentConstraint -n "R_EyeInnCorner_Ctrl_Gro_parentConstraint1" -p "R_EyeInnCorner_Ctrl_Gro";
	rename -uid "35755841-4B6E-B20B-C613-E1B294827C18";
	addAttr -ci true -k true -sn "w0" -ln "R_EyeInnCorner_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -1.1102230246251563e-015 -1.4210854715202004e-014 
		4.7331654313260708e-030 ;
	setAttr ".tg[0].tor" -type "double3" 3.3482102233306935e-030 2.853391132930927e-029 
		7.6148046557426831e-014 ;
	setAttr ".rst" -type "double3" -8.3266726846886741e-017 -8.8817841970012523e-016 
		3.9443045261050739e-031 ;
	setAttr -k on ".w0";
createNode transform -n "L_Face_Grp" -p "facial__Ctrl";
	rename -uid "71D4D254-4101-F1A8-6337-FA8642977E51";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 0.80408591032028209 0.80408591032028209 0.80408591032028209 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".Mili_Hide" yes;
createNode transform -n "L_Cheek_Ctrl_Gro" -p "L_Face_Grp";
	rename -uid "129760DC-4A95-ED5E-1FF6-698BC802BC67";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 12.820312087440591 5.2701233648477555 25.775370536656141 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 3 3 3 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Cheek_Ctrl" -p "L_Cheek_Ctrl_Gro";
	rename -uid "DC242E2D-4FDD-C18F-1970-699769D35C6F";
	addAttr -ci true -sn "______________" -ln "______________" -min 0 -max 1 -en "Dn_lid:Dn_lid" 
		-at "enum";
	addAttr -ci true -sn "lid_auto" -ln "lid_auto" -min 0 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr -l on -k on ".______________";
	setAttr -k on ".lid_auto";
createNode nurbsCurve -n "L_Cheek_Ctrl_Shape" -p "L_Cheek_Ctrl";
	rename -uid "B20DDD04-4296-DED8-08FB-10878F1913FD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		-0.25516975858324631 -2.6182807946170947e-015 -5.6659068233432321e-017
		-0.25129307598795503 0.044309738778055933 -6.5637010219446289e-017
		-0.23978092875892615 0.087273141073141977 -7.2620591724985442e-017
		-0.22098323500845057 0.12758524544241784 -7.7397750531031736e-017
		-0.19547180023219723 0.16401993491480621 -7.9823200304530852e-017
		-0.16401993491481082 0.19547180023219241 -7.9823200304530852e-017
		-0.12758524544242125 0.22098323500844613 -7.7397750531031736e-017
		-0.087273141073145516 0.23978092875892168 -7.2620591724985442e-017
		-0.044309738778059923 0.2512930759879507 -6.5637010219446301e-017
		-1.3739194777311664e-015 0.25516975858324176 -5.6659068233432321e-017
		0.044309738778057099 0.2512930759879507 -4.595953333683578e-017
		0.087273141073143295 0.23978092875892168 -3.3863531464679648e-017
		0.12758524544241881 0.22098323500844613 -2.0738519693981118e-017
		0.16401993491480846 0.19547180023219241 -6.9837170085543817e-018
		0.19547180023219457 0.16401993491480621 6.9837170085543601e-018
		0.22098323500844819 0.12758524544241784 2.0738519693981088e-017
		0.23978092875892373 0.087273141073141977 3.3863531464679641e-017
		0.25129307598795253 0.044309738778055933 4.595953333683578e-017
		0.25516975858324392 -2.6182807946170947e-015 5.6659068233432321e-017
		0.25129307598795253 -0.044309738778061034 6.5637010219446289e-017
		0.23978092875892373 -0.087273141073146848 7.2620591724985442e-017
		0.22098323500844819 -0.1275852454424227 7.7397750531031736e-017
		0.19547180023219457 -0.16401993491481279 7.9823200304530852e-017
		0.16401993491480846 -0.19547180023219923 7.9823200304530852e-017
		0.12758524544241881 -0.22098323500845249 7.7397750531031736e-017
		0.087273141073143295 -0.23978092875892787 7.2620591724985442e-017
		0.044309738778057099 -0.25129307598795736 6.5637010219446301e-017
		-1.3739194777311664e-015 -0.25516975858324836 5.6659068233432321e-017
		-0.044309738778059923 -0.25129307598795736 4.595953333683578e-017
		-0.087273141073145516 -0.23978092875892787 3.3863531464679641e-017
		-0.12758524544242125 -0.22098323500845249 2.0738519693981097e-017
		-0.16401993491481082 -0.19547180023219923 6.9837170085543724e-018
		-0.19547180023219723 -0.16401993491481279 -6.9837170085543632e-018
		-0.22098323500845057 -0.1275852454424227 -2.0738519693981088e-017
		-0.23978092875892615 -0.087273141073146848 -3.3863531464679641e-017
		-0.25129307598795503 -0.044309738778061034 -4.595953333683578e-017
		-0.25516975858324631 -2.6182807946170947e-015 -5.6659068233432321e-017
		;
createNode transform -n "L_Puffer_Ctrl_Gro" -p "L_Face_Grp";
	rename -uid "F64753BD-4F25-B278-0269-A48E89FC206F";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 16.263353094322341 -0.9226509569130138 24.093333709557299 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 45.680626494992346 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 3 3 3 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Puffer_Ctrl" -p "L_Puffer_Ctrl_Gro";
	rename -uid "105020A5-4607-A6C4-FDA2-ABA4A35F5024";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "L_Puffer_Ctrl_Shape" -p "L_Puffer_Ctrl";
	rename -uid "29DDC923-478A-D0F7-16CE-C88FF71F51DA";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.39182306297605529 2.4048106414094419e-014 -9.1602139351487609e-015
		-0.3858702664647975 0.068039322779033851 -9.1602139351487609e-015
		-0.36819291780971464 0.13401129366068881 -9.1602139351487609e-015
		-0.33932832984642608 0.19591209372680152 -9.1602139351487609e-015
		-0.3001545320952938 0.25185897280414915 -9.1602139351487609e-015
		-0.25185897280413261 0.30015453209531051 -9.1602139351487609e-015
		-0.19591209372678503 0.3393283298464424 -9.1602139351487609e-015
		-0.13401129366067246 0.3681929178097314 -9.1602139351487609e-015
		-0.068039322779017544 0.3858702664648142 -9.1602139351487609e-015
		-7.6821797541486816e-015 0.39182306297607278 -9.1602139351487609e-015
		0.06803932277900207 0.3858702664648142 -9.1602139351487609e-015
		0.13401129366065667 0.3681929178097314 -9.1602139351487609e-015
		0.19591209372676976 0.3393283298464424 -9.1602139351487609e-015
		0.25185897280411695 0.30015453209531051 -9.1602139351487609e-015
		0.30015453209527854 0.25185897280414915 -9.1602139351487609e-015
		0.33932832984641031 0.19591209372680152 -9.1602139351487609e-015
		0.36819291780969832 0.13401129366068881 -9.1602139351487609e-015
		0.38587026646478118 0.068039322779033851 -9.1602139351487609e-015
		0.39182306297604014 2.4048106414094419e-014 -9.1602139351487609e-015
		0.38587026646478118 -0.068039322778985722 -9.1602139351487609e-015
		0.36819291780969832 -0.13401129366064038 -9.1602139351487609e-015
		0.33932832984641031 -0.19591209372675333 -9.1602139351487609e-015
		0.30015453209527854 -0.25185897280409997 -9.1602139351487609e-015
		0.25185897280411695 -0.30015453209526177 -9.1602139351487609e-015
		0.19591209372676976 -0.33932832984639377 -9.1602139351487609e-015
		0.13401129366065667 -0.36819291780968222 -9.1602139351487609e-015
		0.06803932277900207 -0.38587026646476463 -9.1602139351487609e-015
		-7.6821797541486816e-015 -0.39182306297602321 -9.1602139351487609e-015
		-0.068039322779017544 -0.38587026646476463 -9.1602139351487609e-015
		-0.13401129366067246 -0.36819291780968222 -9.1602139351487609e-015
		-0.19591209372678503 -0.33932832984639377 -9.1602139351487609e-015
		-0.25185897280413261 -0.30015453209526177 -9.1602139351487609e-015
		-0.3001545320952938 -0.25185897280409997 -9.1602139351487609e-015
		-0.33932832984642608 -0.19591209372675333 -9.1602139351487609e-015
		-0.36819291780971464 -0.13401129366064038 -9.1602139351487609e-015
		-0.3858702664647975 -0.068039322778985722 -9.1602139351487609e-015
		-0.39182306297605529 2.4048106414094419e-014 -9.1602139351487609e-015
		0.39182306297604014 2.4048106414094419e-014 -9.1602139351487609e-015
		;
createNode transform -n "R_Face_Grp" -p "facial__Ctrl";
	rename -uid "169099F1-4EBE-3BA2-ABF2-27AA30BC5634";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 0.80408591032028209 0.80408591032028209 0.80408591032028209 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".Mili_Hide" yes;
createNode transform -n "R_Cheek_Ctrl_Gro" -p "R_Face_Grp";
	rename -uid "1005D7C5-4E50-D72A-E955-5CB7CBFA113E";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -12.820316189381938 5.2702678903263021 25.775268360873632 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -3 3 3 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Cheek_Ctrl" -p "R_Cheek_Ctrl_Gro";
	rename -uid "936543C9-4BEB-A749-475F-598C63D36BD1";
	addAttr -ci true -sn "______________" -ln "______________" -min 0 -max 1 -en "Dn_lid:Dn_lid" 
		-at "enum";
	addAttr -ci true -sn "lid_auto" -ln "lid_auto" -min 0 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr -l on -k on ".______________";
	setAttr -k on ".lid_auto";
createNode nurbsCurve -n "R_Cheek_Ctrl_Shape" -p "R_Cheek_Ctrl";
	rename -uid "E1E50444-4571-AAF2-26DF-4FBFA2BCB670";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		-0.2551697585832437 -2.6318310961517608e-015 -5.0307844851880913e-015
		-0.25129307598795242 0.044309738778055933 -5.0397624271741109e-015
		-0.23978092875892351 0.087273141073141977 -5.0467460086796418e-015
		-0.22098323500844799 0.12758524544241773 -5.0515231674856935e-015
		-0.19547180023219443 0.16401993491480615 -5.053948617259193e-015
		-0.16401993491480818 0.19547180023219241 -5.053948617259193e-015
		-0.12758524544241859 0.22098323500844613 -5.0515231674856935e-015
		-0.087273141073143101 0.2397809287589216 -5.0467460086796418e-015
		-0.044309738778057141 0.2512930759879507 -5.0397624271741109e-015
		1.4255911639855152e-015 0.25516975858324176 -5.0307844851880913e-015
		0.044309738778059847 0.2512930759879507 -5.0200849502915031e-015
		0.087273141073145696 0.2397809287589216 -5.0079889484193457e-015
		0.12758524544242139 0.22098323500844613 -4.9948639366486453e-015
		0.16401993491481098 0.19547180023219241 -4.9811091339632186e-015
		0.19547180023219732 0.16401993491480615 -4.9671416999461091e-015
		0.22098323500845063 0.12758524544241773 -4.9533868972606817e-015
		0.23978092875892623 0.087273141073141977 -4.9402618854899804e-015
		0.25129307598795536 0.044309738778055933 -4.9281658836178223e-015
		0.25516975858324653 -2.6318310961517608e-015 -4.9174663487212325e-015
		0.25129307598795536 -0.044309738778061054 -4.9084884067352208e-015
		0.23978092875892623 -0.087273141073146848 -4.901504825229682e-015
		0.22098323500845063 -0.1275852454424227 -4.8967276664236319e-015
		0.19547180023219732 -0.16401993491481279 -4.894302216650134e-015
		0.16401993491481098 -0.19547180023219923 -4.894302216650134e-015
		0.12758524544242139 -0.22098323500845249 -4.8967276664236319e-015
		0.087273141073145696 -0.23978092875892787 -4.901504825229682e-015
		0.044309738778059847 -0.25129307598795736 -4.9084884067352208e-015
		1.4255911639855152e-015 -0.25516975858324836 -4.9174663487212325e-015
		-0.044309738778057141 -0.25129307598795736 -4.9281658836178223e-015
		-0.087273141073143101 -0.23978092875892787 -4.9402618854899804e-015
		-0.12758524544241859 -0.22098323500845249 -4.9533868972606817e-015
		-0.16401993491480818 -0.19547180023219923 -4.9671416999461091e-015
		-0.19547180023219443 -0.16401993491481279 -4.9811091339632186e-015
		-0.22098323500844799 -0.1275852454424227 -4.9948639366486453e-015
		-0.23978092875892351 -0.087273141073146848 -5.0079889484193457e-015
		-0.25129307598795242 -0.044309738778061054 -5.0200849502915031e-015
		-0.2551697585832437 -2.6318310961517608e-015 -5.0307844851880913e-015
		;
createNode transform -n "R_Puffer_Ctrl_Gro" -p "R_Face_Grp";
	rename -uid "CAFAAE88-49D4-8BB3-8682-AC9EDE14537B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -16.263339990880073 -0.92264168380623701 24.093298236217471 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -45.680625915527344 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -3 3 3 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Puffer_Ctrl" -p "R_Puffer_Ctrl_Gro";
	rename -uid "B840AACD-485E-FE98-C6F9-F785AE9100AA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "R_Puffer_Ctrl_Shape" -p "R_Puffer_Ctrl";
	rename -uid "44B42E57-4A7B-330B-3489-329E7DF37A96";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.39182306297604591 4.9502234028272742e-014 -3.5221146215673841e-015
		-0.385870266464788 0.06803932277905933 -3.5221146215673841e-015
		-0.36819291780970526 0.13401129366071421 -3.5221146215673841e-015
		-0.33932832984641687 0.19591209372682741 -3.5221146215673841e-015
		-0.30015453209528503 0.25185897280417435 -3.5221146215673841e-015
		-0.25185897280412362 0.30015453209533616 -3.5221146215673841e-015
		-0.19591209372677615 0.33932832984646821 -3.5221146215673841e-015
		-0.13401129366066344 0.36819291780975655 -3.5221146215673841e-015
		-0.068039322779008912 0.38587026646483918 -3.5221146215673841e-015
		8.780181716070166e-016 0.39182306297609798 -3.5221146215673841e-015
		0.068039322779010689 0.38587026646483918 -3.5221146215673841e-015
		0.13401129366066578 0.36819291780975655 -3.5221146215673841e-015
		0.19591209372677823 0.33932832984646821 -3.5221146215673841e-015
		0.25185897280412578 0.30015453209533616 -3.5221146215673841e-015
		0.30015453209528736 0.25185897280417435 -3.5221146215673841e-015
		0.33932832984641942 0.19591209372682741 -3.5221146215673841e-015
		0.36819291780970737 0.13401129366071421 -3.5221146215673841e-015
		0.38587026646479033 0.06803932277905933 -3.5221146215673841e-015
		0.3918230629760483 4.9502234028272742e-014 -3.5221146215673841e-015
		0.38587026646479033 -0.068039322778960271 -3.5221146215673841e-015
		0.36819291780970737 -0.13401129366061493 -3.5221146215673841e-015
		0.33932832984641942 -0.19591209372672752 -3.5221146215673841e-015
		0.30015453209528736 -0.25185897280407488 -3.5221146215673841e-015
		0.25185897280412578 -0.30015453209523602 -3.5221146215673841e-015
		0.19591209372677823 -0.3393283298463684 -3.5221146215673841e-015
		0.13401129366066578 -0.36819291780965674 -3.5221146215673841e-015
		0.068039322779010689 -0.38587026646473954 -3.5221146215673841e-015
		8.780181716070166e-016 -0.39182306297599784 -3.5221146215673841e-015
		-0.068039322779008912 -0.38587026646473954 -3.5221146215673841e-015
		-0.13401129366066344 -0.36819291780965674 -3.5221146215673841e-015
		-0.19591209372677615 -0.3393283298463684 -3.5221146215673841e-015
		-0.25185897280412362 -0.30015453209523602 -3.5221146215673841e-015
		-0.30015453209528503 -0.25185897280407488 -3.5221146215673841e-015
		-0.33932832984641687 -0.19591209372672752 -3.5221146215673841e-015
		-0.36819291780970526 -0.13401129366061493 -3.5221146215673841e-015
		-0.385870266464788 -0.068039322778960271 -3.5221146215673841e-015
		-0.39182306297604591 4.9502234028272742e-014 -3.5221146215673841e-015
		0.3918230629760483 4.9502234028272742e-014 -3.5221146215673841e-015
		;
createNode transform -n "L_Ear_Grp" -p "facial__Ctrl";
	rename -uid "7D74CCE4-4D6A-4AF4-5334-AB85C72C83DC";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" 5.6194987275667261 17.524904895489435 6.4826445263829129 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 0 -60.664486583495233 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Ear_Ctrl_Gro" -p "L_Ear_Grp";
	rename -uid "AF42B08D-4570-0F74-C922-2F90082FCBBE";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 7.1054273576010003e-015 1.1102230246251538e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Ear_Ctrl" -p "L_Ear_Ctrl_Gro";
	rename -uid "28478FC4-4E0D-A156-3608-8987A10DF3F4";
createNode nurbsCurve -n "L_Ear_Ctrl_Shape" -p "L_Ear_Ctrl";
	rename -uid "9EC5419E-4A98-CFAB-0BF7-1892D4201EE5";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		-5.7703962179435688 4.4209365039620572 5.6956718348009012e-015
		-5.6815448327452494 4.4347303221987691 -1.0277195269131891
		-5.4176928916168645 4.4756922690407031 -2.0242121422826949
		-4.986860320930715 4.5425772833511875 -2.9592105867281178
		-4.402152581117349 4.6333507953969182 -3.8042763185607567
		-3.6812935136468647 4.7452612504649281 -4.5337704892762858
		-2.8462309184206029 4.8749013413775213 -5.1254823883342695
		-1.9223001540552436 5.0183378561657559 -5.5614758620277875
		-0.93760313207369439 5.1712080867099317 -5.8284884608434586
		0.0779511650431568 5.3288687844319167 -5.9184041884621967
		1.0935054621600075 5.4865294821539123 -5.8284884608434586
		2.0782024841415518 5.6393997126980775 -5.5614758620277875
		3.0021332485069037 5.7828362274863121 -5.1254823883342695
		3.8371958437331632 5.9124763183989071 -4.5337704892762858
		4.5580549112036595 6.0243867734669259 -3.8042763185607567
		5.1427626510170592 6.1151602855126495 -2.9592105867281178
		5.5735952217031812 6.182045299823141 -2.0242121422826949
		5.8374471628315572 6.2230072466650679 -1.0277195269131891
		5.9262985480298829 6.2368010649017709 5.6956718348009012e-015
		5.8374471628315572 6.2230072466650679 1.027719526913198
		5.5735952217031812 6.1820452998231392 2.0242121422827006
		5.1427626510170592 6.1151602855126477 2.9592105867281204
		4.5580549112036595 6.0243867734669241 3.8042763185607682
		3.8371958437331632 5.9124763183989053 4.5337704892763044
		3.002133248506905 5.7828362274863103 5.1254823883342748
		2.0782024841415518 5.6393997126980722 5.5614758620277938
		1.0935054621600082 5.4865294821539088 5.8284884608434675
		0.077951165043157467 5.3288687844319131 5.918404188462203
		-0.93760313207369317 5.1712080867099282 5.8284884608434675
		-1.9223001540552436 5.0183378561657541 5.5614758620277938
		-2.8462309184206012 4.8749013413775177 5.1254823883342748
		-3.6812935136468647 4.7452612504649245 4.5337704892763044
		-4.4021525811173507 4.6333507953969146 3.8042763185607682
		-4.986860320930715 4.5425772833511857 2.9592105867281204
		-5.4176928916168663 4.4756922690407013 2.0242121422827006
		-5.6815448327452494 4.4347303221987673 1.027719526913198
		-5.7703962179435688 4.4209365039620572 5.6956718348009012e-015
		;
createNode transform -n "R_Ear_Grp" -p "facial__Ctrl";
	rename -uid "ABFDB066-44A6-BCF2-0138-3AAA829C43F3";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" -5.6195041055274908 17.524921380140263 6.4826444541822461 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 180 0 60.664486583495247 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Ear_Ctrl_Gro" -p "R_Ear_Grp";
	rename -uid "EEEE9DDE-4028-8891-6F03-018A3628D405";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -8.8817841970012523e-016 0 -5.5511151231257827e-017 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -1.557197801369239e-012 4.0403471501813624e-012 6.3611093628723757e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Ear_Ctrl" -p "R_Ear_Ctrl_Gro";
	rename -uid "95175BFC-48A6-A39B-9E1A-A5AFB5B0A42C";
createNode nurbsCurve -n "R_Ear_Ctrl_Shape" -p "R_Ear_Ctrl";
	rename -uid "73E56244-459E-592E-B7E8-A591FE0B9690";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		5.7704063443258855 -4.4208952038989633 1.1210366393584309e-006
		5.6815549591275669 -4.4346890221356734 -1.0277184058765545
		5.417703017999199 -4.4756509689776003 -2.0242110212460558
		4.9868704473130521 -4.5425359832880901 -2.9592094656914822
		4.4021627074996568 -4.6333094953338154 -3.8042751975241273
		3.6813036400291592 -4.7452199504018324 -4.5337693682396552
		2.8462410448029054 -4.8748600413144274 -5.1254812672976318
		1.9223102804375567 -5.018296556102662 -5.5614747409911489
		0.93761325845600485 -5.1711667866468325 -5.8284873398068129
		-0.077941038660847617 -5.3288274843688193 -5.9184030674255661
		-1.0934953357776938 -5.4864881820908167 -5.8284873398068129
		-2.0781923577592374 -5.6393584126349783 -5.5614747409911489
		-3.0021231221246101 -5.7827949274232182 -5.1254812672976318
		-3.8371857173508626 -5.9124350183358132 -4.5337693682396552
		-4.5580447848213508 -6.0243454734038178 -3.8042751975241273
		-5.1427525246347541 -6.1151189854495502 -2.9592094656914822
		-5.5735850953208859 -6.1820039997600329 -2.0242110212460558
		-5.8374370364492503 -6.2229659466019758 -1.0277184058765545
		-5.9262884216475724 -6.2367597648386734 1.1210366393584309e-006
		-5.8374370364492503 -6.2229659466019758 1.0277206479498393
		-5.5735850953208859 -6.1820039997600329 2.0242132633193437
		-5.1427525246347541 -6.1151189854495502 2.9592117077647604
		-4.5580447848213508 -6.0243454734038178 3.8042774395973953
		-3.8371857173508626 -5.9124350183358132 4.5337716103129386
		-3.0021231221246105 -5.7827949274232147 5.125483509370909
		-2.0781923577592383 -5.6393584126349783 5.5614769830644253
		-1.0934953357776944 -5.4864881820908149 5.8284895818801079
		-0.077941038660848269 -5.3288274843688175 5.9184053094988345
		0.93761325845600452 -5.1711667866468272 5.8284895818801079
		1.9223102804375551 -5.0182965561026585 5.5614769830644253
		2.8462410448029054 -4.8748600413144256 5.125483509370909
		3.6813036400291592 -4.7452199504018324 4.5337716103129386
		4.4021627074996568 -4.6333094953338154 3.8042774395973953
		4.9868704473130521 -4.5425359832880901 2.9592117077647604
		5.417703017999199 -4.4756509689776003 2.0242132633193437
		5.6815549591275669 -4.4346890221356734 1.0277206479498393
		5.7704063443258855 -4.4208952038989633 1.1210366393584309e-006
		;
createNode transform -n "C_palate_Grp" -p "facial__Ctrl";
	rename -uid "3B1FF518-42BA-2B39-42BE-2099FA560834";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Jaw_Main_Ctrl_Grp" -p "C_palate_Grp";
	rename -uid "DF9BDD00-4E8C-1BB9-0CB3-31A812A021D8";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.7131028289272445e-029 1.1526162922803458 5.5595019937145764 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Jaw_Main_Ctrl_Gro" -p "Jaw_Main_Ctrl_Grp";
	rename -uid "A2E31084-4606-9815-AF52-318CA3C534E0";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Jaw_Main_Ctrl" -p "Jaw_Main_Ctrl_Gro";
	rename -uid "4A6AD4C5-495B-160B-9584-DDBBD23389B9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Jaw_Main_Ctrl_Shape" -p "Jaw_Main_Ctrl";
	rename -uid "2D82996E-4788-2563-F8D6-CA9C765FD6AF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 29;
	setAttr ".cc" -type "nurbsCurve" 
		3 20 2 no 3
		25 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
		23
		5.8575729159755383 -3.5879978292257348 -15.173784411076996
		-1.1682290179606402e-015 -3.5879978292257348 -16.101532819033974
		-5.8575729159755285 -3.5879978292257348 -15.173784411077021
		-11.141765782825075 -3.5879978292257348 -12.481353665380247
		-15.335324985604766 -3.5879978292257348 -8.2877944626005409
		-18.027755731301554 -3.5879978292257357 -3.0036015957510074
		-18.95550413925849 -3.5879978292257366 2.8539713202245149
		-18.027755731301554 -3.5879978292257366 8.7115442362000515
		-15.335324985604752 -3.5879978292257375 13.995737103049576
		-11.141765782825081 -3.5879978292257375 18.189296305829263
		-5.8575729159755365 -3.5879978292257375 20.881727051526088
		-1.0173277251340127e-014 -3.5879978292257375 21.809475459483025
		5.857572915975517 -3.5879978292257375 20.881727051526088
		11.141765782825059 -3.5879978292257375 18.189296305829263
		15.335324985604748 -3.5879978292257375 13.995737103049596
		18.027755731301532 -3.5879978292257366 8.7115442362000639
		18.95550413925849 -3.5879978292257366 2.8539713202245283
		18.027755731301532 -3.5879978292257357 -3.0036015957509896
		15.335324985604766 -3.5879978292257348 -8.2877944626005231
		11.141765782825075 -3.5879978292257348 -12.481353665380237
		5.8575729159755383 -3.5879978292257348 -15.173784411076996
		-1.1682290179606402e-015 -3.5879978292257348 -16.101532819033974
		-5.8575729159755285 -3.5879978292257348 -15.173784411077021
		;
createNode transform -n "palate_Main_Ctrl_Grp" -p "C_palate_Grp";
	rename -uid "6C63910B-483A-83E3-4046-279624F436B8";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.8330379277131641e-029 1.5014641958682873 5.55950199371458 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "palate_Main_Ctrl_Gro" -p "palate_Main_Ctrl_Grp";
	rename -uid "BEB093BD-4CC5-B72E-96A2-62ABCCE13D31";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "palate_Main_Ctrl" -p "palate_Main_Ctrl_Gro";
	rename -uid "A8A43AEA-4198-7369-CA1A-5087F9DAB26E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "palate_Main_Ctrl_Shape" -p "palate_Main_Ctrl";
	rename -uid "2684D698-450D-DCDC-FF80-0E8BB5C7E0D3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 29;
	setAttr ".cc" -type "nurbsCurve" 
		3 20 2 no 3
		25 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
		23
		6.6103626120502978 0.43762815026398411 -16.766158783137179
		-1.318364710676954e-015 0.43762815026398422 -17.813137365789061
		-6.6103626120502712 0.43762815026398411 -16.766158783137222
		-12.573656874528549 0.43762815026398394 -13.727708593580466
		-17.306153996309167 0.4376281502639835 -8.995211471799843
		-20.344604185865972 0.43762815026398322 -3.0319172093215689
		-21.3915827685178 0.43762815026398277 3.5784454027287036
		-20.344604185865972 0.4376281502639825 10.188808014778989
		-17.306153996309167 0.43762815026398222 16.15210227725726
		-12.573656874528552 0.43762815026398194 20.884599399037889
		-6.6103626120502845 0.43762815026398166 23.923049588594651
		-1.1480702425550708e-014 0.43762815026398161 24.970028171246508
		6.6103626120502579 0.43762815026398166 23.923049588594651
		12.573656874528528 0.43762815026398194 20.884599399037889
		17.306153996309167 0.43762815026398222 16.152102277257271
		20.344604185865972 0.4376281502639825 10.188808014778996
		21.3915827685178 0.43762815026398277 3.5784454027287187
		20.344604185865972 0.43762815026398322 -3.0319172093215494
		17.306153996309167 0.4376281502639835 -8.9952114717998164
		12.573656874528549 0.43762815026398394 -13.727708593580466
		6.6103626120502978 0.43762815026398411 -16.766158783137179
		-1.318364710676954e-015 0.43762815026398422 -17.813137365789061
		-6.6103626120502712 0.43762815026398411 -16.766158783137222
		;
createNode transform -n "C_teeth_Grp" -p "facial__Ctrl";
	rename -uid "7D0FE821-49D3-D763-16C7-A8A0E3F499DB";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Upper_teeth_Ctrl_Grp" -p "C_teeth_Grp";
	rename -uid "8B063603-4940-D717-DC14-F3AA4FB52C73";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.8330379277131641e-029 1.5014641958682979 20.880200116970997 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0 -6.9388939039072296e-017 ;
	setAttr ".sp" -type "double3" 0 0 -6.9388939039072296e-017 ;
createNode transform -n "Upper_teeth_Ctrl_Gro" -p "Upper_teeth_Ctrl_Grp";
	rename -uid "12A58F76-4CBF-5A04-57E6-B7A73234DE8F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.5884498452564457e-030 0 -6.9388939039072296e-017 ;
	setAttr ".sp" -type "double3" 2.5884498452564457e-030 0 -6.9388939039072296e-017 ;
createNode transform -n "Upper_teeth_Ctrl" -p "Upper_teeth_Ctrl_Gro";
	rename -uid "670CC9E5-491A-CD3B-0753-3B919FDD5E99";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.5884498452564453e-030 0 0 ;
	setAttr ".sp" -type "double3" 2.5884498452564453e-030 0 0 ;
createNode nurbsCurve -n "Upper_teeth_Ctrl_Shape" -p "Upper_teeth_Ctrl";
	rename -uid "F7E120FA-4AA4-C11A-1A0B-22B118E999D9";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 40 2 no 3
		41 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41
		41
		-5.7369879375095314 -2.4100190835002957 -2.5144472387741921
		-5.4070635513441605 -2.4100190835002984 -1.61098462863199
		-4.991866685277123 -2.4100190835002984 -0.76792986597448387
		-4.4979450088181796 -2.4100190835002984 0.0014213338774280368
		-3.9330881017752009 -2.4100190835002984 0.68493580178349589
		-3.3062040271058084 -2.4100190835002984 1.2718346002060534
		-2.6271792189914671 -2.4100190835003024 1.7528613955401098
		-1.9067220881771187 -2.410019083500317 2.1204306257638184
		-1.1561949680687409 -2.410019083500317 2.3687451020352031
		-0.38743392416301325 -2.410019083500317 2.4938887429908285
		0.3874371153779661 -2.410019083500317 2.4938882249221255
		1.1561979833899567 -2.410019083500317 2.3687435478290726
		1.9067249024769213 -2.410019083500317 2.1204285534889911
		2.6271816312484426 -2.4100190835003024 1.752858805196571
		3.306206037319952 -2.4100190835002984 1.2718314917938034
		3.9330897099465161 -2.4100190835002984 0.68493269337124829
		4.497946214946662 -2.4100190835002984 0.0014182254651806045
		4.9918674893627868 -2.4100190835002984 -0.76793245631802365
		5.407063953386988 -2.4100190835002984 -1.6109867009068226
		5.7369879375095332 -2.4100190835002957 -2.514449052014669
		4.1691153852756093 -2.4100190835002802 -3.3143606068799958
		3.9293571443239914 -2.4100190835002926 -2.6578072116388531
		3.6276304339989518 -2.4100190835002984 -2.0451526274004346
		3.2686938332221094 -2.4100190835002984 -1.4860590946024064
		2.8582081050228898 -2.4100190835002984 -0.98934362458542047
		2.4026467420091224 -2.4100190835002984 -0.56283993428242907
		1.909194249531375 -2.4100190835002984 -0.21327359166007212
		1.3856325685837902 -2.4100190835002984 0.053842116091618986
		0.84021860350738331 -2.4100190835002984 0.23429477230827919
		0.28155385960279694 -2.4100190835002984 0.32523810750841364
		-0.28155114581370233 -2.4100190835002984 0.32523862557712291
		-0.8402159399736423 -2.4100190835002984 0.23429580844569187
		-1.3856300558161103 -2.4100190835002984 0.053843670297743562
		-1.909192038295819 -2.4100190835002984 -0.21327151938523897
		-2.4026449328163917 -2.4100190835002984 -0.56283786200759689
		-2.858206697872987 -2.4100190835002984 -0.98934155231058907
		-3.2686928281150358 -2.4100190835002984 -1.4860572813619275
		-3.6276296299132911 -2.4100190835002984 -2.045151073194309
		-3.9293563402383298 -2.4100190835002926 -2.6578056574327307
		-4.1691149832327836 -2.4100190835002802 -3.3143590526738711
		-5.7369879375095314 -2.4100190835002957 -2.5144472387741921
		;
createNode transform -n "lower_teeth_Ctrl_Grp" -p "C_teeth_Grp";
	rename -uid "2E99DCF0-4614-72BD-1642-E2BC4CC41CB4";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.8330379277131641e-029 -3.900127815116349 18.742592590035883 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 22.528671177099294 0 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -2.775557561562892e-017 -1.387778780781446e-017 ;
	setAttr ".sp" -type "double3" 0 -2.775557561562892e-017 -1.387778780781446e-017 ;
createNode transform -n "lower_teeth_Ctrl_Gro" -p "lower_teeth_Ctrl_Grp";
	rename -uid "3130DB11-4495-D144-817D-E8BABD1DACC8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.1993509878592001e-030 -0.3838857779585112 -14.112998703150524 ;
	setAttr ".sp" -type "double3" -1.1993509878592001e-030 -0.3838857779585112 -14.112998703150524 ;
createNode transform -n "lower_teeth_Ctrl" -p "lower_teeth_Ctrl_Gro";
	rename -uid "F5A1E9C2-49B8-CC8E-5585-09B75DC6731F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.6154135697744781e-031 0 0 ;
	setAttr ".sp" -type "double3" 2.6154135697744781e-031 0 0 ;
createNode nurbsCurve -n "lower_teeth_Ctrl_Shape" -p "lower_teeth_Ctrl";
	rename -uid "95D1689E-43E0-C350-9642-C0B923A30A3B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 40 2 no 3
		41 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41
		41
		-5.8760701108747853 2.2740135263601537 -1.0311625319842848
		-5.5538435736348237 2.279019271814684 -0.272958988765929
		-5.1483341477307913 2.2836903201776373 0.43454910398560487
		-4.6659367313926392 2.2879530049067718 1.0802037211868627
		-4.1142591566973969 2.2917401006896183 1.6538224693117205
		-3.502001642242722 2.2949918855000733 2.1463594525572547
		-2.8388199503351768 2.2976570734859627 2.5500465742056506
		-2.1351726413551666 2.2996936359100881 2.858517881822682
		-1.4021569409153067 2.3010694527363031 3.0669082608243472
		-0.65133275352543141 2.3017628264352745 3.1719312589192792
		0.10545887009727502 2.3017628235648515 3.171930824145861
		0.85628288569739297 2.3010694441250337 3.0669069565040865
		1.5892983898061024 2.2996936244283961 2.858516142728996
		2.2929453061238076 2.2976570591338463 2.5500444003385421
		2.9561266053690565 2.2949918682775339 2.1463568439167271
		3.5683837271614296 2.2917400834670794 1.6538198606711938
		4.120060909194379 2.2879529876842328 1.0802011125463349
		4.6024579328702231 2.2836903058255213 0.43454693011849871
		5.0079669661119635 2.2790192603329902 -0.27296072785961328
		5.3301931106896205 2.2740135163136705 -1.0311640536912603
		3.7989024134124594 2.2695815081875534 -1.7024655202397647
		3.5647382503612848 2.2732192228389301 -1.1514730331178813
		3.2700514762466018 2.2766137107411653 -0.63732128923395237
		2.91948964206005 2.2797114370654694 -0.16811903028135242
		2.518581432996176 2.2824635500785817 0.24873433488333663
		2.0736493010904669 2.2848266461105688 0.60666459735710376
		1.5917101216572973 2.2867634613268217 0.90002752858503487
		1.0803642661899495 2.2882434486831347 1.1241962698179808
		0.54767598760724634 2.2892432687680779 1.2756356783676035
		0.0020460995025484152 2.289747151476325 1.3519571090574511
		-0.54792044921718741 2.2897471543467476 1.3519575438308729
		-1.0935503864046732 2.2892432745089231 1.2756365479144467
		-1.6262388122357383 2.2882434572944046 1.1241975741382433
		-2.1375849621998162 2.2867634728085147 0.90002926767871905
		-2.6195245342952873 2.2848266575922604 0.60666633645078905
		-3.0644570588632947 2.2824635615602742 0.24873607397702224
		-3.4653656605894696 2.2797114471119513 -0.16811750857437863
		-3.8159276911071638 2.2766137193524361 -0.63731998491368858
		-4.1106144652218468 2.2732192314501991 -1.1514717287976182
		-4.3447790209353165 2.269581516798822 -1.7024642159194996
		-5.8760701108747853 2.2740135263601537 -1.0311625319842848
		;
createNode transform -n "Deform_Ctrl_Grp" -p "facial__Ctrl";
	rename -uid "27DBE778-4FFD-6526-EB0C-6EB9EEB8F012";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
createNode transform -n "Jaw_Deform_Ctrl_Gro" -p "Deform_Ctrl_Grp";
	rename -uid "4CEB42D9-4AC1-7326-28C6-CC962C5BCA74";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -1.313717310304516e-045 -9.9676902115730961 31.608707641815993 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -56.320253626441335 0 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Jaw_Deform_Ctrl" -p "Jaw_Deform_Ctrl_Gro";
	rename -uid "13BB3BD3-4F3F-EEB0-F0B4-36A17678A679";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".rp" -type "double3" 8.3266726846886741e-017 0 0 ;
	setAttr ".sp" -type "double3" 2.2204460492503131e-016 0 0 ;
createNode nurbsCurve -n "Jaw_Deform_Ctrl_Shape" -p "Jaw_Deform_Ctrl";
	rename -uid "878B9C04-474B-4F07-C4CA-8982C0DAB323";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 74 0 no 3
		77 0 0 0.84623107382366158 0.84623107382366158 1.8462310738236616 2.8462310738236618
		 2.8462310738236618 3.8462310738236618 4.8462310738236614 4.8462310738236614 5.8462310738236614
		 6.8462310738236614 6.8462310738236614 7.8462310738236605 8.8462310738236614 8.8462310738236614
		 9.4917711003297747 9.4917711003297747 10.877117664659169 10.877117664659169 11.877117664659169
		 12.877117664659169 12.877117664659169 13.877117664659169 14.877117664659169 14.877117664659169
		 15.877117664659169 16.877117664659167 16.877117664659167 17.877117664659167 18.877117664659167
		 18.877117664659167 19.70306588990011 19.70306588990011 21.881337486615365 22.544408319543106
		 23.207479152470839 23.870549985398576 24.533620818326312 25.196691651254049 25.859762484181783
		 26.522833317109523 27.18590415003726 27.848974982964997 28.512045815892733 29.17511664882047
		 29.838187481748207 30.501258314675944 31.164329147603681 31.827399980531418 32.490470813459154
		 33.153541646386891 33.816612479314628 34.479683312242365 35.142754145170102 35.805824978097839
		 36.468895811025575 37.131966643953312 37.795037476881049 38.458108309808786 39.121179142736523
		 39.78424997566426 40.447320808592004 41.110391641519733 41.77346247444747 42.436533307375207
		 43.099604140302944 43.762674973230681 44.425745806158417 45.088816639086154 45.751887472013891
		 46.414958304941635 47.078029137869365 47.741099970797102 48.404170803724838 49.067241636652575
		 49.067241636652575
		76
		-9.565369337286636e-016 1.6626019261850764 -1.6631758603025404
		-7.8504458061971778e-016 1.3749986123733269 -1.2315540918572276
		-8.7750582705877648e-016 1.0555994730227076 -0.81514565684806917
		-7.8711714325402686e-016 0.82811732668785565 -1.2222200995496479
		-6.8919639365966655e-016 0.19755172087562772 -1.6632159509346502
		-6.8919639365966655e-016 -0.15564444829924906 -1.6632159509346502
		-6.8919639365966655e-016 -0.77024612121467873 -1.6632159509346502
		-9.2048451187631759e-016 -1.7255292090890304 -0.62158686791891882
		-1.1371515866603842e-015 -1.7255292090890304 0.35419488934206483
		-1.2937819626378634e-015 -1.676495636943248 1.0595953922291368
		-1.454841028065295e-015 -1.031651624955231 1.7849409392727495
		-1.454841028065295e-015 -0.65051857321095297 1.7849409392727495
		-1.454841028065295e-015 -0.35319616917487723 1.7849409392727495
		-1.3653385205538258e-015 0.041905323854101159 1.3818574797953729
		-1.2727343960158738e-015 0.14965992218522625 0.96480557903329345
		-1.3631230798206241e-015 0.21451242521733935 1.3718800217348719
		-1.4535117636253745e-015 0.27936492824945219 1.7789544644364494
		-1.2587773357483505e-015 0.39510149302897818 0.90194856761328046
		-1.0640429078713276e-015 0.51083805780850311 0.024942670790110685
		-1.1034773202190156e-015 0.35519360950925444 0.20253947554473783
		-1.142911732566705e-015 0.039909832242001064 0.38013628029936514
		-1.1479478340362542e-015 -0.11972754800372584 0.40281686500102798
		-1.1483675091587163e-015 -0.28787216041038233 0.40470691372616702
		-1.1188179955567079e-015 -0.47492713203087078 0.27162773527917605
		-1.0924001165530158e-015 -0.49571766800739447 0.15265218524223667
		-1.0370149636295567e-015 -0.51083805780850344 -0.096780368825715127
		-9.7276848047656577e-016 -0.14167600701454883 -0.38612080641339014
		-9.7276848047656577e-016 0.1775968047546273 -0.38612080641339014
		-9.7276848047656577e-016 0.44498878333147951 -0.38612080641339014
		-1.008214666801228e-015 0.8660316673177586 -0.22648537488994111
		-1.0458767265623561e-015 1.0436265233501074 -0.056870536583714153
		-1.2326118505172936e-015 1.2123498095087937 0.78410969807672892
		-1.3478130378306127e-015 1.3071346867224063 1.3029297223336316
		-1.0419301830793589e-015 1.4567936345464951 -0.074644188343142431
		-9.565369337286636e-016 1.6626019261850764 -1.6631758603025404
		-9.565369337286636e-016 1.6626019261850764 -1.6631758603025404
		-1.0573833327421795e-015 1.9022207804416371 -1.3825213796058524
		-1.1582573391658379e-015 2.0950006459749013 -1.0678246342178732
		-1.256675100179858e-015 2.2361946426957431 -0.72683450242866654
		-1.3502132438782498e-015 2.3223261058088949 -0.36794729296425066
		-1.4365685507278556e-015 2.3512741928385616 -1.277350030280977e-015
		-1.5136146664772108e-015 2.3223261058088926 0.36794729296424666
		-1.5794544600551653e-015 2.23619464269574 0.72683450242866099
		-1.6324667372340843e-015 2.0950006459749 1.0678246342178674
		-1.6713461598121595e-015 1.9022207804416356 1.3825213796058495
		-1.6951353873721152e-015 1.662601926185074 1.6631758603025364
		-1.703248650179503e-015 1.3820442946463969 1.9028774315543555
		-1.6954861727776331e-015 1.06745614583148 2.0957238451531821
		-1.6720390931223239e-015 0.72658368402235363 2.2369665823756613
		-1.633484756131083e-015 0.36782032051960206 2.3231277782736011
		-1.5807724975351439e-015 5.7842507935852909e-016 2.3520858582513879
		-1.515200268083097e-015 -0.36782032051960051 2.3231277782736011
		-1.4383826736858023e-015 -0.72658368402235285 2.2369665823756613
		-1.3522112184603006e-015 -1.0674561458314782 2.0957238451531852
		-1.2588077296209082e-015 -1.3820442946463969 1.9028774315543555
		-1.1604721110512592e-015 -1.662601926185074 1.6631758603025386
		-1.0596257120377433e-015 -1.9022207804416369 1.3825213796058502
		-9.5875170561408358e-016 -2.0950006459749004 1.0678246342178681
		-8.6033394460006547e-016 -2.2361946426957413 0.7268345024286611
		-7.6679580090167307e-016 -2.3223261058088935 0.36794729296424739
		-6.8044049405206577e-016 -2.3512741928385648 -1.0339300113811744e-015
		-6.0339437830271106e-016 -2.3223261058088935 -0.36794729296424977
		-5.3755458472475656e-016 -2.2361946426957418 -0.72683450242866499
		-4.8454230754583731e-016 -2.0950006459749004 -1.0678246342178714
		-4.4566288496776212e-016 -1.9022207804416369 -1.3825213796058524
		-4.2187365740780659e-016 -1.662601926185076 -1.6631758603025404
		-4.1376039460041742e-016 -1.3820442946463969 -1.9028774315543615
		-4.2152287200228662e-016 -1.06745614583148 -2.0957238451531897
		-4.4496995165759676e-016 -0.72658368402235307 -2.236966582375667
		-4.8352428864883927e-016 -0.36782032051960145 -2.3231277782736064
		-5.3623654724477761e-016 9.1585041558921856e-017 -2.3520858582513933
		-6.0180877669682544e-016 0.36782032051960206 -2.3231277782736073
		-6.7862637109411981e-016 0.72658368402235396 -2.236966582375667
		-7.6479782631962123e-016 1.06745614583148 -2.0957238451531901
		-8.5820131515901413e-016 1.3820442946463971 -1.9028774315543615
		-9.565369337286636e-016 1.6626019261850764 -1.6631758603025404
		;
createNode transform -n "Head_Deform_Ctrl_Gro" -p "Deform_Ctrl_Grp";
	rename -uid "38C2C922-4EC9-C3CC-358D-BBA056F87D8E";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -1.313717310304516e-045 27.925381183087808 14.677030212263286 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Head_Deform_Ctrl" -p "Head_Deform_Ctrl_Gro";
	rename -uid "10F16D3E-4784-463C-C5E1-FAAF834DA701";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Head_Deform_Ctrl_Shape" -p "Head_Deform_Ctrl";
	rename -uid "2FA6FE03-414C-1E46-35C6-8BBB9791569C";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 60 0 no 3
		61 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60
		61
		-2.3641860462498085 -1.4751850593001423 0
		-2.0663704976972226 -1.774656833645935 0
		-1.717680487115077 -2.030423860251191 0
		-1.326691341472154 -2.2361881226127793 0
		-0.90303641092487841 -2.3869046697948129 0
		-0.45714664910376873 -2.4788360975402455 0
		3.5199423943699571e-046 -2.5097377840503863 0
		0.45714664910376873 -2.4788360975402455 0
		0.90303641092487841 -2.3869046697948129 0
		1.326691341472154 -2.2361881226127793 0
		1.717680487115077 -2.030423860251191 0
		2.0663704976972226 -1.774656833645935 0
		2.3641860462498085 -1.4751850593001423 0
		2.6037830789266274 -1.139396175949311 0
		2.779266739450525 -0.77555169935930113 0
		2.8863112275589908 -0.39260941390246307 0
		2.922290553672001 0 0
		2.8863112275589908 0.39260941390246307 0
		2.779266739450525 0.77555169935930113 0
		2.6037830789266274 1.139396175949311 0
		2.3641860462498085 1.4751850593001423 0
		2.0663704976972226 1.774656833645935 0
		1.717680487115077 2.030423860251191 0
		1.326691341472154 2.2361881226127793 0
		0.90303641092487841 2.3869046697948129 0
		0.45714664910376873 2.4788360975402455 0
		3.5199423943699571e-046 2.5097377840503863 0
		-0.45714664910376873 2.4788360975402455 0
		-0.90303641092487841 2.3869046697948129 0
		-1.326691341472154 2.2361881226127793 0
		-1.717680487115077 2.030423860251191 0
		-2.0663704976972226 1.774656833645935 0
		-2.3641860462498085 1.4751850593001423 0
		-2.6037830789266274 1.139396175949311 0
		-2.779266739450525 0.77555169935930113 0
		-2.8863112275589908 0.39260941390246307 0
		-2.922290553672001 0 0
		-2.8863112275589908 -0.39260941390246307 0
		-2.779266739450525 -0.77555169935930113 0
		-2.6037830789266274 -1.139396175949311 0
		-2.3641860462498085 -1.4751850593001423 0
		-2.1141831212538125 -1.179559651434632 0
		-1.8302493599416805 1.2729184843044754 0
		-2.1439624968646087 1.4751850593001423 0
		-0.25456081479401527 2.3139217726703731 0
		-0.42814853263358826 1.8968361745620843 0
		-0.40368760313901458 0.35731110168469304 0
		0.054115761284207121 0.14292356897609149 0
		0.082629104823204916 1.7762367858828798 0
		-0.18088600755201717 2.0442293739353756 0
		2.0691163457228057 1.4751850593001423 0
		1.554302529592851 1.2148525155412413 0
		1.6522050871716956 -1.0120705492296591 0
		1.9377514893877417 -1.5428397037082726 0
		-0.057407074199317398 -1.7846377732944854 0
		0.082629104823204916 -1.4965634474993299 0
		0.082629104823204916 -0.50777376688658404 0
		-0.4220717094436362 -0.32648786797528478 0
		-0.4220717094436362 -1.7087128961426357 0
		3.5199423943699571e-046 -2.2779206541127213 0
		-2.3641860462498085 -1.4751850593001423 0
		;
createNode transform -n "Face_Pose__Sel" -p "facial__Ctrl";
	rename -uid "D56CD144-4070-2682-F2EB-5C90FE8158AC";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.8886090522101303e-031 -13.141963 -0.14325199999999991 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
	setAttr ".Mili_Hide" yes;
createNode transform -n "Orb__Wr_Gro" -p "Face_Pose__Sel";
	rename -uid "16EDF3FD-4D29-9234-9271-BEAA71BDA607";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_A_Pose" -p "Orb__Wr_Gro";
	rename -uid "B7EDDF84-470F-F248-B537-F3A13114E114";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.3051663339138031 14.112489609067868 1.5530088041096839 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_A_Mix" -p "L_UppOrb_A_Pose";
	rename -uid "8F4AE560-4C23-1200-4CD6-1597CD6D2A93";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_A_Offset" -p "L_UppOrb_A_Mix";
	rename -uid "71A3A89E-4FDE-A6BB-A256-13921092CAA9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_A_Sel" -p "L_UppOrb_A_Offset";
	rename -uid "DDE15FFE-4057-EAF8-EC0F-0B99E11B6F6D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppOrb_A_Sel_Shape" -p "L_UppOrb_A_Sel";
	rename -uid "E2A8634B-4B91-F6AC-DEE0-63BAC2C043A7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_UppOrb_B_Pose" -p "Orb__Wr_Gro";
	rename -uid "DE87F697-46E4-9E33-1CC4-DFB27555DEFC";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.37172111868858337 14.170125870054196 1.5771494004994544 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_B_Mix" -p "L_UppOrb_B_Pose";
	rename -uid "79B6A68F-4E3B-4012-A5BA-1B8DBA8B3CEA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_B_Offset" -p "L_UppOrb_B_Mix";
	rename -uid "CF4CE654-4632-A107-F8D0-5C97F90EF1F5";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_B_Sel" -p "L_UppOrb_B_Offset";
	rename -uid "24F40BB8-4658-1D37-D514-5A83D64A08D8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppOrb_B_Sel_Shape" -p "L_UppOrb_B_Sel";
	rename -uid "281D32A3-4D8C-08BB-76F6-08B5A9D457C0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_UppOrb_C_Pose" -p "Orb__Wr_Gro";
	rename -uid "586AA293-4CEA-9C20-5CD5-549AE5E8C649";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.52350372076034546 14.19881143981738 1.5801622960835608 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_C_Mix" -p "L_UppOrb_C_Pose";
	rename -uid "EA1E2276-4A62-D88F-7A7A-298181A2D004";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_C_Offset" -p "L_UppOrb_C_Mix";
	rename -uid "1E862FAA-43D9-E5CA-F4ED-368BF9F08A4C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_C_Sel" -p "L_UppOrb_C_Offset";
	rename -uid "300CEBF4-40FD-5422-17F2-BBB091C055BD";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppOrb_C_Sel_Shape" -p "L_UppOrb_C_Sel";
	rename -uid "163FED6B-4E0C-BB04-0146-92B6327D46B0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_UppOrb_D_Pose" -p "Orb__Wr_Gro";
	rename -uid "FC233BE6-490B-4644-F44A-9F800264AAB4";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.65998560190200806 14.158397583311032 1.5184462163716468 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_D_Mix" -p "L_UppOrb_D_Pose";
	rename -uid "2B6A67D3-4BAC-5B06-F2A1-0CBFEC418F44";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_D_Offset" -p "L_UppOrb_D_Mix";
	rename -uid "DE8A11C2-4603-522E-389D-779CB68DBAEE";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_D_Sel" -p "L_UppOrb_D_Offset";
	rename -uid "641CC306-4695-9E38-5D3A-BC9830F4CB21";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppOrb_D_Sel_Shape" -p "L_UppOrb_D_Sel";
	rename -uid "3A4168CD-41B9-1327-225C-36A76EE5625F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_UppOrb_E_Pose" -p "Orb__Wr_Gro";
	rename -uid "3B826560-454E-69BF-9768-2AB27706009A";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.72242259979248047 14.097748665159177 1.4647510144978677 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_E_Mix" -p "L_UppOrb_E_Pose";
	rename -uid "68AB329A-479C-95C4-32DF-05AA78AA9390";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_E_Offset" -p "L_UppOrb_E_Mix";
	rename -uid "14295F3C-479A-AFC5-A002-439370806022";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppOrb_E_Sel" -p "L_UppOrb_E_Offset";
	rename -uid "EEB552DD-4F1A-BE5C-CD6D-8CA384BB6310";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppOrb_E_Sel_Shape" -p "L_UppOrb_E_Sel";
	rename -uid "A8F3F84E-4209-E294-C7FC-9BB3D5B86772";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_LowOrb_A_Pose" -p "Orb__Wr_Gro";
	rename -uid "66468C3D-47F9-B7EA-252C-BA9752958875";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.30469036102294922 13.955089477842282 1.5496707055836827 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_A_Mix" -p "L_LowOrb_A_Pose";
	rename -uid "389A6439-4BED-DDEF-0E52-9E8D1D23A681";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_A_Offset" -p "L_LowOrb_A_Mix";
	rename -uid "99CD1DD3-43D7-ACE9-2B53-42BA30A1DBCA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_A_Sel" -p "L_LowOrb_A_Offset";
	rename -uid "CFA1B63B-4E00-D708-7B58-679D29840CAC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowOrb_A_Sel_Shape" -p "L_LowOrb_A_Sel";
	rename -uid "8E92C99B-4F31-5D17-1E97-738FB721573E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_LowOrb_B_Pose" -p "Orb__Wr_Gro";
	rename -uid "E228D982-4407-C9FE-FAE0-95B90A245821";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.37047025561332703 13.893838791196774 1.5607586000233802 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_B_Mix" -p "L_LowOrb_B_Pose";
	rename -uid "2378EFA8-4B3B-EF74-0A08-6E8BDD6386D7";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_B_Offset" -p "L_LowOrb_B_Mix";
	rename -uid "03EE4913-4A5F-4B40-7A21-F0A5FD971142";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_B_Sel" -p "L_LowOrb_B_Offset";
	rename -uid "44017511-4B09-6992-35DD-2D8A72B92BF8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowOrb_B_Sel_Shape" -p "L_LowOrb_B_Sel";
	rename -uid "44E7A87A-49FA-1620-2074-F7BF90940815";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_LowOrb_C_Pose" -p "Orb__Wr_Gro";
	rename -uid "D7C4EA3B-44E6-9DA0-7724-EA9DD62E5A8E";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.52415925264358521 13.846062568967772 1.5595938060551795 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_C_Mix" -p "L_LowOrb_C_Pose";
	rename -uid "D2720882-41EB-80D4-B4ED-1F8CA7DB676C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_C_Offset" -p "L_LowOrb_C_Mix";
	rename -uid "4C40D909-466E-65F4-251F-7DAEF3E3C5EF";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_C_Sel" -p "L_LowOrb_C_Offset";
	rename -uid "0FD0BFA8-461A-67AA-0AA2-9389B987C94C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowOrb_C_Sel_Shape" -p "L_LowOrb_C_Sel";
	rename -uid "A01A9C20-4CDF-AEBF-B68E-15863B65B502";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_LowOrb_D_Pose" -p "Orb__Wr_Gro";
	rename -uid "3B062BB2-4CA3-6B8A-818E-70B2E2C7F4C2";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.67298567295074463 13.886000541990231 1.4925614688664588 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_D_Mix" -p "L_LowOrb_D_Pose";
	rename -uid "E68459DD-4FC4-88D9-93BA-5BA11E45C26F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_D_Offset" -p "L_LowOrb_D_Mix";
	rename -uid "45806D41-4E1D-BFCA-2720-A0BC27E50D69";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_D_Sel" -p "L_LowOrb_D_Offset";
	rename -uid "E200CC3D-4071-38D8-F3D6-C49738256B2A";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowOrb_D_Sel_Shape" -p "L_LowOrb_D_Sel";
	rename -uid "ED6C5D0D-4A36-9E30-17AF-7C9BFE89BB7F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "L_LowOrb_E_Pose" -p "Orb__Wr_Gro";
	rename -uid "332CE84D-4E7E-CE55-8F8A-BFA2B80236B9";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.7265961766242981 13.97671785766406 1.4530404899388465 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_E_Mix" -p "L_LowOrb_E_Pose";
	rename -uid "A390B359-43CF-9361-8008-2D88C0E56B67";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_E_Offset" -p "L_LowOrb_E_Mix";
	rename -uid "C37331F6-428F-1CF6-D007-BDA8F0A4E8BA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowOrb_E_Sel" -p "L_LowOrb_E_Offset";
	rename -uid "3A263309-411B-C383-BAB2-EAB697C67419";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowOrb_E_Sel_Shape" -p "L_LowOrb_E_Sel";
	rename -uid "CA41DC61-4C61-74B7-0EA0-99ABDE241A7B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_UppOrb_A_Pose" -p "Orb__Wr_Gro";
	rename -uid "CD820C43-4208-0B5C-E3B9-1CAFD64F93FB";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.3051663339138031 14.112489609067868 1.5530088041096839 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_A_Mix" -p "R_UppOrb_A_Pose";
	rename -uid "378BEFB5-4B7D-BAFB-FF80-DDA8DB0D0EE2";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_A_Offset" -p "R_UppOrb_A_Mix";
	rename -uid "C39FAE67-4E25-485C-D89D-28A03241103C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_A_Sel" -p "R_UppOrb_A_Offset";
	rename -uid "7B4B7164-4842-7623-1C95-A9BEE38C93ED";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppOrb_A_Sel_Shape" -p "R_UppOrb_A_Sel";
	rename -uid "427A4746-48F3-77E9-137C-A2944A12560B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_UppOrb_B_Pose" -p "Orb__Wr_Gro";
	rename -uid "C2D1AB7D-48E4-C3B2-2BCB-E4B0E98332E4";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.37172111868858337 14.170125870054196 1.5771494004994544 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_B_Mix" -p "R_UppOrb_B_Pose";
	rename -uid "D0484AD6-4A35-7FFC-F89B-5CA04CEA3DD3";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_B_Offset" -p "R_UppOrb_B_Mix";
	rename -uid "12EECAF3-4C53-6564-6CF3-80838A78B90C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_B_Sel" -p "R_UppOrb_B_Offset";
	rename -uid "B60117AF-4F4D-19D4-CD30-A58BEFC2C8CA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppOrb_B_Sel_Shape" -p "R_UppOrb_B_Sel";
	rename -uid "BC8C5278-4D63-D842-A744-F0BC812EC91C";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_UppOrb_C_Pose" -p "Orb__Wr_Gro";
	rename -uid "E79F0D34-4BD1-0B35-044C-FDA84FCA1FBD";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.52350372076034546 14.19881143981738 1.5801622960835608 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_C_Mix" -p "R_UppOrb_C_Pose";
	rename -uid "5A9BC64A-465D-2391-715D-3D939119EBFE";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_C_Offset" -p "R_UppOrb_C_Mix";
	rename -uid "5567B39E-488D-5379-8B56-E3B6174386A6";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_C_Sel" -p "R_UppOrb_C_Offset";
	rename -uid "5C3C2562-4FDC-BB82-AA42-71AC2599AAFD";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppOrb_C_Sel_Shape" -p "R_UppOrb_C_Sel";
	rename -uid "DAC40874-4EFE-8CBD-98B3-49A85751A0BE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_UppOrb_D_Pose" -p "Orb__Wr_Gro";
	rename -uid "1878F723-435F-90E5-938A-B699E7918909";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.65998560190200806 14.158397583311032 1.5184462163716468 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_D_Mix" -p "R_UppOrb_D_Pose";
	rename -uid "A51A1E29-4A27-2974-6031-57AADC62F3FC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_D_Offset" -p "R_UppOrb_D_Mix";
	rename -uid "DED8E9A1-4AE2-164A-620E-67AD293B0D25";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_D_Sel" -p "R_UppOrb_D_Offset";
	rename -uid "F6BDB9B9-4BEB-4BBF-4E86-7988739EF5CA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppOrb_D_Sel_Shape" -p "R_UppOrb_D_Sel";
	rename -uid "BD0EF427-4BA6-87C3-1FAA-2BB8CB5F145A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_UppOrb_E_Pose" -p "Orb__Wr_Gro";
	rename -uid "14155ADD-42C7-B95D-F2C0-BEBFD2A77CA4";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.72242259979248047 14.097748665159177 1.4647510144978677 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_E_Mix" -p "R_UppOrb_E_Pose";
	rename -uid "5CC9B5BD-48D0-016E-8329-AA9E2A0A182B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_E_Offset" -p "R_UppOrb_E_Mix";
	rename -uid "84FEAB44-414B-F731-D63F-AE86A461581B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppOrb_E_Sel" -p "R_UppOrb_E_Offset";
	rename -uid "145A97FE-4CE2-A65F-8BCF-70B7B329A35C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppOrb_E_Sel_Shape" -p "R_UppOrb_E_Sel";
	rename -uid "46237A69-4341-BB42-B27D-9D8793AA354D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_LowOrb_A_Pose" -p "Orb__Wr_Gro";
	rename -uid "99FDBC69-46BB-9CC7-F9CD-D183177255E4";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.30469036102294922 13.955089477842282 1.5496707055836827 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_A_Mix" -p "R_LowOrb_A_Pose";
	rename -uid "387D0D64-4133-F394-B1B2-7CA8754EEBD1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_A_Offset" -p "R_LowOrb_A_Mix";
	rename -uid "933606CB-4797-391A-C133-069BB9562AF8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_A_Sel" -p "R_LowOrb_A_Offset";
	rename -uid "24F30C86-4CDC-FFC6-0A9C-90893555342A";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowOrb_A_Sel_Shape" -p "R_LowOrb_A_Sel";
	rename -uid "EBFE68C3-454C-D2CC-5D93-F8857CB614FC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_LowOrb_B_Pose" -p "Orb__Wr_Gro";
	rename -uid "5D5DF58D-47DF-C5A9-D882-E3B52B4CE91D";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.37047028541564941 13.893838791196774 1.5607586000233802 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_B_Mix" -p "R_LowOrb_B_Pose";
	rename -uid "BC811D58-4AFC-AB0E-82AF-9D8185A929FD";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_B_Offset" -p "R_LowOrb_B_Mix";
	rename -uid "C6B8CB53-424E-9F24-E846-78A3A75DB3AC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_B_Sel" -p "R_LowOrb_B_Offset";
	rename -uid "C4815326-4741-58F3-EF69-A1ACDC3A1894";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowOrb_B_Sel_Shape" -p "R_LowOrb_B_Sel";
	rename -uid "0697B11F-49C4-5268-7744-75B7C6D8C7D3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_LowOrb_C_Pose" -p "Orb__Wr_Gro";
	rename -uid "8CD15406-4BE8-0B17-9177-F486C8B2ABB6";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.52415925264358521 13.846062568967772 1.5595938060551795 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_C_Mix" -p "R_LowOrb_C_Pose";
	rename -uid "A6F29BA0-4AAA-6B51-167F-59BF08A6B8B2";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_C_Offset" -p "R_LowOrb_C_Mix";
	rename -uid "E4385B88-4467-401F-10AB-08BAC4B4E291";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_C_Sel" -p "R_LowOrb_C_Offset";
	rename -uid "39411500-43B3-B677-60C3-2280FEEC1E5F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowOrb_C_Sel_Shape" -p "R_LowOrb_C_Sel";
	rename -uid "7C4A3280-4BE4-717D-68CF-63BD8742A807";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_LowOrb_D_Pose" -p "Orb__Wr_Gro";
	rename -uid "FF641F01-498C-1640-B196-28A8B56E255B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.6729857325553894 13.886000541990231 1.4925614688664588 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_D_Mix" -p "R_LowOrb_D_Pose";
	rename -uid "E6577F19-4109-51F9-F4E7-E8B5C651B145";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_D_Offset" -p "R_LowOrb_D_Mix";
	rename -uid "C07A3AFE-4C0B-BEF9-9BA4-DE86645D95C5";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_D_Sel" -p "R_LowOrb_D_Offset";
	rename -uid "61B0D14A-41CC-6E73-B46F-60A34E2D3993";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowOrb_D_Sel_Shape" -p "R_LowOrb_D_Sel";
	rename -uid "25DA713B-4056-1D62-DE81-A9AD4C3E1CF3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "R_LowOrb_E_Pose" -p "Orb__Wr_Gro";
	rename -uid "157CD093-4B8F-68FF-D795-A49EE094005B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.72659623622894287 13.97671785766406 1.4530404899388465 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_E_Mix" -p "R_LowOrb_E_Pose";
	rename -uid "5AC6E0F4-4205-57C6-2616-49814C1A4467";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_E_Offset" -p "R_LowOrb_E_Mix";
	rename -uid "9A493802-4DCC-28FF-E090-A19FE951C68D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowOrb_E_Sel" -p "R_LowOrb_E_Offset";
	rename -uid "50616AA6-45CC-30D5-7A1E-47B6CE09A8E4";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowOrb_E_Sel_Shape" -p "R_LowOrb_E_Sel";
	rename -uid "88259319-4032-E9E2-4BD1-CE90606F44B0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.016333546875 0
		0 0.016085398437499999 0.0028362890625000001
		0 0.015348499999999999 0.0055863984375
		0 0.01414525 0.008166796875
		0 0.012512250000000001 0.010499
		0 0.010499 0.012512250000000001
		0 0.008166796875 0.01414525
		0 0.0055863984375 0.015348499999999999
		0 0.0028362890625000001 0.016085398437499999
		0 0 0.016333546875
		0 -0.0028362890625000001 0.016085398437499999
		0 -0.0055863984375 0.015348499999999999
		0 -0.008166796875 0.01414525
		0 -0.010499 0.012512250000000001
		0 -0.012512250000000001 0.010499
		0 -0.01414525 0.008166796875
		0 -0.015348499999999999 0.0055863984375
		0 -0.016085398437499999 0.0028362890625000001
		0 -0.016333546875 0
		0 -0.016085398437499999 -0.0028362890625000001
		0 -0.015348499999999999 -0.0055863984375
		0 -0.01414525 -0.008166796875
		0 -0.012512250000000001 -0.010499
		0 -0.010499 -0.012512250000000001
		0 -0.008166796875 -0.01414525
		0 -0.0055863984375 -0.015348499999999999
		0 -0.0028362890625000001 -0.016085398437499999
		0 0 -0.016333546875
		0 0.0028362890625000001 -0.016085398437499999
		0 0.0055863984375 -0.015348499999999999
		0 0.008166796875 -0.01414525
		0 0.010499 -0.012512250000000001
		0 0.012512250000000001 -0.010499
		0 0.01414525 -0.008166796875
		0 0.015348499999999999 -0.0055863984375
		0 0.016085398437499999 -0.0028362890625000001
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 -0.0028362890625000001 0
		-0.015348499999999999 -0.0055863984375 0
		-0.01414525 -0.008166796875 0
		-0.012512250000000001 -0.010499 0
		-0.010499 -0.012512250000000001 0
		-0.008166796875 -0.01414525 0
		-0.0055863984375 -0.015348499999999999 0
		-0.0028362890625000001 -0.016085398437499999 0
		0 -0.016333546875 0
		0.0028362890625000001 -0.016085398437499999 0
		0.0055863984375 -0.015348499999999999 0
		0.008166796875 -0.01414525 0
		0.010499 -0.012512250000000001 0
		0.012512250000000001 -0.010499 0
		0.01414525 -0.008166796875 0
		0.015348499999999999 -0.0055863984375 0
		0.016085398437499999 -0.0028362890625000001 0
		0.016333546875 0 0
		0.016085398437499999 0.0028362890625000001 0
		0.015348499999999999 0.0055863984375 0
		0.01414525 0.008166796875 0
		0.012512250000000001 0.010499 0
		0.010499 0.012512250000000001 0
		0.008166796875 0.01414525 0
		0.0055863984375 0.015348499999999999 0
		0.0028362890625000001 0.016085398437499999 0
		0 0.016333546875 0
		-0.0028362890625000001 0.016085398437499999 0
		-0.0055863984375 0.015348499999999999 0
		-0.008166796875 0.01414525 0
		-0.010499 0.012512250000000001 0
		-0.012512250000000001 0.010499 0
		-0.01414525 0.008166796875 0
		-0.015348499999999999 0.0055863984375 0
		-0.016085398437499999 0.0028362890625000001 0
		-0.016333546875 0 0
		-0.016085398437499999 0 -0.0028362890625000001
		-0.015348499999999999 0 -0.0055863984375
		-0.01414525 0 -0.008166796875
		-0.012512250000000001 0 -0.010499
		-0.010499 0 -0.012512250000000001
		-0.008166796875 0 -0.01414525
		-0.0055863984375 0 -0.015348499999999999
		-0.0028362890625000001 0 -0.016085398437499999
		0 0 -0.016333546875
		0.0028362890625000001 0 -0.016085398437499999
		0.0055863984375 0 -0.015348499999999999
		0.008166796875 0 -0.01414525
		0.010499 0 -0.012512250000000001
		0.012512250000000001 0 -0.010499
		0.01414525 0 -0.008166796875
		0.015348499999999999 0 -0.0055863984375
		0.016085398437499999 0 -0.0028362890625000001
		0.016333546875 0 0
		0.016085398437499999 0 0.0028362890625000001
		0.015348499999999999 0 0.0055863984375
		0.01414525 0 0.008166796875
		0.012512250000000001 0 0.010499
		0.010499 0 0.012512250000000001
		0.008166796875 0 0.01414525
		0.0055863984375 0 0.015348499999999999
		0.0028362890625000001 0 0.016085398437499999
		0 0 0.016333546875
		-0.0028362890625000001 0 0.016085398437499999
		-0.0055863984375 0 0.015348499999999999
		-0.008166796875 0 0.01414525
		-0.010499 0 0.012512250000000001
		-0.012512250000000001 0 0.010499
		-0.01414525 0 0.008166796875
		-0.015348499999999999 0 0.0055863984375
		-0.016085398437499999 0 0.0028362890625000001
		-0.016333546875 0 0
		;
createNode transform -n "Eye__Wr_Gro" -p "Face_Pose__Sel";
	rename -uid "DBD4728A-4DF5-DC31-F18D-9498D6BA71B1";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_A_Pose" -p "Eye__Wr_Gro";
	rename -uid "D0BFB9C2-4B8A-416F-D300-1791C920400B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.34366938471794128 14.032732395475341 1.5554930064946333 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_A_Mix" -p "L_Tlid_A_Pose";
	rename -uid "BC421D9F-4AC6-DCF1-9234-BE807870E38A";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -2.2204460492503131e-016 1.7763568923398097e-015 -4.4408920985006262e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_A_Offset" -p "L_Tlid_A_Mix";
	rename -uid "D7E5FED0-4440-8F86-6469-2D91F9FBF560";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_A_Sel" -p "L_Tlid_A_Offset";
	rename -uid "CAA4ABF5-4A07-E7B2-2FB1-D0947A41E06E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Tlid_A_Sel_Shape" -p "L_Tlid_A_Sel";
	rename -uid "D2A5D1F2-4575-9EEA-FB33-889862DD3D91";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591428 0.02196521875000039 -3.920475055707584e-016
		-0.012658160077587334 0.022133671875000385 -3.920475055707584e-016
		0.012658160077587115 0.022133671875000385 -3.920475055707584e-016
		0.013196331992591201 0.02196521875000039 -3.920475055707584e-016
		0.01365257278364481 0.021485468750000389 -3.920475055707584e-016
		0.013957421696608532 0.020767468750000385 -3.920475055707584e-016
		0.014064462347033938 0.019920531250000387 -3.8510861166685122e-016
		0.014064462347033938 0.00062460586345722269 -6.0021432268797525e-016
		0.013957421696608532 -0.00022233163654277605 -6.0021432268797525e-016
		0.01365257278364481 -0.00094033163654277246 -6.0021432268797525e-016
		0.013196331992591201 -0.0014200816365427735 -6.0021432268797525e-016
		0.012658160077587115 -0.0015885347615427758 -6.0021432268797525e-016
		-0.012658160077587334 -0.0015885347615427758 -6.0021432268797525e-016
		-0.013196331992591428 -0.0014200816365427735 -6.0021432268797525e-016
		-0.013652572783645015 -0.00094033163654277246 -6.0021432268797525e-016
		-0.013957421696608747 -0.00022233163654277605 -6.0021432268797525e-016
		-0.014064462347034151 0.00062460586345722269 -6.0021432268797525e-016
		-0.014064462347034151 0.019920531250000387 -3.8510861166685122e-016
		-0.013957421696608747 0.020767468750000385 -3.920475055707584e-016
		-0.013652572783645015 0.021485468750000389 -3.920475055707584e-016
		-0.013196331992591428 0.02196521875000039 -3.920475055707584e-016
		;
createNode transform -n "L_Tlid_B_Pose" -p "Eye__Wr_Gro";
	rename -uid "89B19999-441C-0EB1-CA75-3BB715F632BB";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.3867969810962677 14.031530288999512 1.5959382150441326 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_B_Mix" -p "L_Tlid_B_Pose";
	rename -uid "D9AD81A8-4906-6447-58B1-A4ADF93FF3CA";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -2.2204460492503131e-016 1.7763568394002505e-015 -4.4408920985006262e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_B_Offset" -p "L_Tlid_B_Mix";
	rename -uid "59647296-4206-3A8E-0CBB-F39AA15FE763";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_B_Sel" -p "L_Tlid_B_Offset";
	rename -uid "28FC8E9F-4831-2735-6BF6-58A521406F20";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Tlid_B_Sel_Shape" -p "L_Tlid_B_Sel";
	rename -uid "3856F750-4DE0-5CC6-31EE-C38C30632225";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591282 0.021965218749997451 1.7347234759768071e-017
		-0.01265816007758718 0.02213367187499745 1.7347234759768071e-017
		0.012658160077587277 0.02213367187499745 1.7347234759768071e-017
		0.013196331992591358 0.021965218749997451 1.7347234759768071e-017
		0.01365257278364497 0.02148546874999745 1.7347234759768071e-017
		0.01395742169660869 0.02076746874999745 1.7347234759768071e-017
		0.014064462347034096 0.019920531249997455 1.7347234759768071e-017
		0.014064462347034096 0.00062460586345428754 -1.9775847626135601e-016
		0.01395742169660869 -0.0002223316365457112 -1.9775847626135601e-016
		0.01365257278364497 -0.00094033163654570762 -1.9775847626135601e-016
		0.013196331992591358 -0.0014200816365457086 -1.9775847626135601e-016
		0.012658160077587277 -0.001588534761545711 -1.9775847626135601e-016
		-0.01265816007758718 -0.001588534761545711 -1.9775847626135601e-016
		-0.013196331992591282 -0.0014200816365457086 -1.9775847626135601e-016
		-0.013652572783644861 -0.00094033163654570762 -1.9775847626135601e-016
		-0.013957421696608586 -0.0002223316365457112 -1.9775847626135601e-016
		-0.014064462347034 0.00062460586345428754 -1.9775847626135601e-016
		-0.014064462347034 0.019920531249997455 1.7347234759768071e-017
		-0.013957421696608586 0.02076746874999745 1.7347234759768071e-017
		-0.013652572783644861 0.02148546874999745 1.7347234759768071e-017
		-0.013196331992591282 0.021965218749997451 1.7347234759768071e-017
		;
createNode transform -n "L_Tlid_C_Pose" -p "Eye__Wr_Gro";
	rename -uid "03821D0B-4CC5-2B3C-1BBB-C68801D57161";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.52614259719848633 14.030793098752929 1.627551326540104 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_C_Mix" -p "L_Tlid_C_Pose";
	rename -uid "8B32D9B1-4F7D-3572-7B65-C5BF9B4DF1CB";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1.7763568394002505e-015 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_C_Offset" -p "L_Tlid_C_Mix";
	rename -uid "0F34B390-48DE-DA30-EF75-2198450434F2";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_C_Sel" -p "L_Tlid_C_Offset";
	rename -uid "F4976891-4CFA-8EB2-B296-848F0D2CF2E3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Tlid_C_Sel_Shape" -p "L_Tlid_C_Sel";
	rename -uid "4B80EBDB-460E-29FC-EC96-F89893F59B53";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591305 0.021965218750002041 1.3877787807814457e-017
		-0.012658160077587207 0.022133671875002033 1.3877787807814457e-017
		0.012658160077587247 0.022133671875002033 1.3877787807814457e-017
		0.013196331992591346 0.021965218750002041 1.3877787807814457e-017
		0.013652572783644935 0.021485468750002033 1.3877787807814457e-017
		0.013957421696608656 0.020767468750002037 1.3877787807814457e-017
		0.014064462347034077 0.019920531250002042 1.3877787807814457e-017
		0.014064462347034077 0.00062460586345887414 -1.9775847626135601e-016
		0.013957421696608656 -0.00022233163654112459 -1.9775847626135601e-016
		0.013652572783644935 -0.00094033163654112795 -1.9775847626135601e-016
		0.013196331992591346 -0.001420081636541129 -1.9775847626135601e-016
		0.012658160077587247 -0.0015885347615411244 -1.9775847626135601e-016
		-0.012658160077587207 -0.0015885347615411244 -1.9775847626135601e-016
		-0.013196331992591305 -0.001420081636541129 -1.9775847626135601e-016
		-0.013652572783644882 -0.00094033163654112795 -1.9775847626135601e-016
		-0.013957421696608616 -0.00022233163654112459 -1.9775847626135601e-016
		-0.014064462347034032 0.00062460586345887414 -1.9775847626135601e-016
		-0.014064462347034032 0.019920531250002042 1.3877787807814457e-017
		-0.013957421696608616 0.020767468750002037 1.3877787807814457e-017
		-0.013652572783644882 0.021485468750002033 1.3877787807814457e-017
		-0.013196331992591305 0.021965218750002041 1.3877787807814457e-017
		;
createNode transform -n "L_Tlid_D_Pose" -p "Eye__Wr_Gro";
	rename -uid "D75E6038-40F2-FFDA-198D-96A524B57F94";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.65386086702346802 14.03189363891406 1.5413129422932781 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_D_Mix" -p "L_Tlid_D_Pose";
	rename -uid "31C7529C-4A72-5567-EE50-4CA5D6A141BC";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 2.2204460492503131e-016 1.7763568394002505e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_D_Offset" -p "L_Tlid_D_Mix";
	rename -uid "A2C0F76B-4446-8640-12C1-B488E8A70A04";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_D_Sel" -p "L_Tlid_D_Offset";
	rename -uid "90DCD848-4454-7369-2CC2-5892C700C5E8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Tlid_D_Sel_Shape" -p "L_Tlid_D_Sel";
	rename -uid "280476C3-424F-3085-1759-EEA8E385E437";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591312 0.021965218750002041 1.3877787807814457e-017
		-0.012658160077587207 0.022133671875002033 1.3877787807814457e-017
		0.012658160077587247 0.022133671875002033 1.3877787807814457e-017
		0.013196331992591346 0.021965218750002041 1.3877787807814457e-017
		0.013652572783644932 0.021485468750002033 1.3877787807814457e-017
		0.013957421696608656 0.020767468750002037 1.3877787807814457e-017
		0.014064462347034077 0.019920531250002042 1.3877787807814457e-017
		0.014064462347034077 0.00062460586345887414 -1.9775847626135601e-016
		0.013957421696608656 -0.00022233163654112459 -1.9775847626135601e-016
		0.013652572783644932 -0.00094033163654113142 -1.9775847626135601e-016
		0.013196331992591346 -0.001420081636541129 -1.9775847626135601e-016
		0.012658160077587247 -0.0015885347615411244 -1.9775847626135601e-016
		-0.012658160077587207 -0.0015885347615411244 -1.9775847626135601e-016
		-0.013196331992591312 -0.001420081636541129 -1.9775847626135601e-016
		-0.01365257278364488 -0.00094033163654113142 -1.9775847626135601e-016
		-0.013957421696608616 -0.00022233163654112459 -1.9775847626135601e-016
		-0.014064462347034032 0.00062460586345887414 -1.9775847626135601e-016
		-0.014064462347034032 0.019920531250002042 1.3877787807814457e-017
		-0.013957421696608616 0.020767468750002037 1.3877787807814457e-017
		-0.01365257278364488 0.021485468750002033 1.3877787807814457e-017
		-0.013196331992591312 0.021965218750002041 1.3877787807814457e-017
		;
createNode transform -n "L_Tlid_E_Pose" -p "Eye__Wr_Gro";
	rename -uid "A47D5024-4C4B-1274-2341-6FAF148A0BF1";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.68304216861724854 14.030395893400144 1.4853673074513587 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_E_Mix" -p "L_Tlid_E_Pose";
	rename -uid "ED904BEF-42D2-A713-6C8A-2FAD06252124";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1.7763568394002505e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_E_Offset" -p "L_Tlid_E_Mix";
	rename -uid "99244833-4C86-52FA-30B1-49B99D21822D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Tlid_E_Sel" -p "L_Tlid_E_Offset";
	rename -uid "167223FE-48F2-CA53-78BF-619B9002495B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Tlid_E_Sel_Shape" -p "L_Tlid_E_Sel";
	rename -uid "5011B2B5-40A7-CF72-3B40-1EB12686085F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591312 0.021965218750002041 1.3877787807814457e-017
		-0.012658160077587207 0.022133671875002033 1.3877787807814457e-017
		0.012658160077587247 0.022133671875002033 1.3877787807814457e-017
		0.013196331992591346 0.021965218750002041 1.3877787807814457e-017
		0.013652572783644932 0.021485468750002033 1.3877787807814457e-017
		0.013957421696608656 0.020767468750002037 1.3877787807814457e-017
		0.014064462347034077 0.019920531250002042 1.3877787807814457e-017
		0.014064462347034077 0.00062460586345887414 -1.9775847626135601e-016
		0.013957421696608656 -0.00022233163654112459 -1.9775847626135601e-016
		0.013652572783644932 -0.00094033163654113142 -1.9775847626135601e-016
		0.013196331992591346 -0.001420081636541129 -1.9775847626135601e-016
		0.012658160077587247 -0.0015885347615411244 -1.9775847626135601e-016
		-0.012658160077587207 -0.0015885347615411244 -1.9775847626135601e-016
		-0.013196331992591312 -0.001420081636541129 -1.9775847626135601e-016
		-0.01365257278364488 -0.00094033163654113142 -1.9775847626135601e-016
		-0.013957421696608616 -0.00022233163654112459 -1.9775847626135601e-016
		-0.014064462347034032 0.00062460586345887414 -1.9775847626135601e-016
		-0.014064462347034032 0.019920531250002042 1.3877787807814457e-017
		-0.013957421696608616 0.020767468750002037 1.3877787807814457e-017
		-0.01365257278364488 0.021485468750002033 1.3877787807814457e-017
		-0.013196331992591312 0.021965218750002041 1.3877787807814457e-017
		;
createNode transform -n "L_Blid_A_Pose" -p "Eye__Wr_Gro";
	rename -uid "55B4D0E2-42FD-8D89-4747-F383C765AD6E";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.34365963935852051 14.030704883878659 1.5556809995442544 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_A_Mix" -p "L_Blid_A_Pose";
	rename -uid "FF3A048E-4211-04FA-98D6-CFB3758C0F52";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 5.2939559203393771e-023 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_A_Offset" -p "L_Blid_A_Mix";
	rename -uid "460141D8-40AB-9ACA-F126-E8AD444BE69E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_A_Sel" -p "L_Blid_A_Offset";
	rename -uid "68201B68-475E-370A-38E2-F58835434106";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Blid_A_Sel_Shape" -p "L_Blid_A_Sel";
	rename -uid "67F5D66D-4EE3-539B-1849-929BAAF0CE17";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591282 -0.0021843283833573902 1.7347234759768071e-017
		-0.01265816007758718 -0.0020158752583573879 1.7347234759768071e-017
		0.012658160077587277 -0.0020158752583573879 1.7347234759768071e-017
		0.013196331992591358 -0.0021843283833573902 1.7347234759768071e-017
		0.013652572783644968 -0.0026640783833573912 1.7347234759768071e-017
		0.01395742169660869 -0.0033820783833573911 1.7347234759768071e-017
		0.014064462347034094 -0.0042290158833573899 1.7347234759768071e-017
		0.014064462347034094 -0.019920531250000578 -1.9775847626135601e-016
		0.01395742169660869 -0.020767468750000576 -1.9775847626135601e-016
		0.013652572783644968 -0.02148546875000058 -1.9775847626135601e-016
		0.013196331992591358 -0.021965218750000581 -1.9775847626135601e-016
		0.012658160077587277 -0.022133671875000576 -1.9428902930940239e-016
		-0.01265816007758718 -0.022133671875000576 -1.9428902930940239e-016
		-0.013196331992591282 -0.021965218750000581 -1.9775847626135601e-016
		-0.013652572783644861 -0.02148546875000058 -1.9775847626135601e-016
		-0.013957421696608586 -0.020767468750000576 -1.9775847626135601e-016
		-0.014064462347034012 -0.019920531250000578 -1.9775847626135601e-016
		-0.014064462347034012 -0.0042290158833573899 1.7347234759768071e-017
		-0.013957421696608586 -0.0033820783833573911 1.7347234759768071e-017
		-0.013652572783644861 -0.0026640783833573912 1.7347234759768071e-017
		-0.013196331992591282 -0.0021843283833573902 1.7347234759768071e-017
		;
createNode transform -n "L_Blid_B_Pose" -p "Eye__Wr_Gro";
	rename -uid "5522CE6B-4FBD-F177-C6D9-DF987384D787";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.38698843121528625 14.029996780698728 1.5950960014134561 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_B_Mix" -p "L_Blid_B_Pose";
	rename -uid "34A52A08-4062-8466-7D15-C790D60C4057";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1.7763568394002505e-015 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_B_Offset" -p "L_Blid_B_Mix";
	rename -uid "36A94EDA-4360-3BED-457F-40A89BFA7D6F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_B_Sel" -p "L_Blid_B_Offset";
	rename -uid "BE441F9E-49A8-1495-6C53-65A05056B84D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Blid_B_Sel_Shape" -p "L_Blid_B_Sel";
	rename -uid "3DADC798-49BA-3465-305E-4383E0627A98";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591275 -0.0021843283833560129 2.9143354396410359e-016
		-0.012658160077587173 -0.002015875258356014 2.9143354396410359e-016
		0.012658160077587277 -0.002015875258356014 2.9143354396410359e-016
		0.013196331992591372 -0.0021843283833560129 2.9143354396410359e-016
		0.01365257278364497 -0.0026640783833560139 2.9143354396410359e-016
		0.013957421696608694 -0.0033820783833560138 2.9143354396410359e-016
		0.01406446234703411 -0.0042290158833560125 2.9143354396410359e-016
		0.01406446234703411 -0.0199205312499992 7.9797279894933114e-017
		0.013957421696608694 -0.020767468749999199 7.9797279894933114e-017
		0.01365257278364497 -0.021485468749999199 7.9797279894933114e-017
		0.013196331992591372 -0.021965218749999203 7.9797279894933114e-017
		0.012658160077587277 -0.022133671874999199 7.9797279894933114e-017
		-0.012658160077587173 -0.022133671874999199 7.9797279894933114e-017
		-0.013196331992591275 -0.021965218749999203 7.9797279894933114e-017
		-0.013652572783644856 -0.021485468749999199 7.9797279894933114e-017
		-0.013957421696608584 -0.020767468749999199 7.9797279894933114e-017
		-0.014064462347033997 -0.0199205312499992 7.9797279894933114e-017
		-0.014064462347033997 -0.0042290158833560125 2.9143354396410359e-016
		-0.013957421696608584 -0.0033820783833560138 2.9143354396410359e-016
		-0.013652572783644856 -0.0026640783833560139 2.9143354396410359e-016
		-0.013196331992591275 -0.0021843283833560129 2.9143354396410359e-016
		;
createNode transform -n "L_Blid_C_Pose" -p "Eye__Wr_Gro";
	rename -uid "EF61781A-4615-4CA9-03E7-4DB62BC98321";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.52584892511367798 14.029387382810546 1.6256134603291663 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_C_Mix" -p "L_Blid_C_Pose";
	rename -uid "A651BE3D-436A-462A-6434-2A9C72FBB0B6";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1.7763568394002505e-015 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_C_Offset" -p "L_Blid_C_Mix";
	rename -uid "CC266F97-475C-0C71-A665-1F874FCB27D9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_C_Sel" -p "L_Blid_C_Offset";
	rename -uid "D76C5714-43A3-1245-51BB-958F217CB6C8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Blid_C_Sel_Shape" -p "L_Blid_C_Sel";
	rename -uid "8EAD8B7B-4C83-5D7F-0858-F08A59AA540E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591357 -0.0021843283833546667 4.0939474033052647e-016
		-0.012658160077587277 -0.0020158752583546713 4.0939474033052647e-016
		0.012658160077587185 -0.0020158752583546713 4.0939474033052647e-016
		0.013196331992591284 -0.0021843283833546667 4.0939474033052647e-016
		0.013652572783644864 -0.0026640783833546677 4.0939474033052647e-016
		0.013957421696608602 -0.0033820783833546676 4.0939474033052647e-016
		0.014064462347034012 -0.0042290158833546664 4.0939474033052647e-016
		0.014064462347034012 -0.019920531249997861 2.0122792321330957e-016
		0.013957421696608602 -0.020767468749997856 2.0122792321330957e-016
		0.013652572783644864 -0.021485468749997853 2.0122792321330957e-016
		0.013196331992591284 -0.021965218749997857 2.0122792321330957e-016
		0.012658160077587185 -0.022133671874997856 2.0122792321330957e-016
		-0.012658160077587277 -0.022133671874997856 2.0122792321330957e-016
		-0.013196331992591357 -0.021965218749997857 2.0122792321330957e-016
		-0.013652572783644953 -0.021485468749997853 2.0122792321330957e-016
		-0.013957421696608683 -0.020767468749997856 2.0122792321330957e-016
		-0.01406446234703409 -0.019920531249997861 2.0122792321330957e-016
		-0.01406446234703409 -0.0042290158833546664 4.0939474033052647e-016
		-0.013957421696608683 -0.0033820783833546676 4.0939474033052647e-016
		-0.013652572783644953 -0.0026640783833546677 4.0939474033052647e-016
		-0.013196331992591357 -0.0021843283833546667 4.0939474033052647e-016
		;
createNode transform -n "L_Blid_D_Pose" -p "Eye__Wr_Gro";
	rename -uid "3143B8C3-4C81-ABBE-42EB-F9A387980B0B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.65399408340454102 14.030682472532224 1.5409052465230142 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_D_Mix" -p "L_Blid_D_Pose";
	rename -uid "148C8856-49BF-4E86-E778-D68A39785F91";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 2.2204460492503131e-016 1.7763568394002505e-015 -4.4408920985006262e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_D_Offset" -p "L_Blid_D_Mix";
	rename -uid "5A6814FB-49D2-6E3D-567C-24AC54A712D9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_D_Sel" -p "L_Blid_D_Offset";
	rename -uid "BDF48331-4FB1-26BC-73E8-BBA66EA08E24";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Blid_D_Sel_Shape" -p "L_Blid_D_Sel";
	rename -uid "B63E7A0C-49EA-FCCC-2815-41B00E812D27";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591357 -0.0021843283833546667 4.0939474033052647e-016
		-0.012658160077587277 -0.0020158752583546713 4.0939474033052647e-016
		0.012658160077587185 -0.0020158752583546713 4.0939474033052647e-016
		0.013196331992591284 -0.0021843283833546667 4.0939474033052647e-016
		0.013652572783644864 -0.0026640783833546677 4.0939474033052647e-016
		0.013957421696608602 -0.0033820783833546676 4.0939474033052647e-016
		0.014064462347034012 -0.0042290158833546664 4.0939474033052647e-016
		0.014064462347034012 -0.019920531249997861 2.0122792321330957e-016
		0.013957421696608602 -0.020767468749997856 2.0122792321330957e-016
		0.013652572783644864 -0.021485468749997853 2.0122792321330957e-016
		0.013196331992591284 -0.021965218749997857 2.0122792321330957e-016
		0.012658160077587185 -0.022133671874997856 2.0122792321330957e-016
		-0.012658160077587277 -0.022133671874997856 2.0122792321330957e-016
		-0.013196331992591357 -0.021965218749997857 2.0122792321330957e-016
		-0.013652572783644953 -0.021485468749997853 2.0122792321330957e-016
		-0.013957421696608683 -0.020767468749997856 2.0122792321330957e-016
		-0.01406446234703409 -0.019920531249997861 2.0122792321330957e-016
		-0.01406446234703409 -0.0042290158833546664 4.0939474033052647e-016
		-0.013957421696608683 -0.0033820783833546676 4.0939474033052647e-016
		-0.013652572783644953 -0.0026640783833546677 4.0939474033052647e-016
		-0.013196331992591357 -0.0021843283833546667 4.0939474033052647e-016
		;
createNode transform -n "L_Blid_E_Pose" -p "Eye__Wr_Gro";
	rename -uid "0ECEC947-4FC3-0BAC-9952-01B522B19B26";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.68303656578063965 14.029031185453368 1.4850989673405799 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_E_Mix" -p "L_Blid_E_Pose";
	rename -uid "B8639DFD-4E0E-5930-49D8-ECBCC14D8E40";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 2.2204460492503131e-016 1.7763568394002505e-015 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_E_Offset" -p "L_Blid_E_Mix";
	rename -uid "F69B4C04-4532-05AF-77EB-0DB9A8A75BE8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Blid_E_Sel" -p "L_Blid_E_Offset";
	rename -uid "9B2A91BF-4361-BE0B-9C9A-A08ED18FCAE0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "L_Blid_E_Sel_Shape" -p "L_Blid_E_Sel";
	rename -uid "396CBE15-42D4-08C9-2C90-8A8AEA42B2AD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591357 -0.0021843283833546667 4.0939474033052647e-016
		-0.012658160077587277 -0.0020158752583546713 4.0939474033052647e-016
		0.012658160077587185 -0.0020158752583546713 4.0939474033052647e-016
		0.013196331992591284 -0.0021843283833546667 4.0939474033052647e-016
		0.013652572783644864 -0.0026640783833546677 4.0939474033052647e-016
		0.013957421696608602 -0.0033820783833546676 4.0939474033052647e-016
		0.014064462347034012 -0.0042290158833546664 4.0939474033052647e-016
		0.014064462347034012 -0.019920531249997861 2.0122792321330957e-016
		0.013957421696608602 -0.020767468749997856 2.0122792321330957e-016
		0.013652572783644864 -0.021485468749997853 2.0122792321330957e-016
		0.013196331992591284 -0.021965218749997857 2.0122792321330957e-016
		0.012658160077587185 -0.022133671874997856 2.0122792321330957e-016
		-0.012658160077587277 -0.022133671874997856 2.0122792321330957e-016
		-0.013196331992591357 -0.021965218749997857 2.0122792321330957e-016
		-0.013652572783644953 -0.021485468749997853 2.0122792321330957e-016
		-0.013957421696608683 -0.020767468749997856 2.0122792321330957e-016
		-0.01406446234703409 -0.019920531249997861 2.0122792321330957e-016
		-0.01406446234703409 -0.0042290158833546664 4.0939474033052647e-016
		-0.013957421696608683 -0.0033820783833546676 4.0939474033052647e-016
		-0.013652572783644953 -0.0026640783833546677 4.0939474033052647e-016
		-0.013196331992591357 -0.0021843283833546667 4.0939474033052647e-016
		;
createNode transform -n "L_lid_Out_Pose" -p "Eye__Wr_Gro";
	rename -uid "84B73B27-44C4-D692-FC1C-98BCCDD8F64D";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.69165986776351929 14.028612045591307 1.4614126775532876 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_lid_Out_Mix" -p "L_lid_Out_Pose";
	rename -uid "93DBE903-4487-7398-8070-14B19A9E1C26";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1.7763568394002505e-015 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_lid_Out_Offset" -p "L_lid_Out_Mix";
	rename -uid "108B0E86-4A2A-E0C7-E2FC-9081699DC8FF";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_lid_Out_Sel" -p "L_lid_Out_Offset";
	rename -uid "4E6DB568-4D1A-D14D-33A1-2188DA2B99CB";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_lid_Out_Sel_Shape" -p "L_lid_Out_Sel";
	rename -uid "0807C8C9-41E9-58D8-ADA7-EBA02369F28D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 47 0 no 3
		48 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
		48
		-8.6736173798840355e-018 0.021560281875001967 7.6327832942979524e-017
		0.0037439015624999919 0.021232725937501969 7.6327832942979524e-017
		0.0073740459374999918 0.020260020000001967 7.6327832942979524e-017
		0.010780171874999994 0.018671730000001965 7.6327832942979524e-017
		0.013858679999999996 0.016516170000001967 7.6327832942979524e-017
		0.016516169999999997 0.013858680000001964 7.6327832942979524e-017
		0.018671729999999991 0.010780171875001965 7.6327832942979524e-017
		0.02026001999999999 0.0073740459375019624 7.6327832942979524e-017
		0.021232725937499988 0.0037439015625019647 7.6327832942979524e-017
		0.021560281874999993 1.9637069748057456e-015 7.6327832942979524e-017
		0.021232725937499988 -0.0037439015624980351 7.6327832942979524e-017
		0.02026001999999999 -0.0073740459374980385 7.6327832942979524e-017
		0.018671729999999991 -0.010780171874998036 7.6327832942979524e-017
		0.016516169999999997 -0.013858679999998036 7.6327832942979524e-017
		0.013858679999999996 -0.01651616999999804 7.6327832942979524e-017
		0.010780171874999994 -0.01867172999999803 7.6327832942979524e-017
		0.0073740459374999918 -0.020260019999998029 7.6327832942979524e-017
		0.0037439015624999919 -0.021232725937498031 7.6327832942979524e-017
		-8.6736173798840355e-018 -0.02156028187499804 7.6327832942979524e-017
		-0.0037439015625000075 -0.021232725937498031 7.6327832942979524e-017
		-0.0073740459375000074 -0.020260019999998029 7.6327832942979524e-017
		-0.010780171875000005 -0.01867172999999803 7.6327832942979524e-017
		-0.013858680000000003 -0.01651616999999804 7.6327832942979524e-017
		-0.016516170000000007 -0.013858679999998036 7.6327832942979524e-017
		-0.018671730000000011 -0.010780171874998036 7.6327832942979524e-017
		-0.020260020000000007 -0.0073740459374980385 7.6327832942979524e-017
		-0.021232725937500009 -0.0037439015624980351 7.6327832942979524e-017
		-0.021560281875000011 1.9637069748057456e-015 7.6327832942979524e-017
		-0.021232725937500009 0.0037439015625019647 7.6327832942979524e-017
		-0.020260020000000007 0.0073740459375019624 7.6327832942979524e-017
		-0.018671730000000011 0.010780171875001965 7.6327832942979524e-017
		-0.016516170000000007 0.013858680000001964 7.6327832942979524e-017
		-0.013858680000000003 0.016516170000001967 7.6327832942979524e-017
		-0.010780171875000005 0.018671730000001965 7.6327832942979524e-017
		-0.0073740459375000074 0.020260020000001967 7.6327832942979524e-017
		-0.0037439015625000075 0.021232725937501969 7.6327832942979524e-017
		-8.6736173798840355e-018 0.021560281875001967 7.6327832942979524e-017
		-8.6736173798840355e-018 -0.02156028187499804 7.6327832942979524e-017
		0.0037439015624999919 -0.021232725937498031 7.6327832942979524e-017
		0.0073740459374999918 -0.020260019999998029 7.6327832942979524e-017
		0.010780171874999994 -0.01867172999999803 7.6327832942979524e-017
		0.013858679999999996 -0.01651616999999804 7.6327832942979524e-017
		0.016516169999999997 -0.013858679999998036 7.6327832942979524e-017
		0.018671729999999991 -0.010780171874998036 7.6327832942979524e-017
		0.02026001999999999 -0.0073740459374980385 7.6327832942979524e-017
		0.021232725937499988 -0.0037439015624980351 7.6327832942979524e-017
		0.021560281874999993 1.9637069748057456e-015 7.6327832942979524e-017
		-0.021560281875000011 1.9637069748057456e-015 7.6327832942979524e-017
		;
createNode transform -n "L_lid_Inn_Pose" -p "Eye__Wr_Gro";
	rename -uid "09FB92CA-4057-A039-C2E8-19BC82B14CFE";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.31462252140045166 14.031264213865231 1.5312280748158609 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_lid_Inn_Mix" -p "L_lid_Inn_Pose";
	rename -uid "F565382E-4030-293C-0AE3-9CA2150D2C8D";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1.7763568394002505e-015 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_lid_Inn_Offset" -p "L_lid_Inn_Mix";
	rename -uid "CCD52210-46EE-00F5-69D1-2C805975295B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_lid_Inn_Sel" -p "L_lid_Inn_Offset";
	rename -uid "ADA56557-48C4-FF89-85B6-069E63933D9F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_lid_Inn_Sel_Shape" -p "L_lid_Inn_Sel";
	rename -uid "EDB232D2-455C-20D5-C30B-63B5F2F21A7D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 47 0 no 3
		48 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
		48
		4.5970172113385388e-017 0.021560281875001336 -5.2041704279304213e-017
		0.0037439015625000457 0.021232725937501334 -5.2041704279304213e-017
		0.0073740459375000447 0.020260020000001336 -5.2041704279304213e-017
		0.01078017187500005 0.018671730000001337 -5.2041704279304213e-017
		0.013858680000000049 0.016516170000001336 -5.2041704279304213e-017
		0.016516170000000045 0.013858680000001336 -5.2041704279304213e-017
		0.01867173000000005 0.010780171875001337 -5.2041704279304213e-017
		0.020260020000000045 0.0073740459375013327 -5.2041704279304213e-017
		0.021232725937500044 0.0037439015625013346 -5.2041704279304213e-017
		0.021560281875000052 1.3340023530261649e-015 -5.2041704279304213e-017
		0.021232725937500044 -0.0037439015624986666 -5.2041704279304213e-017
		0.020260020000000045 -0.0073740459374986647 -5.2041704279304213e-017
		0.01867173000000005 -0.010780171874998664 -5.2041704279304213e-017
		0.016516170000000045 -0.013858679999998666 -5.2041704279304213e-017
		0.013858680000000049 -0.016516169999998668 -5.2041704279304213e-017
		0.01078017187500005 -0.018671729999998669 -5.2041704279304213e-017
		0.0073740459375000447 -0.020260019999998668 -5.2041704279304213e-017
		0.0037439015625000457 -0.021232725937498663 -5.2041704279304213e-017
		4.5970172113385388e-017 -0.021560281874998668 -5.2041704279304213e-017
		-0.0037439015624999555 -0.021232725937498663 -5.2041704279304213e-017
		-0.0073740459374999571 -0.020260019999998668 -5.2041704279304213e-017
		-0.010780171874999953 -0.018671729999998669 -5.2041704279304213e-017
		-0.013858679999999951 -0.016516169999998668 -5.2041704279304213e-017
		-0.016516169999999952 -0.013858679999998666 -5.2041704279304213e-017
		-0.018671729999999956 -0.010780171874998664 -5.2041704279304213e-017
		-0.020260019999999952 -0.0073740459374986647 -5.2041704279304213e-017
		-0.021232725937499954 -0.0037439015624986666 -5.2041704279304213e-017
		-0.021560281874999952 1.3340023530261649e-015 -5.2041704279304213e-017
		-0.021232725937499954 0.0037439015625013346 -5.2041704279304213e-017
		-0.020260019999999952 0.0073740459375013327 -5.2041704279304213e-017
		-0.018671729999999956 0.010780171875001337 -5.2041704279304213e-017
		-0.016516169999999952 0.013858680000001336 -5.2041704279304213e-017
		-0.013858679999999951 0.016516170000001336 -5.2041704279304213e-017
		-0.010780171874999953 0.018671730000001337 -5.2041704279304213e-017
		-0.0073740459374999571 0.020260020000001336 -5.2041704279304213e-017
		-0.0037439015624999555 0.021232725937501334 -5.2041704279304213e-017
		4.5970172113385388e-017 0.021560281875001336 -5.2041704279304213e-017
		4.5970172113385388e-017 -0.021560281874998668 -5.2041704279304213e-017
		0.0037439015625000457 -0.021232725937498663 -5.2041704279304213e-017
		0.0073740459375000447 -0.020260019999998668 -5.2041704279304213e-017
		0.01078017187500005 -0.018671729999998669 -5.2041704279304213e-017
		0.013858680000000049 -0.016516169999998668 -5.2041704279304213e-017
		0.016516170000000045 -0.013858679999998666 -5.2041704279304213e-017
		0.01867173000000005 -0.010780171874998664 -5.2041704279304213e-017
		0.020260020000000045 -0.0073740459374986647 -5.2041704279304213e-017
		0.021232725937500044 -0.0037439015624986666 -5.2041704279304213e-017
		0.021560281875000052 1.3340023530261649e-015 -5.2041704279304213e-017
		-0.021560281874999952 1.3340023530261649e-015 -5.2041704279304213e-017
		;
createNode transform -n "R_Tlid_A_Pose" -p "Eye__Wr_Gro";
	rename -uid "F43E77F7-45B1-AE1D-4D45-F69CA1080280";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.34366938471794123 14.032732395475341 1.5554930064946326 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_A_Mix" -p "R_Tlid_A_Pose";
	rename -uid "54011F36-44A4-59CC-6523-18B7341DD47E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_A_Offset" -p "R_Tlid_A_Mix";
	rename -uid "5FBC2751-41B7-6D7A-4965-D09C049BEC96";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_A_Sel" -p "R_Tlid_A_Offset";
	rename -uid "ED263CC5-4D00-9B65-79A8-B78EAA598D4B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Tlid_A_Sel_Shape" -p "R_Tlid_A_Sel";
	rename -uid "732D68F9-4413-A320-6789-2291E24ABC63";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591419 0.021965218750000248 8.3266726846886741e-017
		-0.012658160077587324 0.022133671875000246 8.3266726846886741e-017
		0.012658160077587133 0.022133671875000246 8.3266726846886741e-017
		0.01319633199259124 0.021965218750000248 8.3266726846886741e-017
		0.013652572783644814 0.021485468750000247 8.3266726846886741e-017
		0.013957421696608527 0.020767468750000247 8.3266726846886741e-017
		0.014064462347033966 0.019920531250000244 8.3266726846886741e-017
		0.014064462347033966 0.00062460586345708738 -1.2836953722228372e-016
		0.013957421696608527 -0.00022233163654291482 -1.2836953722228372e-016
		0.013652572783644814 -0.00094033163654291471 -1.2836953722228372e-016
		0.01319633199259124 -0.0014200816365429123 -1.2836953722228372e-016
		0.012658160077587133 -0.0015885347615429146 -1.2836953722228372e-016
		-0.012658160077587324 -0.0015885347615429146 -1.2836953722228372e-016
		-0.013196331992591419 -0.0014200816365429123 -1.2836953722228372e-016
		-0.013652572783645012 -0.00094033163654291471 -1.2836953722228372e-016
		-0.013957421696608747 -0.00022233163654291482 -1.2836953722228372e-016
		-0.014064462347034151 0.00062460586345708738 -1.2836953722228372e-016
		-0.014064462347034151 0.019920531250000244 8.3266726846886741e-017
		-0.013957421696608747 0.020767468750000247 8.3266726846886741e-017
		-0.013652572783645012 0.021485468750000247 8.3266726846886741e-017
		-0.013196331992591419 0.021965218750000248 8.3266726846886741e-017
		;
createNode transform -n "R_Tlid_B_Pose" -p "Eye__Wr_Gro";
	rename -uid "9618C5E8-4081-A88C-0A87-BD97647844E9";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.3867969810962677 14.031530288999512 1.5959382150441319 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_B_Mix" -p "R_Tlid_B_Pose";
	rename -uid "79AA3F56-4E92-3375-701C-81880C1C6A3E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_B_Offset" -p "R_Tlid_B_Mix";
	rename -uid "3C4203EB-4910-630A-3A06-4A9D282AD2C0";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_B_Sel" -p "R_Tlid_B_Offset";
	rename -uid "1FA8361B-4C1A-3AF3-1AA6-74AA7FD53DCD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Tlid_B_Sel_Shape" -p "R_Tlid_B_Sel";
	rename -uid "408D1ADD-426A-6B09-A0C9-45B50C3853A2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591282 0.021965218749998992 6.2450045135165055e-017
		-0.01265816007758718 0.022133671874998991 6.2450045135165055e-017
		0.012658160077587277 0.022133671874998991 6.2450045135165055e-017
		0.013196331992591358 0.021965218749998992 6.2450045135165055e-017
		0.013652572783644968 0.021485468749998991 6.2450045135165055e-017
		0.01395742169660869 0.020767468749998991 6.2450045135165055e-017
		0.014064462347034094 0.019920531249998989 6.2450045135165055e-017
		0.014064462347034094 0.00062460586345583144 -1.5265566588595902e-016
		0.01395742169660869 -0.00022233163654416729 -1.5265566588595902e-016
		0.013652572783644968 -0.00094033163654417065 -1.5265566588595902e-016
		0.013196331992591358 -0.0014200816365441682 -1.5265566588595902e-016
		0.012658160077587277 -0.0015885347615441706 -1.5265566588595902e-016
		-0.01265816007758718 -0.0015885347615441706 -1.4918621893400541e-016
		-0.013196331992591282 -0.0014200816365441682 -1.4918621893400541e-016
		-0.013652572783644856 -0.00094033163654417065 -1.4918621893400541e-016
		-0.013957421696608586 -0.00022233163654416729 -1.4918621893400541e-016
		-0.014064462347034 0.00062460586345583144 -1.4918621893400541e-016
		-0.014064462347034 0.019920531249998989 6.2450045135165055e-017
		-0.013957421696608586 0.020767468749998991 6.2450045135165055e-017
		-0.013652572783644856 0.021485468749998991 6.2450045135165055e-017
		-0.013196331992591282 0.021965218749998992 6.2450045135165055e-017
		;
createNode transform -n "R_Tlid_C_Pose" -p "Eye__Wr_Gro";
	rename -uid "3C4D47F5-4493-6FD0-D833-639293E3A37B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.52614259719848622 14.030793098752929 1.6275513265401038 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_C_Mix" -p "R_Tlid_C_Pose";
	rename -uid "DCDB777C-4653-685E-938A-B5A5A6F4909F";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -3.5527136788005009e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_C_Offset" -p "R_Tlid_C_Mix";
	rename -uid "ED35765D-4CE1-B1CB-6CF5-0294285AA22B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_C_Sel" -p "R_Tlid_C_Offset";
	rename -uid "0BA5E385-4EE9-15B2-3EC6-C1A235CE1F5F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Tlid_C_Sel_Shape" -p "R_Tlid_C_Sel";
	rename -uid "4DAC187A-473F-DBA3-B82A-A3942E67A01F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591296 0.021965218750000945 8.3266726846886741e-017
		-0.012658160077587206 0.02213367187500094 8.3266726846886741e-017
		0.012658160077587252 0.02213367187500094 8.3266726846886741e-017
		0.013196331992591346 0.021965218750000945 8.3266726846886741e-017
		0.013652572783644932 0.02148546875000094 8.3266726846886741e-017
		0.013957421696608661 0.020767468750000941 8.3266726846886741e-017
		0.014064462347034077 0.019920531250000945 8.3266726846886741e-017
		0.014064462347034077 0.00062460586345777086 -1.3183898417423734e-016
		0.013957421696608661 -0.0002223316365422244 -1.3183898417423734e-016
		0.013652572783644932 -0.00094033163654222429 -1.3183898417423734e-016
		0.013196331992591346 -0.0014200816365422288 -1.3183898417423734e-016
		0.012658160077587252 -0.0015885347615422242 -1.3183898417423734e-016
		-0.012658160077587207 -0.0015885347615422242 -1.3183898417423734e-016
		-0.013196331992591298 -0.0014200816365422288 -1.3183898417423734e-016
		-0.01365257278364488 -0.00094033163654222429 -1.3183898417423734e-016
		-0.013957421696608616 -0.0002223316365422244 -1.3183898417423734e-016
		-0.014064462347034032 0.00062460586345777086 -1.3183898417423734e-016
		-0.014064462347034032 0.019920531250000945 8.3266726846886741e-017
		-0.013957421696608616 0.020767468750000941 8.3266726846886741e-017
		-0.01365257278364488 0.02148546875000094 8.3266726846886741e-017
		-0.013196331992591296 0.021965218750000945 8.3266726846886741e-017
		;
createNode transform -n "R_Tlid_D_Pose" -p "Eye__Wr_Gro";
	rename -uid "C43B1CE9-4896-15EE-2500-229DFCE2CBE3";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.65386086702346791 14.03189363891406 1.5413129422932776 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_D_Mix" -p "R_Tlid_D_Pose";
	rename -uid "EF018B32-4559-AB99-E22A-15AF276AF6E2";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.1102230246251563e-016 -1.7763568394002505e-015 2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_D_Offset" -p "R_Tlid_D_Mix";
	rename -uid "A7EF986E-421A-442B-D2D1-37B9C00DCC5F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_D_Sel" -p "R_Tlid_D_Offset";
	rename -uid "69F118B3-49B8-63EF-D269-02B82A2F03CD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Tlid_D_Sel_Shape" -p "R_Tlid_D_Sel";
	rename -uid "4515AF72-4817-CAB4-8FBA-539DBE7BF70C";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591286 0.021965218750000945 8.3266726846886741e-017
		-0.012658160077587178 0.02213367187500094 8.3266726846886741e-017
		0.012658160077587277 0.02213367187500094 8.3266726846886741e-017
		0.013196331992591364 0.021965218750000945 8.3266726846886741e-017
		0.013652572783644958 0.02148546875000094 8.3266726846886741e-017
		0.013957421696608676 0.020767468750000941 8.3266726846886741e-017
		0.014064462347034092 0.019920531250000945 8.3266726846886741e-017
		0.014064462347034092 0.00062460586345777086 -1.3183898417423734e-016
		0.013957421696608676 -0.0002223316365422244 -1.3183898417423734e-016
		0.013652572783644958 -0.00094033163654222429 -1.3183898417423734e-016
		0.013196331992591364 -0.0014200816365422288 -1.3183898417423734e-016
		0.012658160077587277 -0.0015885347615422242 -1.3183898417423734e-016
		-0.012658160077587185 -0.0015885347615422242 -1.3183898417423734e-016
		-0.013196331992591287 -0.0014200816365422288 -1.3183898417423734e-016
		-0.013652572783644864 -0.00094033163654222429 -1.3183898417423734e-016
		-0.013957421696608597 -0.0002223316365422244 -1.3183898417423734e-016
		-0.014064462347034012 0.00062460586345777086 -1.3183898417423734e-016
		-0.014064462347034012 0.019920531250000945 8.3266726846886741e-017
		-0.013957421696608597 0.020767468750000941 8.3266726846886741e-017
		-0.013652572783644864 0.02148546875000094 8.3266726846886741e-017
		-0.013196331992591286 0.021965218750000945 8.3266726846886741e-017
		;
createNode transform -n "R_Tlid_E_Pose" -p "Eye__Wr_Gro";
	rename -uid "7BC6C0EF-4725-389E-26BC-20B6DB928392";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.68304216861724831 14.030395893400144 1.4853673074513585 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_E_Mix" -p "R_Tlid_E_Pose";
	rename -uid "9F59A3F1-41C6-C20A-10D3-E2A3750D6BCA";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -1.1102230246251563e-016 5.2939559203393771e-023 6.6613381477509392e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_E_Offset" -p "R_Tlid_E_Mix";
	rename -uid "9C7133D2-4214-6162-A4A4-D6ADA751A067";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Tlid_E_Sel" -p "R_Tlid_E_Offset";
	rename -uid "B9B9AFB9-428C-F0BC-1E87-419AFEBCBA8F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Tlid_E_Sel_Shape" -p "R_Tlid_E_Sel";
	rename -uid "92893BD4-4DC8-1452-13CD-89A74D76D746";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591286 0.021965218750000945 8.3266726846886741e-017
		-0.012658160077587178 0.02213367187500094 8.3266726846886741e-017
		0.012658160077587277 0.02213367187500094 8.3266726846886741e-017
		0.013196331992591364 0.021965218750000945 8.3266726846886741e-017
		0.013652572783644958 0.02148546875000094 8.3266726846886741e-017
		0.013957421696608676 0.020767468750000941 8.3266726846886741e-017
		0.014064462347034092 0.019920531250000945 8.3266726846886741e-017
		0.014064462347034092 0.00062460586345777086 -1.3183898417423734e-016
		0.013957421696608676 -0.0002223316365422244 -1.3183898417423734e-016
		0.013652572783644958 -0.00094033163654222429 -1.3183898417423734e-016
		0.013196331992591364 -0.0014200816365422288 -1.3183898417423734e-016
		0.012658160077587277 -0.0015885347615422242 -1.3183898417423734e-016
		-0.012658160077587185 -0.0015885347615422242 -1.3183898417423734e-016
		-0.013196331992591287 -0.0014200816365422288 -1.3183898417423734e-016
		-0.013652572783644864 -0.00094033163654222429 -1.3183898417423734e-016
		-0.013957421696608597 -0.0002223316365422244 -1.3183898417423734e-016
		-0.014064462347034012 0.00062460586345777086 -1.3183898417423734e-016
		-0.014064462347034012 0.019920531250000945 8.3266726846886741e-017
		-0.013957421696608597 0.020767468750000941 8.3266726846886741e-017
		-0.013652572783644864 0.02148546875000094 8.3266726846886741e-017
		-0.013196331992591286 0.021965218750000945 8.3266726846886741e-017
		;
createNode transform -n "R_Blid_A_Pose" -p "Eye__Wr_Gro";
	rename -uid "B8094FC1-413C-470B-7C40-4E8CCA5A15D5";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.34365963935852045 14.030704883878659 1.5556809995442542 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_A_Mix" -p "R_Blid_A_Pose";
	rename -uid "67614F18-44E8-EADC-80A1-0F8B449FB4B4";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_A_Offset" -p "R_Blid_A_Mix";
	rename -uid "90143062-45DF-407E-7F26-8AA0FE19D291";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_A_Sel" -p "R_Blid_A_Offset";
	rename -uid "2D29672D-4B81-2D27-50AC-5F83678DA0CA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Blid_A_Sel_Shape" -p "R_Blid_A_Sel";
	rename -uid "97AD8816-440F-A1E5-4CB2-9697FB1848B8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591312 -0.0021843283833572688 2.1163626406917047e-016
		-0.012658160077587214 -0.0020158752583572664 2.1163626406917047e-016
		0.012658160077587244 -0.0020158752583572664 2.1163626406917047e-016
		0.013196331992591346 -0.0021843283833572688 2.1163626406917047e-016
		0.013652572783644932 -0.0026640783833572663 2.1163626406917047e-016
		0.013957421696608656 -0.0033820783833572697 2.1163626406917047e-016
		0.014064462347034077 -0.0042290158833572719 2.1163626406917047e-016
		0.014064462347034077 -0.019920531250000467 3.4694469519536142e-018
		0.013957421696608656 -0.020767468750000465 3.4694469519536142e-018
		0.013652572783644932 -0.021485468750000465 3.4694469519536142e-018
		0.013196331992591346 -0.021965218750000463 3.4694469519536142e-018
		0.012658160077587244 -0.022133671875000465 3.4694469519536142e-018
		-0.012658160077587214 -0.022133671875000465 3.4694469519536142e-018
		-0.013196331992591312 -0.021965218750000463 3.4694469519536142e-018
		-0.01365257278364488 -0.021485468750000465 3.4694469519536142e-018
		-0.013957421696608616 -0.020767468750000465 3.4694469519536142e-018
		-0.014064462347034032 -0.019920531250000467 3.4694469519536142e-018
		-0.014064462347034032 -0.0042290158833572719 2.1163626406917047e-016
		-0.013957421696608616 -0.0033820783833572697 2.1163626406917047e-016
		-0.01365257278364488 -0.0026640783833572663 2.1163626406917047e-016
		-0.013196331992591312 -0.0021843283833572688 2.1163626406917047e-016
		;
createNode transform -n "R_Blid_B_Pose" -p "Eye__Wr_Gro";
	rename -uid "98370F0F-41FC-E77B-98C3-A4BBBAD4FFED";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.38698843121528614 14.029996780698728 1.5950960014134561 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 29.999999999999996 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_B_Mix" -p "R_Blid_B_Pose";
	rename -uid "12EB79F0-41AD-8E55-1CA2-8DB804C954DC";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 2.2204460492503131e-016 -3.5527136788005009e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_B_Offset" -p "R_Blid_B_Mix";
	rename -uid "A6B3244C-4D52-C062-E5D6-3B91B567BA77";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_B_Sel" -p "R_Blid_B_Offset";
	rename -uid "0073E2C4-4760-322C-2ABD-8FB1480EA12E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Blid_B_Sel_Shape" -p "R_Blid_B_Sel";
	rename -uid "D571306E-4004-09AC-11E5-C3872E8AD417";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591268 -0.0021843283833567484 2.1510571102112408e-016
		-0.012658160077587164 -0.002015875258356746 2.1510571102112408e-016
		0.012658160077587287 -0.002015875258356746 2.1510571102112408e-016
		0.013196331992591378 -0.0021843283833567484 2.1510571102112408e-016
		0.013652572783644972 -0.0026640783833567459 2.1510571102112408e-016
		0.013957421696608694 -0.0033820783833567458 2.1510571102112408e-016
		0.01406446234703411 -0.004229015883356748 2.1510571102112408e-016
		0.01406446234703411 -0.019920531249999929 0
		0.013957421696608694 -0.020767468749999924 0
		0.013652572783644972 -0.021485468749999927 0
		0.013196331992591378 -0.021965218749999925 0
		0.012658160077587287 -0.022133671874999924 0
		-0.012658160077587164 -0.022133671874999924 0
		-0.013196331992591268 -0.021965218749999925 0
		-0.01365257278364485 -0.021485468749999927 0
		-0.013957421696608576 -0.020767468749999924 0
		-0.014064462347033986 -0.019920531249999929 0
		-0.014064462347033986 -0.004229015883356748 2.1510571102112408e-016
		-0.013957421696608576 -0.0033820783833567458 2.1510571102112408e-016
		-0.01365257278364485 -0.0026640783833567459 2.1510571102112408e-016
		-0.013196331992591268 -0.0021843283833567484 2.1510571102112408e-016
		;
createNode transform -n "R_Blid_C_Pose" -p "Eye__Wr_Gro";
	rename -uid "1D171562-42BC-8BBD-EF6C-65ADC33E406F";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.52584892511367787 14.029387382810546 1.6256134603291663 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_C_Mix" -p "R_Blid_C_Pose";
	rename -uid "05F2C4E2-4D92-E3E2-0FC1-71A661339BED";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -3.5527136788005009e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_C_Offset" -p "R_Blid_C_Mix";
	rename -uid "D784CC41-40FF-89A5-9EDB-EDB5AF584B56";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_C_Sel" -p "R_Blid_C_Offset";
	rename -uid "9089E5A5-48F4-C0F0-418D-BEB70678AF5E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Blid_C_Sel_Shape" -p "R_Blid_C_Sel";
	rename -uid "B5D62CA0-41A1-7FB1-81C0-C7B8A2846919";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591293 -0.0021843283833548124 2.4980018054066022e-016
		-0.012658160077587195 -0.0020158752583548205 2.4980018054066022e-016
		0.012658160077587254 -0.0020158752583548205 2.4286128663675299e-016
		0.013196331992591348 -0.0021843283833548124 2.4286128663675299e-016
		0.013652572783644941 -0.00266407838335481 2.4286128663675299e-016
		0.013957421696608666 -0.0033820783833548203 2.4286128663675299e-016
		0.014064462347034078 -0.0042290158833548121 2.4286128663675299e-016
		0.014064462347034078 -0.019920531249998021 2.7755575615628914e-017
		0.013957421696608666 -0.020767468749998016 2.7755575615628914e-017
		0.013652572783644941 -0.021485468749998012 2.7755575615628914e-017
		0.013196331992591348 -0.021965218749998013 2.7755575615628914e-017
		0.012658160077587254 -0.022133671874998016 2.7755575615628914e-017
		-0.012658160077587195 -0.022133671874998016 3.1225022567582528e-017
		-0.013196331992591293 -0.021965218749998013 3.1225022567582528e-017
		-0.013652572783644871 -0.021485468749998012 3.1225022567582528e-017
		-0.013957421696608614 -0.020767468749998016 3.1225022567582528e-017
		-0.014064462347034016 -0.019920531249998021 3.1225022567582528e-017
		-0.014064462347034016 -0.0042290158833548121 2.4980018054066022e-016
		-0.013957421696608614 -0.0033820783833548203 2.4980018054066022e-016
		-0.013652572783644871 -0.00266407838335481 2.4980018054066022e-016
		-0.013196331992591293 -0.0021843283833548124 2.4980018054066022e-016
		;
createNode transform -n "R_Blid_D_Pose" -p "Eye__Wr_Gro";
	rename -uid "296C114A-49B9-868F-AFC3-5AAF2D6563C2";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.65399414300918557 14.030682472532224 1.540905246523014 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_D_Mix" -p "R_Blid_D_Pose";
	rename -uid "26DA8318-4CE4-EFCA-0883-E9B82A226DD6";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 2.2204460492503131e-016 -1.7763568394002505e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_D_Offset" -p "R_Blid_D_Mix";
	rename -uid "D1C63F5E-4CAE-60FA-1905-BA945350C12E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_D_Sel" -p "R_Blid_D_Offset";
	rename -uid "3B60998E-4164-A277-FAFA-D8B0DF35C5DD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Blid_D_Sel_Shape" -p "R_Blid_D_Sel";
	rename -uid "0C6BEEEE-43C0-02FE-B92A-539D8433B04A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591284 -0.0021843283833548124 2.4980018054066022e-016
		-0.012658160077587173 -0.0020158752583548205 2.4980018054066022e-016
		0.01265816007758728 -0.0020158752583548205 2.4286128663675299e-016
		0.013196331992591379 -0.0021843283833548124 2.4286128663675299e-016
		0.01365257278364496 -0.00266407838335481 2.4286128663675299e-016
		0.013957421696608676 -0.0033820783833548203 2.4286128663675299e-016
		0.014064462347034104 -0.0042290158833548121 2.4286128663675299e-016
		0.014064462347034104 -0.019920531249998021 2.7755575615628914e-017
		0.013957421696608676 -0.020767468749998016 2.7755575615628914e-017
		0.01365257278364496 -0.021485468749998012 2.7755575615628914e-017
		0.013196331992591379 -0.021965218749998013 2.7755575615628914e-017
		0.01265816007758728 -0.022133671874998016 2.7755575615628914e-017
		-0.012658160077587173 -0.022133671874998016 3.1225022567582528e-017
		-0.013196331992591284 -0.021965218749998013 3.1225022567582528e-017
		-0.01365257278364485 -0.021485468749998012 3.1225022567582528e-017
		-0.013957421696608591 -0.020767468749998016 3.1225022567582528e-017
		-0.014064462347033997 -0.019920531249998021 3.1225022567582528e-017
		-0.014064462347033997 -0.0042290158833548121 2.4980018054066022e-016
		-0.013957421696608591 -0.0033820783833548203 2.4980018054066022e-016
		-0.01365257278364485 -0.00266407838335481 2.4980018054066022e-016
		-0.013196331992591284 -0.0021843283833548124 2.4980018054066022e-016
		;
createNode transform -n "R_Blid_E_Pose" -p "Eye__Wr_Gro";
	rename -uid "59930951-4886-8E9F-677B-6DAC845C6655";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.68303656578063954 14.029031185453368 1.4850989673405799 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -47.458356433377645 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_E_Mix" -p "R_Blid_E_Pose";
	rename -uid "C367BBEE-4346-1701-36FB-8BA4E70A43DD";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_E_Offset" -p "R_Blid_E_Mix";
	rename -uid "45747280-4B4F-A56E-2938-67A4DE57A672";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Blid_E_Sel" -p "R_Blid_E_Offset";
	rename -uid "A767EBE1-41DF-6874-E859-E6A5986F1F2A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_Blid_E_Sel_Shape" -p "R_Blid_E_Sel";
	rename -uid "C393DB7E-48DD-C646-2ABC-EAA6FB5A7A42";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.013196331992591293 -0.0021843283833548124 2.4980018054066022e-016
		-0.012658160077587195 -0.0020158752583548205 2.4980018054066022e-016
		0.012658160077587254 -0.0020158752583548205 2.4286128663675299e-016
		0.013196331992591348 -0.0021843283833548124 2.4286128663675299e-016
		0.013652572783644941 -0.00266407838335481 2.4286128663675299e-016
		0.013957421696608666 -0.0033820783833548203 2.4286128663675299e-016
		0.014064462347034078 -0.0042290158833548121 2.4286128663675299e-016
		0.014064462347034078 -0.019920531249998021 2.7755575615628914e-017
		0.013957421696608666 -0.020767468749998016 2.7755575615628914e-017
		0.013652572783644941 -0.021485468749998012 2.7755575615628914e-017
		0.013196331992591348 -0.021965218749998013 2.7755575615628914e-017
		0.012658160077587254 -0.022133671874998016 2.7755575615628914e-017
		-0.012658160077587195 -0.022133671874998016 3.1225022567582528e-017
		-0.013196331992591293 -0.021965218749998013 3.1225022567582528e-017
		-0.013652572783644871 -0.021485468749998012 3.1225022567582528e-017
		-0.013957421696608614 -0.020767468749998016 3.1225022567582528e-017
		-0.014064462347034016 -0.019920531249998021 3.1225022567582528e-017
		-0.014064462347034016 -0.0042290158833548121 2.4980018054066022e-016
		-0.013957421696608614 -0.0033820783833548203 2.4980018054066022e-016
		-0.013652572783644871 -0.00266407838335481 2.4980018054066022e-016
		-0.013196331992591293 -0.0021843283833548124 2.4980018054066022e-016
		;
createNode transform -n "R_lid_Out_Pose" -p "Eye__Wr_Gro";
	rename -uid "087FF493-4FDD-45EE-F862-97B901F8EBD5";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.69165986776351907 14.028612045591307 1.4614126775532874 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_lid_Out_Mix" -p "R_lid_Out_Pose";
	rename -uid "6F15738F-452D-1148-234F-1BB02070C7D0";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.1102230246251563e-016 -1.7763568394002505e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_lid_Out_Offset" -p "R_lid_Out_Mix";
	rename -uid "0E0691E9-46DF-BD14-503F-0EBE84ADFE3F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_lid_Out_Sel" -p "R_lid_Out_Offset";
	rename -uid "A14CF73B-4B57-D96B-8FF0-87814A22A4F7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_lid_Out_Sel_Shape" -p "R_lid_Out_Sel";
	rename -uid "C8BBB4B3-47BA-AD7B-1930-A39711B927B5";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 47 0 no 3
		48 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
		48
		2.8622937353617317e-017 0.021560281875002089 -6.591949208711867e-017
		0.0037439015625000283 0.021232725937502087 -6.591949208711867e-017
		0.0073740459375000282 0.020260020000002085 -6.591949208711867e-017
		0.010780171875000024 0.01867173000000209 -6.591949208711867e-017
		0.013858680000000026 0.016516170000002082 -6.591949208711867e-017
		0.016516170000000028 0.01385868000000208 -6.591949208711867e-017
		0.018671730000000025 0.010780171875002079 -6.2450045135165055e-017
		0.020260020000000028 0.0073740459375020778 -6.2450045135165055e-017
		0.021232725937500023 0.0037439015625020779 -6.2450045135165055e-017
		0.021560281875000028 2.0799334476961917e-015 -6.2450045135165055e-017
		0.021232725937500023 -0.0037439015624979198 -6.2450045135165055e-017
		0.020260020000000028 -0.0073740459374979197 -6.2450045135165055e-017
		0.018671730000000025 -0.010780171874997919 -6.2450045135165055e-017
		0.016516170000000028 -0.013858679999997923 -6.2450045135165055e-017
		0.013858680000000026 -0.016516169999997929 -6.2450045135165055e-017
		0.010780171875000024 -0.018671729999997923 -6.2450045135165055e-017
		0.0073740459375000282 -0.020260019999997915 -6.2450045135165055e-017
		0.0037439015625000283 -0.021232725937497914 -6.2450045135165055e-017
		2.8622937353617317e-017 -0.021560281874997915 -6.2450045135165055e-017
		-0.0037439015624999711 -0.021232725937497914 -6.2450045135165055e-017
		-0.007374045937499971 -0.020260019999997915 -6.2450045135165055e-017
		-0.01078017187499997 -0.018671729999997923 -6.2450045135165055e-017
		-0.01385867999999997 -0.016516169999997929 -6.2450045135165055e-017
		-0.016516169999999969 -0.013858679999997923 -6.2450045135165055e-017
		-0.01867172999999997 -0.010780171874997919 -6.2450045135165055e-017
		-0.020260019999999969 -0.0073740459374979197 -6.2450045135165055e-017
		-0.021232725937499974 -0.0037439015624979198 -6.2450045135165055e-017
		-0.021560281874999969 2.0799334476961917e-015 -6.2450045135165055e-017
		-0.021232725937499974 0.0037439015625020779 -6.2450045135165055e-017
		-0.020260019999999969 0.0073740459375020778 -6.2450045135165055e-017
		-0.01867172999999997 0.010780171875002079 -6.2450045135165055e-017
		-0.016516169999999969 0.01385868000000208 -6.2450045135165055e-017
		-0.01385867999999997 0.016516170000002082 -6.2450045135165055e-017
		-0.01078017187499997 0.01867173000000209 -6.2450045135165055e-017
		-0.007374045937499971 0.020260020000002085 -6.2450045135165055e-017
		-0.0037439015624999711 0.021232725937502087 -6.2450045135165055e-017
		2.8622937353617317e-017 0.021560281875002089 -6.591949208711867e-017
		2.8622937353617317e-017 -0.021560281874997915 -6.2450045135165055e-017
		0.0037439015625000283 -0.021232725937497914 -6.2450045135165055e-017
		0.0073740459375000282 -0.020260019999997915 -6.2450045135165055e-017
		0.010780171875000024 -0.018671729999997923 -6.2450045135165055e-017
		0.013858680000000026 -0.016516169999997929 -6.2450045135165055e-017
		0.016516170000000028 -0.013858679999997923 -6.2450045135165055e-017
		0.018671730000000025 -0.010780171874997919 -6.2450045135165055e-017
		0.020260020000000028 -0.0073740459374979197 -6.2450045135165055e-017
		0.021232725937500023 -0.0037439015624979198 -6.2450045135165055e-017
		0.021560281875000028 2.0799334476961917e-015 -6.2450045135165055e-017
		-0.021560281874999969 2.0799334476961917e-015 -6.2450045135165055e-017
		;
createNode transform -n "R_lid_Inn_Pose" -p "Eye__Wr_Gro";
	rename -uid "C833F0E8-4357-DE8C-714B-CBAAC206F7D6";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.3146225214004516 14.031264213865231 1.5312280748158609 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_lid_Inn_Mix" -p "R_lid_Inn_Pose";
	rename -uid "8F23B053-4A89-3E38-4967-C99C3A59C05F";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -5.5511151231257827e-017 -1.7763568394002505e-015 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_lid_Inn_Offset" -p "R_lid_Inn_Mix";
	rename -uid "B0F5BDE7-4B29-2533-652C-60BCD26CA3BC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_lid_Inn_Sel" -p "R_lid_Inn_Offset";
	rename -uid "696138CD-42A9-F91D-617A-4582B7DE8AF3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".liw" yes;
createNode nurbsCurve -n "R_lid_Inn_Sel_Shape" -p "R_lid_Inn_Sel";
	rename -uid "70378F0F-4FC2-E02E-5708-F2AF609C2666";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 47 0 no 3
		48 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
		48
		1.1275702593849246e-017 0.021560281875000437 5.8980598183211441e-017
		0.0037439015625000127 0.021232725937500439 5.8980598183211441e-017
		0.0073740459375000109 0.020260020000000437 5.5511151231257827e-017
		0.010780171875000017 0.018671730000000435 5.5511151231257827e-017
		0.01385868000000001 0.016516170000000434 5.5511151231257827e-017
		0.016516170000000018 0.013858680000000435 5.8980598183211441e-017
		0.018671730000000008 0.010780171875000437 5.8980598183211441e-017
		0.020260020000000007 0.0073740459375004359 5.8980598183211441e-017
		0.021232725937500009 0.0037439015625004395 5.8980598183211441e-017
		0.021560281875000017 4.3888503942213219e-016 5.8980598183211441e-017
		0.021232725937500009 -0.00374390156249956 5.8980598183211441e-017
		0.020260020000000007 -0.0073740459374995598 5.8980598183211441e-017
		0.018671730000000008 -0.010780171874999561 5.8980598183211441e-017
		0.016516170000000018 -0.013858679999999558 5.8980598183211441e-017
		0.01385868000000001 -0.016516169999999566 5.8980598183211441e-017
		0.010780171875000017 -0.01867172999999956 5.8980598183211441e-017
		0.0073740459375000109 -0.020260019999999553 5.8980598183211441e-017
		0.0037439015625000127 -0.021232725937499555 5.8980598183211441e-017
		1.1275702593849246e-017 -0.021560281874999553 5.8980598183211441e-017
		-0.0037439015624999867 -0.021232725937499555 5.8980598183211441e-017
		-0.0073740459374999883 -0.020260019999999553 5.8980598183211441e-017
		-0.010780171874999986 -0.01867172999999956 5.8980598183211441e-017
		-0.013858679999999984 -0.016516169999999566 5.8980598183211441e-017
		-0.016516169999999986 -0.013858679999999558 5.8980598183211441e-017
		-0.018671729999999984 -0.010780171874999561 5.8980598183211441e-017
		-0.020260019999999983 -0.0073740459374995598 5.8980598183211441e-017
		-0.021232725937499985 -0.0037439015624995617 5.8980598183211441e-017
		-0.021560281874999979 4.3888503942213219e-016 5.8980598183211441e-017
		-0.021232725937499985 0.0037439015625004395 5.8980598183211441e-017
		-0.020260019999999983 0.0073740459375004359 5.8980598183211441e-017
		-0.018671729999999984 0.010780171875000437 5.8980598183211441e-017
		-0.016516169999999986 0.013858680000000435 5.8980598183211441e-017
		-0.013858679999999984 0.016516170000000434 5.8980598183211441e-017
		-0.010780171874999986 0.018671730000000435 5.8980598183211441e-017
		-0.0073740459374999883 0.020260020000000437 5.8980598183211441e-017
		-0.0037439015624999884 0.021232725937500439 5.8980598183211441e-017
		1.1275702593849246e-017 0.021560281875000437 5.8980598183211441e-017
		1.1275702593849246e-017 -0.021560281874999553 5.8980598183211441e-017
		0.0037439015625000127 -0.021232725937499555 5.8980598183211441e-017
		0.0073740459375000109 -0.020260019999999553 5.8980598183211441e-017
		0.010780171875000017 -0.01867172999999956 5.8980598183211441e-017
		0.01385868000000001 -0.016516169999999566 5.8980598183211441e-017
		0.016516170000000018 -0.013858679999999558 5.8980598183211441e-017
		0.018671730000000008 -0.010780171874999561 5.8980598183211441e-017
		0.020260020000000007 -0.0073740459374995598 5.8980598183211441e-017
		0.021232725937500009 -0.00374390156249956 5.8980598183211441e-017
		0.021560281875000017 4.3888503942213219e-016 5.8980598183211441e-017
		-0.021560281874999979 4.3888503942213219e-016 5.8980598183211441e-017
		;
createNode transform -n "Nose__Wr_Gro" -p "Face_Pose__Sel";
	rename -uid "178DA1F9-4F09-2544-2621-D29FB2213E5A";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_nose_Mid_Pose" -p "Nose__Wr_Gro";
	rename -uid "C9AAEF8E-4909-DA97-8426-36A883304866";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.22681662440299957 12.965101150815917 2.6175259444981727 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 359.99999999999989 9.541664044390544e-015 -6.3611093629270422e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_nose_Mid_Mix" -p "L_nose_Mid_Pose";
	rename -uid "2ADDD54A-466A-B82B-1633-7A86056BB8F9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_nose_Mid_Offset" -p "L_nose_Mid_Mix";
	rename -uid "638E2DD9-477A-7D6A-96B9-AA9A5E0361B1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_nose_Mid_Sel" -p "L_nose_Mid_Offset";
	rename -uid "74BD9267-427F-4F69-5829-03866684D96C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_nose_Mid_Sel_Shape" -p "L_nose_Mid_Sel";
	rename -uid "5C8822F0-4423-E22D-CF8B-87BF54121207";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.065837240080265133 0.051724102573295266
		0 0.065250588140715465 0.058429421762094501
		0 0.063508474017548652 0.064931002086643666
		0 0.060663850237625709 0.071031365898809318
		0 0.056803247177069693 0.07654496695344086
		0 0.05204368862736701 0.081304525503143488
		0 0.046530087572735405 0.08516512856369958
		0 0.040429723760569747 0.088009752343622447
		0 0.033928143436020547 0.089751866466789273
		0 0.027222824247221333 0.090338518406339011
		0 0.020517505058422085 0.089751866466789273
		0 0.014015924733872871 0.088009752343622447
		0 0.0079155609217072612 0.08516512856369958
		0 0.0024019598670756495 0.081304525503143488
		0 -0.0023575986826270372 0.07654496695344086
		0 -0.0062182017431830459 0.071031365898809318
		0 -0.0090628255231059544 0.064931002086643666
		0 -0.010804939646272819 0.058429421762094501
		0 -0.011391591585822517 0.051724102573295266
		0 -0.010804939646272819 0.045018783384496053
		0 -0.0090628255231059544 0.038517203059946867
		0 -0.0062182017431830459 0.032416839247781187
		0 -0.0023575986826270372 0.026903238193149617
		0 0.0024019598670756495 0.022143679643446965
		0 0.0079155609217072612 0.018283076582890911
		0 0.014015924733872871 0.015438452802968034
		0 0.020517505058422085 0.013696338679801179
		0 0.027222824247221333 0.013109686740251475
		0 0.033928143436020547 0.013696338679801179
		0 0.040429723760569747 0.015438452802968034
		0 0.046530087572735405 0.018283076582890911
		0 0.05204368862736701 0.022143679643446965
		0 0.056803247177069693 0.026903238193149617
		0 0.060663850237625709 0.032416839247781187
		0 0.063508474017548652 0.038517203059946867
		0 0.065250588140715465 0.045018783384496053
		0 0.065837240080265133 0.051724102573295266
		-0.0067053191887992232 0.065250588140715465 0.051724102573295266
		-0.013206899513348438 0.063508474017548652 0.051724102573295266
		-0.019307263325514096 0.060663850237625709 0.051724102573295266
		-0.024820864380145684 0.056803247177069693 0.051724102573295266
		-0.029580422929848357 0.05204368862736701 0.051724102573295266
		-0.033441025990404376 0.046530087572735405 0.051724102573295266
		-0.036285649770327277 0.040429723760569747 0.051724102573295266
		-0.038027763893494153 0.033928143436020547 0.051724102573295266
		-0.038614415833043841 0.027222824247221333 0.051724102573295266
		-0.038027763893494153 0.020517505058422085 0.051724102573295266
		-0.036285649770327277 0.014015924733872871 0.051724102573295266
		-0.033441025990404376 0.0079155609217072612 0.051724102573295266
		-0.029580422929848357 0.0024019598670756495 0.051724102573295266
		-0.024820864380145684 -0.0023575986826270372 0.051724102573295266
		-0.019307263325514096 -0.0062182017431830459 0.051724102573295266
		-0.013206899513348438 -0.0090628255231059544 0.051724102573295266
		-0.0067053191887992232 -0.010804939646272819 0.051724102573295266
		0 -0.011391591585822517 0.051724102573295266
		0.0067053191887992232 -0.010804939646272819 0.051724102573295266
		0.013206899513348438 -0.0090628255231059544 0.051724102573295266
		0.019307263325514096 -0.0062182017431830459 0.051724102573295266
		0.024820864380145684 -0.0023575986826270372 0.051724102573295266
		0.029580422929848357 0.0024019598670756495 0.051724102573295266
		0.033441025990404376 0.0079155609217072612 0.051724102573295266
		0.036285649770327277 0.014015924733872871 0.051724102573295266
		0.038027763893494153 0.020517505058422085 0.051724102573295266
		0.038614415833043841 0.027222824247221333 0.051724102573295266
		0.038027763893494153 0.033928143436020547 0.051724102573295266
		0.036285649770327277 0.040429723760569747 0.051724102573295266
		0.033441025990404376 0.046530087572735405 0.051724102573295266
		0.029580422929848357 0.05204368862736701 0.051724102573295266
		0.024820864380145684 0.056803247177069693 0.051724102573295266
		0.019307263325514096 0.060663850237625709 0.051724102573295266
		0.013206899513348438 0.063508474017548652 0.051724102573295266
		0.0067053191887992232 0.065250588140715465 0.051724102573295266
		0 0.065837240080265133 0.051724102573295266
		-0.0067053191887992232 0.065250588140715465 0.051724102573295266
		-0.013206899513348438 0.063508474017548652 0.051724102573295266
		-0.019307263325514096 0.060663850237625709 0.051724102573295266
		-0.024820864380145684 0.056803247177069693 0.051724102573295266
		-0.029580422929848357 0.05204368862736701 0.051724102573295266
		-0.033441025990404376 0.046530087572735405 0.051724102573295266
		-0.036285649770327277 0.040429723760569747 0.051724102573295266
		-0.038027763893494153 0.033928143436020547 0.051724102573295266
		-0.038614415833043841 0.027222824247221333 0.051724102573295266
		-0.038027763893494153 0.027222824247221333 0.045018783384496053
		-0.036285649770327277 0.027222824247221333 0.038517203059946867
		-0.033441025990404376 0.027222824247221333 0.032416839247781187
		-0.029580422929848357 0.027222824247221333 0.026903238193149617
		-0.024820864380145684 0.027222824247221333 0.022143679643446965
		-0.019307263325514096 0.027222824247221333 0.018283076582890911
		-0.013206899513348438 0.027222824247221333 0.015438452802968034
		-0.0067053191887992232 0.027222824247221333 0.013696338679801179
		0 0.027222824247221333 0.013109686740251475
		0.0067053191887992232 0.027222824247221333 0.013696338679801179
		0.013206899513348438 0.027222824247221333 0.015438452802968034
		0.019307263325514096 0.027222824247221333 0.018283076582890911
		0.024820864380145684 0.027222824247221333 0.022143679643446965
		0.029580422929848357 0.027222824247221333 0.026903238193149617
		0.033441025990404376 0.027222824247221333 0.032416839247781187
		0.036285649770327277 0.027222824247221333 0.038517203059946867
		0.038027763893494153 0.027222824247221333 0.045018783384496053
		0.038614415833043841 0.027222824247221333 0.051724102573295266
		0.038027763893494153 0.027222824247221333 0.058429421762094501
		0.036285649770327277 0.027222824247221333 0.064931002086643666
		0.033441025990404376 0.027222824247221333 0.071031365898809318
		0.029580422929848357 0.027222824247221333 0.07654496695344086
		0.024820864380145684 0.027222824247221333 0.081304525503143488
		0.019307263325514096 0.027222824247221333 0.08516512856369958
		0.013206899513348438 0.027222824247221333 0.088009752343622447
		0.0067053191887992232 0.027222824247221333 0.089751866466789273
		0 0.027222824247221333 0.090338518406339011
		-0.0067053191887992232 0.027222824247221333 0.089751866466789273
		-0.013206899513348438 0.027222824247221333 0.088009752343622447
		-0.019307263325514096 0.027222824247221333 0.08516512856369958
		-0.024820864380145684 0.027222824247221333 0.081304525503143488
		-0.029580422929848357 0.027222824247221333 0.07654496695344086
		-0.033441025990404376 0.027222824247221333 0.071031365898809318
		-0.036285649770327277 0.027222824247221333 0.064931002086643666
		-0.038027763893494153 0.027222824247221333 0.058429421762094501
		-0.038614415833043841 0.027222824247221333 0.051724102573295266
		;
createNode transform -n "R_nose_Mid_Pose" -p "Nose__Wr_Gro";
	rename -uid "242781D8-4F51-FE93-291C-F3B2B20E879E";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.22681662440299949 12.965101150815917 2.6175259444981727 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -3.1805546814635176e-015 9.5416640443905503e-015 -3.1805546814635176e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_nose_Mid_Mix" -p "R_nose_Mid_Pose";
	rename -uid "6EF80849-48E6-BEB8-EAAE-C89A9F94F7ED";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_nose_Mid_Offset" -p "R_nose_Mid_Mix";
	rename -uid "C25AE202-4B43-0FCE-3929-97B33374FC86";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_nose_Mid_Sel" -p "R_nose_Mid_Offset";
	rename -uid "F56EBEC7-4129-26AB-04D3-2EAC60CC1155";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_nose_Mid_Sel_Shape" -p "R_nose_Mid_Sel";
	rename -uid "C8200B6F-4A0B-6696-E220-A2A01BCED321";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 117 0 no 3
		118 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117
		118
		0 0.065983858498712328 0.051858087374233058
		0 0.065397206559162618 0.058563406563032293
		0 0.063655092435995764 0.065064986887581513
		0 0.060810468656072841 0.071165350699747179
		0 0.056949865595516846 0.076678951754378694
		0 0.052190307045814191 0.081438510304081405
		0 0.046676705991182565 0.085299113364637386
		0 0.040576342179016969 0.08814373714456035
		0 0.034074761854467714 0.089885851267727163
		0 0.027369442665668466 0.090472503207276886
		0 0.020664123476869262 0.089885851267727163
		0 0.014162543152320043 0.08814373714456035
		0 0.0080621793401544142 0.085299113364637386
		0 0.0025485782855228095 0.081438510304081405
		0 -0.0022109802641798668 0.076678951754378694
		0 -0.006071583324735879 0.071165350699747179
		0 -0.0089162071046587979 0.065064986887581513
		0 -0.010658321227825656 0.058563406563032293
		0 -0.011244973167375348 0.051858087374233058
		0 -0.010658321227825656 0.045152768185433838
		0 -0.0089162071046587979 0.03865118786088461
		0 -0.006071583324735879 0.032550824048718965
		0 -0.0022109802641798668 0.027037222994087361
		0 0.0025485782855228095 0.022277664444384705
		0 0.0080621793401544142 0.018417061383828683
		0 0.014162543152320043 0.015572437603905772
		0 0.020664123476869262 0.013830323480738912
		0 0.027369442665668466 0.013243671541189222
		0 0.034074761854467714 0.013830323480738912
		0 0.040576342179016969 0.015572437603905772
		0 0.046676705991182565 0.018417061383828683
		0 0.052190307045814191 0.022277664444384705
		0 0.056949865595516846 0.027037222994087361
		0 0.060810468656072841 0.032550824048718965
		0 0.063655092435995764 0.03865118786088461
		0 0.065397206559162618 0.045152768185433838
		0 0.065983858498712328 0.051858087374233058
		-0.0067053191887992232 0.065397206559162618 0.051858087374233058
		-0.013206899513348438 0.063655092435995764 0.051858087374233058
		-0.019307263325514096 0.060810468656072841 0.051858087374233058
		-0.024820864380145684 0.056949865595516846 0.051858087374233058
		-0.029580422929848357 0.052190307045814191 0.051858087374233058
		-0.033441025990404376 0.046676705991182565 0.051858087374233058
		-0.036285649770327277 0.040576342179016969 0.051858087374233058
		-0.038027763893494153 0.034074761854467714 0.051858087374233058
		-0.038614415833043841 0.027369442665668466 0.051858087374233058
		-0.038027763893494153 0.020664123476869262 0.051858087374233058
		-0.036285649770327277 0.014162543152320043 0.051858087374233058
		-0.033441025990404376 0.0080621793401544142 0.051858087374233058
		-0.029580422929848357 0.0025485782855228095 0.051858087374233058
		-0.024820864380145684 -0.0022109802641798668 0.051858087374233058
		-0.019307263325514096 -0.006071583324735879 0.051858087374233058
		-0.013206899513348438 -0.0089162071046587979 0.051858087374233058
		-0.0067053191887992232 -0.010658321227825656 0.051858087374233058
		0 -0.011244973167375348 0.051858087374233058
		0.0067053191887992232 -0.010658321227825656 0.051858087374233058
		0.013206899513348438 -0.0089162071046587979 0.051858087374233058
		0.019307263325514096 -0.006071583324735879 0.051858087374233058
		0.024820864380145684 -0.0022109802641798668 0.051858087374233058
		0.029580422929848357 0.0025485782855228095 0.051858087374233058
		0.033441025990404376 0.0080621793401544142 0.051858087374233058
		0.036285649770327277 0.014162543152320043 0.051858087374233058
		0.038027763893494153 0.020664123476869262 0.051858087374233058
		0.038614415833043841 0.027369442665668466 0.051858087374233058
		0.038027763893494153 0.034074761854467714 0.051858087374233058
		0.036285649770327277 0.040576342179016969 0.051858087374233058
		0.033441025990404376 0.046676705991182565 0.051858087374233058
		0.029580422929848357 0.052190307045814191 0.051858087374233058
		0.024820864380145684 0.056949865595516846 0.051858087374233058
		0.019307263325514096 0.060810468656072841 0.051858087374233058
		0.013206899513348438 0.063655092435995764 0.051858087374233058
		0.0067053191887992232 0.065397206559162618 0.051858087374233058
		0 0.065983858498712328 0.051858087374233058
		-0.0067053191887992232 0.065397206559162618 0.051858087374233058
		-0.013206899513348438 0.063655092435995764 0.051858087374233058
		-0.019307263325514096 0.060810468656072841 0.051858087374233058
		-0.024820864380145684 0.056949865595516846 0.051858087374233058
		-0.029580422929848357 0.052190307045814191 0.051858087374233058
		-0.033441025990404376 0.046676705991182565 0.051858087374233058
		-0.036285649770327277 0.040576342179016969 0.051858087374233058
		-0.038027763893494153 0.034074761854467714 0.051858087374233058
		-0.038614415833043841 0.027369442665668466 0.051858087374233058
		-0.038027763893494153 0.027369442665668466 0.045152768185433838
		-0.036285649770327277 0.027369442665668466 0.03865118786088461
		-0.033441025990404376 0.027369442665668466 0.032550824048718965
		-0.029580422929848357 0.027369442665668466 0.027037222994087361
		-0.024820864380145684 0.027369442665668466 0.022277664444384705
		-0.019307263325514096 0.027369442665668466 0.018417061383828683
		-0.013206899513348438 0.027369442665668466 0.015572437603905772
		-0.0067053191887992232 0.027369442665668466 0.013830323480738912
		0 0.027369442665668466 0.013243671541189222
		0.0067053191887992232 0.027369442665668466 0.013830323480738912
		0.013206899513348438 0.027369442665668466 0.015572437603905772
		0.019307263325514096 0.027369442665668466 0.018417061383828683
		0.024820864380145684 0.027369442665668466 0.022277664444384705
		0.029580422929848357 0.027369442665668466 0.027037222994087361
		0.033441025990404376 0.027369442665668466 0.032550824048718965
		0.036285649770327277 0.027369442665668466 0.03865118786088461
		0.038027763893494153 0.027369442665668466 0.045152768185433838
		0.038614415833043841 0.027369442665668466 0.051858087374233058
		0.038027763893494153 0.027369442665668466 0.058563406563032293
		0.036285649770327277 0.027369442665668466 0.065064986887581513
		0.033441025990404376 0.027369442665668466 0.071165350699747179
		0.029580422929848357 0.027369442665668466 0.076678951754378694
		0.024820864380145684 0.027369442665668466 0.081438510304081405
		0.019307263325514096 0.027369442665668466 0.085299113364637386
		0.013206899513348438 0.027369442665668466 0.08814373714456035
		0.0067053191887992232 0.027369442665668466 0.089885851267727163
		0 0.027369442665668466 0.090472503207276886
		-0.0067053191887992232 0.027369442665668466 0.089885851267727163
		-0.013206899513348438 0.027369442665668466 0.08814373714456035
		-0.019307263325514096 0.027369442665668466 0.085299113364637386
		-0.024820864380145684 0.027369442665668466 0.081438510304081405
		-0.029580422929848357 0.027369442665668466 0.076678951754378694
		-0.033441025990404376 0.027369442665668466 0.071165350699747179
		-0.036285649770327277 0.027369442665668466 0.065064986887581513
		-0.038027763893494153 0.027369442665668466 0.058563406563032293
		-0.038614415833043841 0.027369442665668466 0.051858087374233058
		;
createNode transform -n "Brow__Wr_Gro" -p "Face_Pose__Sel";
	rename -uid "2EEC71B4-472F-BA9A-0040-D48E9CBF98F5";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Inn_Pose" -p "Brow__Wr_Gro";
	rename -uid "9297E28B-4715-C37C-F418-D9B41449DA66";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.15036687254905701 14.323825744932126 1.7020493839055213 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Inn_Mix" -p "L_brow_Inn_Pose";
	rename -uid "E45F4568-4801-5A44-6733-7885869E2B27";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -5.5511151231257827e-017 0 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -4.336627014272433e-007 2.9238578556892461e-023 7.726037516061119e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Inn_Offset" -p "L_brow_Inn_Mix";
	rename -uid "A72A55AC-4C3A-9A40-ED5C-088B61147E3C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Inn_Sel" -p "L_brow_Inn_Offset";
	rename -uid "E327248B-4EB6-3D6F-6B91-94801331D477";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_brow_Inn_Sel_Shape" -p "L_brow_Inn_Sel";
	rename -uid "D77671D9-4175-95D9-DDCD-5C931C5FE9B8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.03791279999999999 0 0.065222343601349264
		-0.037336799999999989 0.0065834999999999999 0.065222343601349264
		-0.035626349999999987 0.01296695 0.065222343601349264
		-0.032833399999999985 0.01895645 0.065222343601349264
		-0.029042949999999988 0.0243699 0.065222343601349264
		-0.024369899999999983 0.029042950000000001 0.065222343601349264
		-0.018956449999999982 0.032833399999999999 0.065222343601349264
		-0.012966949999999986 0.035626350000000001 0.065222343601349264
		-0.0065834999999999861 0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 0.037912800000000003 0.065222343601349264
		0.0065835000000000138 0.037336800000000003 0.065222343601349264
		0.012966950000000014 0.035626350000000001 0.065222343601349264
		0.018956450000000017 0.032833399999999999 0.065222343601349264
		0.024369900000000017 0.029042950000000001 0.065222343601349264
		0.029042950000000015 0.0243699 0.065222343601349264
		0.032833400000000013 0.01895645 0.065222343601349264
		0.035626350000000015 0.01296695 0.065222343601349264
		0.037336800000000017 0.0065834999999999999 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		0.037336800000000017 -0.0065834999999999999 0.065222343601349264
		0.035626350000000015 -0.01296695 0.065222343601349264
		0.032833400000000013 -0.01895645 0.065222343601349264
		0.029042950000000015 -0.0243699 0.065222343601349264
		0.024369900000000017 -0.029042950000000001 0.065222343601349264
		0.018956450000000017 -0.032833399999999999 0.065222343601349264
		0.012966950000000014 -0.035626350000000001 0.065222343601349264
		0.0065835000000000138 -0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 -0.037912800000000003 0.065222343601349264
		-0.0065834999999999861 -0.037336800000000003 0.065222343601349264
		-0.012966949999999986 -0.035626350000000001 0.065222343601349264
		-0.018956449999999982 -0.032833399999999999 0.065222343601349264
		-0.024369899999999983 -0.029042950000000001 0.065222343601349264
		-0.029042949999999988 -0.0243699 0.065222343601349264
		-0.032833399999999985 -0.01895645 0.065222343601349264
		-0.035626349999999987 -0.01296695 0.065222343601349264
		-0.037336799999999989 -0.0065834999999999999 0.065222343601349264
		-0.03791279999999999 0 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		;
createNode transform -n "L_brow_Mid_A_Pose" -p "Brow__Wr_Gro";
	rename -uid "5F5DEC0F-42CC-3F2C-B756-5CA780C0969E";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.29377481341362 14.330921081846189 1.7203883025914344 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_A_Mix" -p "L_brow_Mid_A_Pose";
	rename -uid "2D1F2553-4B55-96CF-2E19-19B9F850F71C";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 5.5511151231257827e-017 0 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -1.0187714214062833e-015 7.9513867036587919e-016 -1.0327484683463079e-014 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_A_Offset" -p "L_brow_Mid_A_Mix";
	rename -uid "C19BC0E8-460E-D521-D935-E0967602CBCB";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_A_Sel" -p "L_brow_Mid_A_Offset";
	rename -uid "82A8237B-4E3E-7B93-61D6-2981EE55B63F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_brow_Mid_A_Sel_Shape" -p "L_brow_Mid_A_Sel";
	rename -uid "B7394796-4835-822D-986E-009AB26B45F2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.03791279999999999 0 0.065222343601349264
		-0.037336799999999989 0.0065834999999999999 0.065222343601349264
		-0.035626349999999987 0.01296695 0.065222343601349264
		-0.032833399999999985 0.01895645 0.065222343601349264
		-0.029042949999999988 0.0243699 0.065222343601349264
		-0.024369899999999983 0.029042950000000001 0.065222343601349264
		-0.018956449999999982 0.032833399999999999 0.065222343601349264
		-0.012966949999999986 0.035626350000000001 0.065222343601349264
		-0.0065834999999999861 0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 0.037912800000000003 0.065222343601349264
		0.0065835000000000138 0.037336800000000003 0.065222343601349264
		0.012966950000000014 0.035626350000000001 0.065222343601349264
		0.018956450000000017 0.032833399999999999 0.065222343601349264
		0.024369900000000017 0.029042950000000001 0.065222343601349264
		0.029042950000000015 0.0243699 0.065222343601349264
		0.032833400000000013 0.01895645 0.065222343601349264
		0.035626350000000015 0.01296695 0.065222343601349264
		0.037336800000000017 0.0065834999999999999 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		0.037336800000000017 -0.0065834999999999999 0.065222343601349264
		0.035626350000000015 -0.01296695 0.065222343601349264
		0.032833400000000013 -0.01895645 0.065222343601349264
		0.029042950000000015 -0.0243699 0.065222343601349264
		0.024369900000000017 -0.029042950000000001 0.065222343601349264
		0.018956450000000017 -0.032833399999999999 0.065222343601349264
		0.012966950000000014 -0.035626350000000001 0.065222343601349264
		0.0065835000000000138 -0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 -0.037912800000000003 0.065222343601349264
		-0.0065834999999999861 -0.037336800000000003 0.065222343601349264
		-0.012966949999999986 -0.035626350000000001 0.065222343601349264
		-0.018956449999999982 -0.032833399999999999 0.065222343601349264
		-0.024369899999999983 -0.029042950000000001 0.065222343601349264
		-0.029042949999999988 -0.0243699 0.065222343601349264
		-0.032833399999999985 -0.01895645 0.065222343601349264
		-0.035626349999999987 -0.01296695 0.065222343601349264
		-0.037336799999999989 -0.0065834999999999999 0.065222343601349264
		-0.03791279999999999 0 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		;
createNode transform -n "L_brow_Mid_B_Pose" -p "Brow__Wr_Gro";
	rename -uid "855C3288-40AA-7339-7B2F-8598CD6B9C15";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.53049081563949585 14.330923942869138 1.6904944274693641 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 17.870057424936522 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_B_Mix" -p "L_brow_Mid_B_Pose";
	rename -uid "5318512F-427F-623D-1BCA-22A759F92B2C";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -2.2204460492503131e-016 0 -2.2204460492503131e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 1.9046763709525273e-015 6.3611093629270335e-015 -6.995004306168043e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_B_Offset" -p "L_brow_Mid_B_Mix";
	rename -uid "DCCB7E3E-4411-9CC4-7942-FFBB4DF2D06C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_B_Sel" -p "L_brow_Mid_B_Offset";
	rename -uid "62D14249-4A00-DBD7-AA3D-AA943EDCB4E7";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_brow_Mid_B_Sel_Shape" -p "L_brow_Mid_B_Sel";
	rename -uid "82BEE4F0-4F9C-AFFE-7039-4DBA1547711E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.057926881131743865 0 0.062075684944303607
		-0.057350881131743865 0.0065834999999999999 0.062075684944303607
		-0.055640431131743863 0.01296695 0.062075684944303607
		-0.052847481131743861 0.01895645 0.062075684944303607
		-0.04905703113174386 0.0243699 0.062075684944303607
		-0.044383981131743855 0.029042950000000001 0.062075684944303607
		-0.038970531131743855 0.032833399999999999 0.062075684944303607
		-0.03298103113174386 0.035626350000000001 0.062075684944303607
		-0.026597581131743864 0.037336800000000003 0.062075684944303607
		-0.020014081131743865 0.037912800000000003 0.062075684944303607
		-0.013430581131743859 0.037336800000000003 0.062075684944303607
		-0.0070471311317438614 0.035626350000000001 0.062075684944303607
		-0.0010576311317438609 0.032833399999999999 0.062075684944303607
		0.0043558188682561406 0.029042950000000001 0.062075684944303607
		0.0090288688682561447 0.0243699 0.062075684944303607
		0.01281931886825614 0.01895645 0.062075684944303607
		0.015612268868256139 0.01296695 0.062075684944303607
		0.017322718868256138 0.0065834999999999999 0.062075684944303607
		0.017898718868256138 0 0.062075684944303607
		0.017322718868256138 -0.0065834999999999999 0.062075684944303607
		0.015612268868256139 -0.01296695 0.062075684944303607
		0.01281931886825614 -0.01895645 0.062075684944303607
		0.0090288688682561447 -0.0243699 0.062075684944303607
		0.0043558188682561406 -0.029042950000000001 0.062075684944303607
		-0.0010576311317438609 -0.032833399999999999 0.062075684944303607
		-0.0070471311317438614 -0.035626350000000001 0.062075684944303607
		-0.013430581131743859 -0.037336800000000003 0.062075684944303607
		-0.020014081131743865 -0.037912800000000003 0.062075684944303607
		-0.026597581131743864 -0.037336800000000003 0.062075684944303607
		-0.03298103113174386 -0.035626350000000001 0.062075684944303607
		-0.038970531131743855 -0.032833399999999999 0.062075684944303607
		-0.044383981131743855 -0.029042950000000001 0.062075684944303607
		-0.04905703113174386 -0.0243699 0.062075684944303607
		-0.052847481131743861 -0.01895645 0.062075684944303607
		-0.055640431131743863 -0.01296695 0.062075684944303607
		-0.057350881131743865 -0.0065834999999999999 0.062075684944303607
		-0.057926881131743865 0 0.062075684944303607
		0.017898718868256138 0 0.062075684944303607
		;
createNode transform -n "L_brow_Mid_C_Pose" -p "Brow__Wr_Gro";
	rename -uid "C088C905-44F2-95EE-5288-EC850D45E288";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.76156973838806141 14.286952881162597 1.5503769014149815 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 42.878363043305875 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_C_Mix" -p "L_brow_Mid_C_Pose";
	rename -uid "C44F76B0-4DEA-A06E-78E4-51BB5F2F3BF5";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -7.7715611723760958e-016 0 -1.3322676295501878e-015 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 1.8891199438470082e-015 7.9308976908035436e-032 -4.8107793992978339e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_C_Offset" -p "L_brow_Mid_C_Mix";
	rename -uid "C1CFE3D1-4446-BC98-F9D4-76853E13CB3A";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Mid_C_Sel" -p "L_brow_Mid_C_Offset";
	rename -uid "335D55EF-42BE-B000-F5CC-04BE8A66ECC9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_brow_Mid_C_Sel_Shape" -p "L_brow_Mid_C_Sel";
	rename -uid "5384F2C0-4AC5-A59F-B37D-A19F6126DA86";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.082292964485075837 0 0.047794927608796313
		-0.081716964485075844 0.0065834999999999999 0.047794927608796313
		-0.080006514485075841 0.01296695 0.047794927608796313
		-0.077213564485075825 0.01895645 0.047794927608796313
		-0.073423114485075838 0.0243699 0.047794927608796313
		-0.06875006448507584 0.029042950000000001 0.047794927608796313
		-0.063336614485075826 0.032833399999999999 0.047794927608796313
		-0.057347114485075817 0.035626350000000001 0.047794927608796313
		-0.050963664485075819 0.037336800000000003 0.047794927608796313
		-0.04438016448507582 0.037912800000000003 0.047794927608796313
		-0.037796664485075813 0.037336800000000003 0.047794927608796313
		-0.031413214485075815 0.035626350000000001 0.047794927608796313
		-0.025423714485075823 0.032833399999999999 0.047794927608796313
		-0.02001026448507582 0.029042950000000001 0.047794927608796313
		-0.015337214485075818 0.0243699 0.047794927608796313
		-0.011546764485075816 0.01895645 0.047794927608796313
		-0.0087538144850758132 0.01296695 0.047794927608796313
		-0.0070433644850758127 0.0065834999999999999 0.047794927608796313
		-0.0064673644850758126 0 0.047794927608796313
		-0.0070433644850758127 -0.0065834999999999999 0.047794927608796313
		-0.0087538144850758132 -0.01296695 0.047794927608796313
		-0.011546764485075816 -0.01895645 0.047794927608796313
		-0.015337214485075818 -0.0243699 0.047794927608796313
		-0.02001026448507582 -0.029042950000000001 0.047794927608796313
		-0.025423714485075823 -0.032833399999999999 0.047794927608796313
		-0.031413214485075815 -0.035626350000000001 0.047794927608796313
		-0.037796664485075813 -0.037336800000000003 0.047794927608796313
		-0.04438016448507582 -0.037912800000000003 0.047794927608796313
		-0.050963664485075819 -0.037336800000000003 0.047794927608796313
		-0.057347114485075817 -0.035626350000000001 0.047794927608796313
		-0.063336614485075826 -0.032833399999999999 0.047794927608796313
		-0.06875006448507584 -0.029042950000000001 0.047794927608796313
		-0.073423114485075838 -0.0243699 0.047794927608796313
		-0.077213564485075825 -0.01895645 0.047794927608796313
		-0.080006514485075841 -0.01296695 0.047794927608796313
		-0.081716964485075844 -0.0065834999999999999 0.047794927608796313
		-0.082292964485075837 0 0.047794927608796313
		-0.0064673644850758126 0 0.047794927608796313
		;
createNode transform -n "L_brow_Out_Pose" -p "Brow__Wr_Gro";
	rename -uid "1BA8F38A-436A-F0BA-35D3-7196B22D97F7";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.9311785101890564 14.112699417417478 1.3148290012150916 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Out_Mix" -p "L_brow_Out_Pose";
	rename -uid "3CEB5AA2-4DCE-6958-2AE2-A180642403B5";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 3.3306690738754696e-016 0 6.6613381477509392e-016 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -2.5345045117912405e-015 -6.3611093629270335e-015 -2.1431471974705343e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Out_Offset" -p "L_brow_Out_Mix";
	rename -uid "B3B8B365-415C-A8EA-0805-8398C1ED2402";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_brow_Out_Sel" -p "L_brow_Out_Offset";
	rename -uid "0E0C8AA8-49C5-3496-5CC3-5B972AFDE2D9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_brow_Out_Sel_Shape" -p "L_brow_Out_Sel";
	rename -uid "C970FCA6-49B8-50C7-035E-0AB889FA746B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.03791279999999999 0 0.065222343601349264
		-0.037336799999999989 0.0065834999999999999 0.065222343601349264
		-0.035626349999999987 0.01296695 0.065222343601349264
		-0.032833399999999985 0.01895645 0.065222343601349264
		-0.029042949999999988 0.0243699 0.065222343601349264
		-0.024369899999999983 0.029042950000000001 0.065222343601349264
		-0.018956449999999982 0.032833399999999999 0.065222343601349264
		-0.012966949999999986 0.035626350000000001 0.065222343601349264
		-0.0065834999999999861 0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 0.037912800000000003 0.065222343601349264
		0.0065835000000000138 0.037336800000000003 0.065222343601349264
		0.012966950000000014 0.035626350000000001 0.065222343601349264
		0.018956450000000017 0.032833399999999999 0.065222343601349264
		0.024369900000000017 0.029042950000000001 0.065222343601349264
		0.029042950000000015 0.0243699 0.065222343601349264
		0.032833400000000013 0.01895645 0.065222343601349264
		0.035626350000000015 0.01296695 0.065222343601349264
		0.037336800000000017 0.0065834999999999999 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		0.037336800000000017 -0.0065834999999999999 0.065222343601349264
		0.035626350000000015 -0.01296695 0.065222343601349264
		0.032833400000000013 -0.01895645 0.065222343601349264
		0.029042950000000015 -0.0243699 0.065222343601349264
		0.024369900000000017 -0.029042950000000001 0.065222343601349264
		0.018956450000000017 -0.032833399999999999 0.065222343601349264
		0.012966950000000014 -0.035626350000000001 0.065222343601349264
		0.0065835000000000138 -0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 -0.037912800000000003 0.065222343601349264
		-0.0065834999999999861 -0.037336800000000003 0.065222343601349264
		-0.012966949999999986 -0.035626350000000001 0.065222343601349264
		-0.018956449999999982 -0.032833399999999999 0.065222343601349264
		-0.024369899999999983 -0.029042950000000001 0.065222343601349264
		-0.029042949999999988 -0.0243699 0.065222343601349264
		-0.032833399999999985 -0.01895645 0.065222343601349264
		-0.035626349999999987 -0.01296695 0.065222343601349264
		-0.037336799999999989 -0.0065834999999999999 0.065222343601349264
		-0.03791279999999999 0 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		;
createNode transform -n "R_brow_Inn_Pose" -p "Brow__Wr_Gro";
	rename -uid "9D0B8C4C-43F4-E75F-B98D-55B5E8F3673D";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.15036687254905701 14.323825744932128 1.7020493839055213 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Inn_Mix" -p "R_brow_Inn_Pose";
	rename -uid "AD39952B-42D2-FEFE-D5AC-379A5CE6BF84";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Inn_Offset" -p "R_brow_Inn_Mix";
	rename -uid "9BCE7A96-43AC-30E8-0DA9-C8AC28AB492A";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Inn_Sel" -p "R_brow_Inn_Offset";
	rename -uid "9916FDF9-4F04-7BEF-365A-78B3CE8B118F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_brow_Inn_Sel_Shape" -p "R_brow_Inn_Sel";
	rename -uid "257ED691-4DA5-E58A-0ED3-86AA7A2D15CF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.037912800000000017 0 0.065222343601349264
		-0.037336800000000017 0.0065834999999999999 0.065222343601349264
		-0.035626350000000015 0.01296695 0.065222343601349264
		-0.032833400000000013 0.01895645 0.065222343601349264
		-0.029042950000000015 0.0243699 0.065222343601349264
		-0.024369900000000017 0.029042950000000001 0.065222343601349264
		-0.018956450000000017 0.032833399999999999 0.065222343601349264
		-0.012966950000000014 0.035626350000000001 0.065222343601349264
		-0.0065835000000000138 0.037336800000000003 0.065222343601349264
		-1.3877787807814457e-017 0.037912800000000003 0.065222343601349264
		0.0065834999999999861 0.037336800000000003 0.065222343601349264
		0.012966949999999986 0.035626350000000001 0.065222343601349264
		0.018956449999999982 0.032833399999999999 0.065222343601349264
		0.024369899999999983 0.029042950000000001 0.065222343601349264
		0.029042949999999988 0.0243699 0.065222343601349264
		0.032833399999999985 0.01895645 0.065222343601349264
		0.035626349999999987 0.01296695 0.065222343601349264
		0.037336799999999989 0.0065834999999999999 0.065222343601349264
		0.03791279999999999 0 0.065222343601349264
		0.037336799999999989 -0.0065834999999999999 0.065222343601349264
		0.035626349999999987 -0.01296695 0.065222343601349264
		0.032833399999999985 -0.01895645 0.065222343601349264
		0.029042949999999988 -0.0243699 0.065222343601349264
		0.024369899999999983 -0.029042950000000001 0.065222343601349264
		0.018956449999999982 -0.032833399999999999 0.065222343601349264
		0.012966949999999986 -0.035626350000000001 0.065222343601349264
		0.0065834999999999861 -0.037336800000000003 0.065222343601349264
		-1.3877787807814457e-017 -0.037912800000000003 0.065222343601349264
		-0.0065835000000000138 -0.037336800000000003 0.065222343601349264
		-0.012966950000000014 -0.035626350000000001 0.065222343601349264
		-0.018956450000000017 -0.032833399999999999 0.065222343601349264
		-0.024369900000000017 -0.029042950000000001 0.065222343601349264
		-0.029042950000000015 -0.0243699 0.065222343601349264
		-0.032833400000000013 -0.01895645 0.065222343601349264
		-0.035626350000000015 -0.01296695 0.065222343601349264
		-0.037336800000000017 -0.0065834999999999999 0.065222343601349264
		-0.037912800000000017 0 0.065222343601349264
		0.03791279999999999 0 0.065222343601349264
		;
createNode transform -n "R_brow_Mid_A_Pose" -p "Brow__Wr_Gro";
	rename -uid "71D55247-4CAC-1996-3274-3F85F756C5F3";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.29377481341362005 14.330921081846189 1.7203883025914342 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_A_Mix" -p "R_brow_Mid_A_Pose";
	rename -uid "B1DCA466-4F7D-3F98-8776-3C9F59466F52";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_A_Offset" -p "R_brow_Mid_A_Mix";
	rename -uid "0449A341-4D22-622B-581D-CB807F4C75DB";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_A_Sel" -p "R_brow_Mid_A_Offset";
	rename -uid "676586D1-429C-F934-85E6-B9BA0FCA8DD8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_brow_Mid_A_Sel_Shape" -p "R_brow_Mid_A_Sel";
	rename -uid "7EA71181-4C98-AA97-300D-11B9C0E5332F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.037912800000000017 0 0.065222343601349264
		-0.037336800000000017 0.0065834999999999999 0.065222343601349264
		-0.035626350000000015 0.01296695 0.065222343601349264
		-0.032833400000000013 0.01895645 0.065222343601349264
		-0.029042950000000015 0.0243699 0.065222343601349264
		-0.024369900000000017 0.029042950000000001 0.065222343601349264
		-0.018956450000000017 0.032833399999999999 0.065222343601349264
		-0.012966950000000014 0.035626350000000001 0.065222343601349264
		-0.0065835000000000138 0.037336800000000003 0.065222343601349264
		-1.3877787807814457e-017 0.037912800000000003 0.065222343601349264
		0.0065834999999999861 0.037336800000000003 0.065222343601349264
		0.012966949999999986 0.035626350000000001 0.065222343601349264
		0.018956449999999982 0.032833399999999999 0.065222343601349264
		0.024369899999999983 0.029042950000000001 0.065222343601349264
		0.029042949999999988 0.0243699 0.065222343601349264
		0.032833399999999985 0.01895645 0.065222343601349264
		0.035626349999999987 0.01296695 0.065222343601349264
		0.037336799999999989 0.0065834999999999999 0.065222343601349264
		0.03791279999999999 0 0.065222343601349264
		0.037336799999999989 -0.0065834999999999999 0.065222343601349264
		0.035626349999999987 -0.01296695 0.065222343601349264
		0.032833399999999985 -0.01895645 0.065222343601349264
		0.029042949999999988 -0.0243699 0.065222343601349264
		0.024369899999999983 -0.029042950000000001 0.065222343601349264
		0.018956449999999982 -0.032833399999999999 0.065222343601349264
		0.012966949999999986 -0.035626350000000001 0.065222343601349264
		0.0065834999999999861 -0.037336800000000003 0.065222343601349264
		-1.3877787807814457e-017 -0.037912800000000003 0.065222343601349264
		-0.0065835000000000138 -0.037336800000000003 0.065222343601349264
		-0.012966950000000014 -0.035626350000000001 0.065222343601349264
		-0.018956450000000017 -0.032833399999999999 0.065222343601349264
		-0.024369900000000017 -0.029042950000000001 0.065222343601349264
		-0.029042950000000015 -0.0243699 0.065222343601349264
		-0.032833400000000013 -0.01895645 0.065222343601349264
		-0.035626350000000015 -0.01296695 0.065222343601349264
		-0.037336800000000017 -0.0065834999999999999 0.065222343601349264
		-0.037912800000000017 0 0.065222343601349264
		0.03791279999999999 0 0.065222343601349264
		;
createNode transform -n "R_brow_Mid_B_Pose" -p "Brow__Wr_Gro";
	rename -uid "48357C92-4D77-E290-F4A9-EB9C146B1E8D";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.53049081563949585 14.330923942869136 1.6904944274693638 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -17.870057424936522 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_B_Mix" -p "R_brow_Mid_B_Pose";
	rename -uid "69EB0AEA-4FA5-E49D-BBFA-04B194D61170";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_B_Offset" -p "R_brow_Mid_B_Mix";
	rename -uid "7452A72D-4359-EDFB-94D7-70B4148D20BB";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_B_Sel" -p "R_brow_Mid_B_Offset";
	rename -uid "29BA0230-46AF-F885-4610-8D8DDA829B70";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_brow_Mid_B_Sel_Shape" -p "R_brow_Mid_B_Sel";
	rename -uid "38BD6583-44F1-73A5-E019-1D9C93A65ED2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.057926881131743893 0 0.062075684944303593
		-0.0573508811317439 0.0065834999999999999 0.062075684944303593
		-0.055640431131743898 0.01296695 0.062075684944303593
		-0.052847481131743895 0.01895645 0.062075684944303593
		-0.049057031131743895 0.0243699 0.062075684944303593
		-0.044383981131743896 0.029042950000000001 0.062075684944303593
		-0.038970531131743896 0.032833399999999999 0.062075684944303593
		-0.032981031131743888 0.035626350000000001 0.062075684944303593
		-0.026597581131743892 0.037336800000000003 0.062075684944303593
		-0.020014081131743893 0.037912800000000003 0.062075684944303593
		-0.013430581131743892 0.037336800000000003 0.062075684944303593
		-0.0070471311317438909 0.035626350000000001 0.062075684944303593
		-0.0010576311317438893 0.032833399999999999 0.062075684944303593
		0.0043558188682561111 0.029042950000000001 0.062075684944303593
		0.0090288688682561152 0.0243699 0.062075684944303593
		0.012819318868256113 0.01895645 0.062075684944303593
		0.015612268868256111 0.01296695 0.062075684944303593
		0.01732271886825611 0.0065834999999999999 0.062075684944303593
		0.01789871886825611 0 0.062075684944303593
		0.01732271886825611 -0.0065834999999999999 0.062075684944303593
		0.015612268868256111 -0.01296695 0.062075684944303593
		0.012819318868256113 -0.01895645 0.062075684944303593
		0.0090288688682561152 -0.0243699 0.062075684944303593
		0.0043558188682561111 -0.029042950000000001 0.062075684944303593
		-0.0010576311317438893 -0.032833399999999999 0.062075684944303593
		-0.0070471311317438909 -0.035626350000000001 0.062075684944303593
		-0.013430581131743892 -0.037336800000000003 0.062075684944303593
		-0.020014081131743893 -0.037912800000000003 0.062075684944303593
		-0.026597581131743892 -0.037336800000000003 0.062075684944303593
		-0.032981031131743888 -0.035626350000000001 0.062075684944303593
		-0.038970531131743896 -0.032833399999999999 0.062075684944303593
		-0.044383981131743896 -0.029042950000000001 0.062075684944303593
		-0.049057031131743895 -0.0243699 0.062075684944303593
		-0.052847481131743895 -0.01895645 0.062075684944303593
		-0.055640431131743898 -0.01296695 0.062075684944303593
		-0.0573508811317439 -0.0065834999999999999 0.062075684944303593
		-0.057926881131743893 0 0.062075684944303593
		0.01789871886825611 0 0.062075684944303593
		;
createNode transform -n "R_brow_Mid_C_Pose" -p "Brow__Wr_Gro";
	rename -uid "E63404F8-4DB3-B547-AE50-DBA03E28158A";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.76156973838806097 14.286952881162597 1.5503769014149813 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 -42.878363043305875 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_C_Mix" -p "R_brow_Mid_C_Pose";
	rename -uid "36183EB5-4D0D-A238-1A54-BA8F16AFE4A9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_C_Offset" -p "R_brow_Mid_C_Mix";
	rename -uid "877243BA-48FF-A703-6F45-849C2827B9DC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Mid_C_Sel" -p "R_brow_Mid_C_Offset";
	rename -uid "E94E04BC-4A5A-C0D8-61BF-6FB64594BE4F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_brow_Mid_C_Sel_Shape" -p "R_brow_Mid_C_Sel";
	rename -uid "E86B2C22-4FD6-3E45-C8B8-9C80330BC291";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.082292964485075851 7.581089963631379e-017 0.047794927608796271
		-0.081716964485075858 0.0065835000000000728 0.047794927608796271
		-0.080006514485075855 0.012966950000000067 0.047794927608796271
		-0.077213564485075839 0.018956450000000069 0.047794927608796271
		-0.073423114485075852 0.024369900000000069 0.047794927608796271
		-0.068750064485075854 0.029042950000000071 0.047794927608796271
		-0.06333661448507584 0.032833400000000137 0.047794927608796271
		-0.057347114485075838 0.03562635000000014 0.047794927608796271
		-0.050963664485075839 0.037336800000000142 0.047794927608796271
		-0.04438016448507584 0.037912800000000142 0.047794927608796271
		-0.037796664485075834 0.037336800000000142 0.047794927608796271
		-0.031413214485075829 0.03562635000000014 0.047794927608796271
		-0.02542371448507583 0.032833400000000137 0.047794927608796271
		-0.02001026448507583 0.029042950000000071 0.047794927608796271
		-0.015337214485075829 0.024369900000000069 0.047794927608796271
		-0.011546764485075828 0.018956450000000069 0.047794927608796271
		-0.0087538144850758271 0.012966950000000067 0.047794927608796271
		-0.0070433644850758266 0.0065835000000000728 0.047794927608796271
		-0.0064673644850758265 7.581089963631379e-017 0.047794927608796271
		-0.0070433644850758266 -0.0065834999999999271 0.047794927608796271
		-0.0087538144850758271 -0.01296694999999993 0.047794927608796271
		-0.011546764485075828 -0.01895644999999993 0.047794927608796271
		-0.015337214485075829 -0.024369899999999931 0.047794927608796271
		-0.02001026448507583 -0.029042949999999932 0.047794927608796271
		-0.02542371448507583 -0.03283339999999986 0.047794927608796271
		-0.031413214485075829 -0.035626349999999862 0.047794927608796271
		-0.037796664485075834 -0.037336799999999865 0.047794927608796271
		-0.04438016448507584 -0.037912799999999865 0.047794927608796271
		-0.050963664485075839 -0.037336799999999865 0.047794927608796271
		-0.057347114485075838 -0.035626349999999862 0.047794927608796271
		-0.06333661448507584 -0.03283339999999986 0.047794927608796271
		-0.068750064485075854 -0.029042949999999932 0.047794927608796271
		-0.073423114485075852 -0.024369899999999931 0.047794927608796271
		-0.077213564485075839 -0.01895644999999993 0.047794927608796271
		-0.080006514485075855 -0.01296694999999993 0.047794927608796271
		-0.081716964485075858 -0.0065834999999999271 0.047794927608796271
		-0.082292964485075851 7.581089963631379e-017 0.047794927608796271
		-0.0064673644850758265 7.581089963631379e-017 0.047794927608796271
		;
createNode transform -n "R_brow_Out_Pose" -p "Brow__Wr_Gro";
	rename -uid "81A70FBB-4F4F-1295-DE97-2EA52C684320";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.93117851018905684 14.112699417417479 1.3148290012150925 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Out_Mix" -p "R_brow_Out_Pose";
	rename -uid "14CE38FE-417F-87F4-D0C0-76942CD53025";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Out_Offset" -p "R_brow_Out_Mix";
	rename -uid "EBEE6643-4895-CE69-0CD2-4A98A1AA20D1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_brow_Out_Sel" -p "R_brow_Out_Offset";
	rename -uid "E927EF6D-4DF1-6927-20AF-8292E3C58745";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_brow_Out_Sel_Shape" -p "R_brow_Out_Sel";
	rename -uid "AEF0871A-466E-2154-B02F-3598592C6DF4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.037912800000000017 0 0.065222343601349264
		-0.037336800000000017 0.0065834999999999999 0.065222343601349264
		-0.035626350000000015 0.01296695 0.065222343601349264
		-0.032833400000000013 0.01895645 0.065222343601349264
		-0.029042950000000015 0.0243699 0.065222343601349264
		-0.024369900000000017 0.029042950000000001 0.065222343601349264
		-0.018956450000000017 0.032833399999999999 0.065222343601349264
		-0.012966950000000014 0.035626350000000001 0.065222343601349264
		-0.0065835000000000138 0.037336800000000003 0.065222343601349264
		-1.3877787807814457e-017 0.037912800000000003 0.065222343601349264
		0.0065834999999999861 0.037336800000000003 0.065222343601349264
		0.012966949999999986 0.035626350000000001 0.065222343601349264
		0.018956449999999982 0.032833399999999999 0.065222343601349264
		0.024369899999999983 0.029042950000000001 0.065222343601349264
		0.029042949999999988 0.0243699 0.065222343601349264
		0.032833399999999985 0.01895645 0.065222343601349264
		0.035626349999999987 0.01296695 0.065222343601349264
		0.037336799999999989 0.0065834999999999999 0.065222343601349264
		0.03791279999999999 0 0.065222343601349264
		0.037336799999999989 -0.0065834999999999999 0.065222343601349264
		0.035626349999999987 -0.01296695 0.065222343601349264
		0.032833399999999985 -0.01895645 0.065222343601349264
		0.029042949999999988 -0.0243699 0.065222343601349264
		0.024369899999999983 -0.029042950000000001 0.065222343601349264
		0.018956449999999982 -0.032833399999999999 0.065222343601349264
		0.012966949999999986 -0.035626350000000001 0.065222343601349264
		0.0065834999999999861 -0.037336800000000003 0.065222343601349264
		-1.3877787807814457e-017 -0.037912800000000003 0.065222343601349264
		-0.0065835000000000138 -0.037336800000000003 0.065222343601349264
		-0.012966950000000014 -0.035626350000000001 0.065222343601349264
		-0.018956450000000017 -0.032833399999999999 0.065222343601349264
		-0.024369900000000017 -0.029042950000000001 0.065222343601349264
		-0.029042950000000015 -0.0243699 0.065222343601349264
		-0.032833400000000013 -0.01895645 0.065222343601349264
		-0.035626350000000015 -0.01296695 0.065222343601349264
		-0.037336800000000017 -0.0065834999999999999 0.065222343601349264
		-0.037912800000000017 0 0.065222343601349264
		0.03791279999999999 0 0.065222343601349264
		;
createNode transform -n "C_brow_Pose" -p "Brow__Wr_Gro";
	rename -uid "9EEF7C26-43D4-9EF8-B8C0-5E9BD86FA2A4";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 2.4035605705952738e-031 14.324051765745114 1.7157648895054969 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 0 360 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_Mix" -p "C_brow_Pose";
	rename -uid "C7BDB304-4726-8702-D7CA-55B29B4F95CE";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_Offset" -p "C_brow_Mix";
	rename -uid "1DE94803-46DF-3363-1B07-E4BAE9F1E142";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_Sel" -p "C_brow_Offset";
	rename -uid "8238F42F-40A4-A0DA-C754-03B9CE4C4741";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_brow_Sel_Shape" -p "C_brow_Sel";
	rename -uid "8FEB2E38-462A-95E2-9AB2-74ADAAB8C317";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 25;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.03791279999999999 0 0.065222343601349264
		-0.037336799999999989 0.0065834999999999999 0.065222343601349264
		-0.035626349999999987 0.01296695 0.065222343601349264
		-0.032833399999999985 0.01895645 0.065222343601349264
		-0.029042949999999988 0.0243699 0.065222343601349264
		-0.024369899999999983 0.029042950000000001 0.065222343601349264
		-0.018956449999999982 0.032833399999999999 0.065222343601349264
		-0.012966949999999986 0.035626350000000001 0.065222343601349264
		-0.0065834999999999861 0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 0.037912800000000003 0.065222343601349264
		0.0065835000000000138 0.037336800000000003 0.065222343601349264
		0.012966950000000014 0.035626350000000001 0.065222343601349264
		0.018956450000000017 0.032833399999999999 0.065222343601349264
		0.024369900000000017 0.029042950000000001 0.065222343601349264
		0.029042950000000015 0.0243699 0.065222343601349264
		0.032833400000000013 0.01895645 0.065222343601349264
		0.035626350000000015 0.01296695 0.065222343601349264
		0.037336800000000017 0.0065834999999999999 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		0.037336800000000017 -0.0065834999999999999 0.065222343601349264
		0.035626350000000015 -0.01296695 0.065222343601349264
		0.032833400000000013 -0.01895645 0.065222343601349264
		0.029042950000000015 -0.0243699 0.065222343601349264
		0.024369900000000017 -0.029042950000000001 0.065222343601349264
		0.018956450000000017 -0.032833399999999999 0.065222343601349264
		0.012966950000000014 -0.035626350000000001 0.065222343601349264
		0.0065835000000000138 -0.037336800000000003 0.065222343601349264
		1.3877787807814457e-017 -0.037912800000000003 0.065222343601349264
		-0.0065834999999999861 -0.037336800000000003 0.065222343601349264
		-0.012966949999999986 -0.035626350000000001 0.065222343601349264
		-0.018956449999999982 -0.032833399999999999 0.065222343601349264
		-0.024369899999999983 -0.029042950000000001 0.065222343601349264
		-0.029042949999999988 -0.0243699 0.065222343601349264
		-0.032833399999999985 -0.01895645 0.065222343601349264
		-0.035626349999999987 -0.01296695 0.065222343601349264
		-0.037336799999999989 -0.0065834999999999999 0.065222343601349264
		-0.03791279999999999 0 0.065222343601349264
		0.037912800000000017 0 0.065222343601349264
		;
createNode transform -n "C_brow_lf_Pose" -p "Brow__Wr_Gro";
	rename -uid "28482C3F-43D8-379A-DC66-60B245E4142A";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.11476376652717592 14.323755173032714 1.707079300668827 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_lf_Mix" -p "C_brow_lf_Pose";
	rename -uid "CD2C00D8-4EC4-E528-557A-1AAE72F59671";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_lf_Offset" -p "C_brow_lf_Mix";
	rename -uid "3CAE166B-4436-15BC-19F2-1DBC362045FB";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_lf_Sel" -p "C_brow_lf_Offset";
	rename -uid "A45CDA51-4379-297C-FF24-75A9851014B6";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_brow_lf_Sel_Shape" -p "C_brow_lf_Sel";
	rename -uid "C6F13C8B-4405-58CB-6181-288D7E17C4D9";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 25;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.018956399999999988 0 0.065222343601349264
		-0.018668399999999988 0.00329175 0.065222343601349264
		-0.017813174999999987 0.0064834749999999998 0.065222343601349264
		-0.016416699999999985 0.0094782249999999998 0.065222343601349264
		-0.014521474999999989 0.01218495 0.065222343601349264
		-0.012184949999999986 0.014521475000000001 0.065222343601349264
		-0.009478224999999986 0.016416699999999999 0.065222343601349264
		-0.006483474999999986 0.017813175000000001 0.065222343601349264
		-0.0032917499999999861 0.018668400000000002 0.065222343601349264
		1.3877787807814457e-017 0.018956400000000002 0.065222343601349264
		0.0032917500000000138 0.018668400000000002 0.065222343601349264
		0.0064834750000000137 0.017813175000000001 0.065222343601349264
		0.0094782250000000137 0.016416699999999999 0.065222343601349264
		0.012184950000000014 0.014521475000000001 0.065222343601349264
		0.014521475000000016 0.01218495 0.065222343601349264
		0.016416700000000013 0.0094782249999999998 0.065222343601349264
		0.017813175000000014 0.0064834749999999998 0.065222343601349264
		0.018668400000000016 0.00329175 0.065222343601349264
		0.018956400000000016 0 0.065222343601349264
		0.018668400000000016 -0.00329175 0.065222343601349264
		0.017813175000000014 -0.0064834749999999998 0.065222343601349264
		0.016416700000000013 -0.0094782249999999998 0.065222343601349264
		0.014521475000000016 -0.01218495 0.065222343601349264
		0.012184950000000014 -0.014521475000000001 0.065222343601349264
		0.0094782250000000137 -0.016416699999999999 0.065222343601349264
		0.0064834750000000137 -0.017813175000000001 0.065222343601349264
		0.0032917500000000138 -0.018668400000000002 0.065222343601349264
		1.3877787807814457e-017 -0.018956400000000002 0.065222343601349264
		-0.0032917499999999861 -0.018668400000000002 0.065222343601349264
		-0.006483474999999986 -0.017813175000000001 0.065222343601349264
		-0.009478224999999986 -0.016416699999999999 0.065222343601349264
		-0.012184949999999986 -0.014521475000000001 0.065222343601349264
		-0.014521474999999989 -0.01218495 0.065222343601349264
		-0.016416699999999985 -0.0094782249999999998 0.065222343601349264
		-0.017813174999999987 -0.0064834749999999998 0.065222343601349264
		-0.018668399999999988 -0.00329175 0.065222343601349264
		-0.018956399999999988 0 0.065222343601349264
		0.018956400000000016 0 0.065222343601349264
		;
createNode transform -n "C_brow_rt_Pose" -p "Brow__Wr_Gro";
	rename -uid "D173DD55-4FA7-72C8-EE19-55BAA7C1D2DA";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.1147637665271759 14.323755173032712 1.707079300668827 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_rt_Mix" -p "C_brow_rt_Pose";
	rename -uid "E312092B-4AD8-8A4E-8CF1-14B8D0FEF2A1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_rt_Offset" -p "C_brow_rt_Mix";
	rename -uid "A878187B-4939-2234-4B6E-8FAC1D63EF1B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_brow_rt_Sel" -p "C_brow_rt_Offset";
	rename -uid "339C550C-4A54-280C-8C9E-6390937B3794";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_brow_rt_Sel_Shape" -p "C_brow_rt_Sel";
	rename -uid "19E001E7-40AE-E603-72A9-44A9DFB01FFD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 25;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.018956399999999988 0 0.065222343601349264
		-0.018668399999999988 0.00329175 0.065222343601349264
		-0.017813174999999987 0.0064834749999999998 0.065222343601349264
		-0.016416699999999985 0.0094782249999999998 0.065222343601349264
		-0.014521474999999989 0.01218495 0.065222343601349264
		-0.012184949999999986 0.014521475000000001 0.065222343601349264
		-0.009478224999999986 0.016416699999999999 0.065222343601349264
		-0.006483474999999986 0.017813175000000001 0.065222343601349264
		-0.0032917499999999861 0.018668400000000002 0.065222343601349264
		1.3877787807814457e-017 0.018956400000000002 0.065222343601349264
		0.0032917500000000138 0.018668400000000002 0.065222343601349264
		0.0064834750000000137 0.017813175000000001 0.065222343601349264
		0.0094782250000000137 0.016416699999999999 0.065222343601349264
		0.012184950000000014 0.014521475000000001 0.065222343601349264
		0.014521475000000016 0.01218495 0.065222343601349264
		0.016416700000000013 0.0094782249999999998 0.065222343601349264
		0.017813175000000014 0.0064834749999999998 0.065222343601349264
		0.018668400000000016 0.00329175 0.065222343601349264
		0.018956400000000016 0 0.065222343601349264
		0.018668400000000016 -0.00329175 0.065222343601349264
		0.017813175000000014 -0.0064834749999999998 0.065222343601349264
		0.016416700000000013 -0.0094782249999999998 0.065222343601349264
		0.014521475000000016 -0.01218495 0.065222343601349264
		0.012184950000000014 -0.014521475000000001 0.065222343601349264
		0.0094782250000000137 -0.016416699999999999 0.065222343601349264
		0.0064834750000000137 -0.017813175000000001 0.065222343601349264
		0.0032917500000000138 -0.018668400000000002 0.065222343601349264
		1.3877787807814457e-017 -0.018956400000000002 0.065222343601349264
		-0.0032917499999999861 -0.018668400000000002 0.065222343601349264
		-0.006483474999999986 -0.017813175000000001 0.065222343601349264
		-0.009478224999999986 -0.016416699999999999 0.065222343601349264
		-0.012184949999999986 -0.014521475000000001 0.065222343601349264
		-0.014521474999999989 -0.01218495 0.065222343601349264
		-0.016416699999999985 -0.0094782249999999998 0.065222343601349264
		-0.017813174999999987 -0.0064834749999999998 0.065222343601349264
		-0.018668399999999988 -0.00329175 0.065222343601349264
		-0.018956399999999988 0 0.065222343601349264
		0.018956400000000016 0 0.065222343601349264
		;
createNode transform -n "Mouth__Wr_Gro" -p "Face_Pose__Sel";
	rename -uid "416D522F-4FBD-278E-B3E8-44A026B9DE14";
	addAttr -ci true -h true -sn "Mili_Hide" -ln "Mili_Hide" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_UppLip_Pose" -p "Mouth__Wr_Gro";
	rename -uid "E8859CE6-4377-263C-D740-5890CA19FBF0";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 4.9953668802645836e-018 11.879221348112058 3.0935453269749806 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -3.1805546814635176e-015 9.5416640443905503e-015 -3.1805546814635176e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_UppLip_Mix" -p "C_UppLip_Pose";
	rename -uid "3BECFBE0-4F1E-36B8-D591-5084FFB10044";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_UppLip_Offset" -p "C_UppLip_Mix";
	rename -uid "FE379065-47C2-C21F-5EC0-A4B61C25C43C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_UppLip_Sel" -p "C_UppLip_Offset";
	rename -uid "C2C4C805-418D-F0E1-8EAA-B0AAD2234ACC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_UppLip_Sel_Shape" -p "C_UppLip_Sel";
	rename -uid "B9E64F38-4CB8-0BEF-4418-6F99043B839E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 25;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.075825611881048194 -6.0504492246614596e-018 0.15122656401758039
		-0.074673626506728707 0.013166971955415354 0.15122656401758039
		-0.071252705420497928 0.025933869904467367 0.15122656401758039
		-0.065666829419767203 0.037912914744985961 0.15122656401758039
		-0.058085914805852366 0.048739756602261243 0.15122656401758039
		-0.048739756602261243 0.058085914805852366 0.15122656401758039
		-0.037912914744985961 0.065666829419767203 0.15122656401758039
		-0.025933869904467371 0.071252705420497914 0.15122656401758039
		-0.013166971955415368 0.074673626506728694 0.15122656401758039
		8.598205489337061e-032 0.075825611881048194 0.15122656401758039
		0.013166971955415368 0.074673626506728694 0.15122656401758039
		0.025933869904467371 0.071252705420497914 0.15122656401758039
		0.037912914744985961 0.065666829419767203 0.15122656401758039
		0.048739756602261243 0.058085914805852366 0.15122656401758039
		0.058085914805852366 0.048739756602261243 0.15122656401758039
		0.065666829419767203 0.037912914744985961 0.15122656401758039
		0.071252705420497928 0.025933869904467367 0.15122656401758039
		0.074673626506728707 0.013166971955415354 0.15122656401758039
		0.075825611881048194 -6.0504492246614596e-018 0.15122656401758039
		0.075551184788477443 -0.0091459635196478976 0.15122656401757997
		0.072090061320617863 -0.0091815179985680617 0.15122656401757997
		0.066438540567186885 -0.0091644446842122848 0.15122656401757997
		0.058768535671818126 -0.0091490135645386772 0.15122656401757997
		0.049312542190127102 -0.0091356928115777156 0.15122656401757997
		0.038358464182935099 -0.0091248879986706166 0.15122656401757997
		0.026238642598350254 -0.0091169266446409214 0.15122656401757997
		0.013321709120671254 -0.0091120509252601983 0.15122656401757997
		1.1656979601502052e-031 -0.0091104090407284205 0.15122656401757997
		-0.013321709120671254 -0.0091120509252601983 0.15122656401757997
		-0.026238642598350254 -0.0091169266446409214 0.15122656401757997
		-0.038358464182935099 -0.0091248879986706166 0.15122656401757997
		-0.049312542190127102 -0.0091356928115777156 0.15122656401757997
		-0.058768535671818126 -0.0091490135645386772 0.15122656401757997
		-0.066438540567186885 -0.0091644446842122848 0.15122656401757997
		-0.072090061320617863 -0.0091815179985680617 0.15122656401757997
		-0.075551184788477443 -0.0091459635196478976 0.15122656401757997
		-0.075825611881048194 -6.0504492246614596e-018 0.15122656401758039
		0.075825611881048194 -6.0504492246614596e-018 0.15122656401758039
		;
createNode transform -n "C_LowLip_Pose" -p "Mouth__Wr_Gro";
	rename -uid "E7189D4D-46B1-7696-4F9E-3984AC167783";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -4.3913493399390691e-017 11.802409557645747 3.0913246963292274 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -3.1805546814635176e-015 9.5416640443905503e-015 -3.1805546814635176e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_LowLip_Mix" -p "C_LowLip_Pose";
	rename -uid "73A5480F-497A-E0FD-E595-F6AA1AF29B5C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_LowLip_Offset" -p "C_LowLip_Mix";
	rename -uid "60305131-4F66-07BB-4BA3-5996E0EC8501";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "C_LowLip_Sel" -p "C_LowLip_Offset";
	rename -uid "9F369B7D-493F-3766-5B04-01B891BAA3CD";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "C_LowLip_Sel_Shape" -p "C_LowLip_Sel";
	rename -uid "1742D5B8-4FFF-321C-9710-B895CD070C0B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 25;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.075825611881048194 -3.0948047784143395e-015 0.15122656401758194
		-0.076480253697678538 0.0087540623517301658 0.15122656401758194
		-0.07297656806201315 0.0087642051629221382 0.15122656401758194
		-0.067255549361774122 0.0087737220550099457 0.15122656401758194
		-0.059491224792906403 0.0087823235659800838 0.15122656401758194
		-0.049918948958078961 0.0087897487305272845 0.15122656401758194
		-0.038830166335281795 0.0087957714766867881 0.15122656401758194
		-0.026561304739599483 0.0088002092411181496 0.15122656401758194
		-0.013485528997170718 0.0088029270318311925 0.15122656401758194
		8.8062274183244061e-032 0.008803842240066917 0.15122656401758194
		0.013485528997170718 0.0088029270318311925 0.15122656401758194
		0.026561304739599483 0.0088002092411181496 0.15122656401758194
		0.038830166335281795 0.0087957714766867881 0.15122656401758194
		0.049918948958078961 0.0087897487305272845 0.15122656401758194
		0.059491224792906403 0.0087823235659800838 0.15122656401758194
		0.067255549361774122 0.0087737220550099457 0.15122656401758194
		0.07297656806201315 0.0087642051629221382 0.15122656401758194
		0.076480253697678538 0.0087540623517301658 0.15122656401758194
		0.075825611881048194 -3.0948047784143395e-015 0.15122656401758194
		0.074673626506728707 -0.013166971955418454 0.15122656401758194
		0.071252705420497928 -0.025933869904470452 0.15122656401758194
		0.065666829419767203 -0.03791291474498909 0.15122656401758194
		0.058085914805852366 -0.048739756602264414 0.15122656401758194
		0.048739756602261243 -0.058085914805855461 0.15122656401758194
		0.037912914744985961 -0.065666829419770326 0.15122656401758194
		0.025933869904467371 -0.071252705420501078 0.15122656401758194
		0.013166971955415368 -0.074673626506731691 0.15122656401758194
		8.598205489337061e-032 -0.075825611881051372 0.15122656401758194
		-0.013166971955415368 -0.074673626506731691 0.15122656401758194
		-0.025933869904467371 -0.071252705420501078 0.15122656401758194
		-0.037912914744985961 -0.065666829419770326 0.15122656401758194
		-0.048739756602261243 -0.058085914805855461 0.15122656401758194
		-0.058085914805852366 -0.048739756602264414 0.15122656401758194
		-0.065666829419767203 -0.03791291474498909 0.15122656401758194
		-0.071252705420497928 -0.025933869904470452 0.15122656401758194
		-0.074673626506728707 -0.013166971955418454 0.15122656401758194
		-0.075825611881048194 -3.0948047784143395e-015 0.15122656401758194
		0.075825611881048194 -3.0948047784143395e-015 0.15122656401758194
		;
createNode transform -n "L_Corner_Pose" -p "Mouth__Wr_Gro";
	rename -uid "9319315E-4380-531D-9B89-ECAB673D493A";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.96226733922958307 11.797164825742676 2.3186501357823541 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -6.9038393263933862e-015 65.525735134300874 6.9038393263933862e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Corner_Mix" -p "L_Corner_Pose";
	rename -uid "4C20AA4C-49E2-A117-8341-EBB4794DB130";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Corner_Offset" -p "L_Corner_Mix";
	rename -uid "06B44561-4375-9243-2A78-65A3976A7776";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_Corner_Sel" -p "L_Corner_Offset";
	rename -uid "2E8CE299-4E33-4748-5DA2-E1BE75106973";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_Corner_Sel_Shape" -p "L_Corner_Sel";
	rename -uid "06E8DA64-4702-0B42-AECA-3CBDD47D81B1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.069271841987681451 0.078456432256657202 0.061053608497339207
		-0.066446802432803376 0.07905812128786624 0.061053608497339207
		0.066446802432805152 0.07905812128786624 0.061053608497339207
		0.06927184198768313 0.078456432256657202 0.061053608497339207
		0.071666798404658991 0.07674283796909151 0.061053608497339207
		0.073267049576029614 0.074178250791452779 0.061053608497339207
		0.073828940791459005 0.071153118405991311 0.061053608497339207
		0.073828940791459005 -0.071153118405992241 0.061053608497339221
		0.073267049576029614 -0.074178250791453723 0.061053608497339221
		0.071666798404658991 -0.076742837969092426 0.061053608497339221
		0.06927184198768313 -0.078456432256658118 0.061053608497339221
		0.066446802432805152 -0.079058121287867364 0.061053608497339221
		-0.066446802432803376 -0.079058121287867364 0.061053608497339221
		-0.069271841987681451 -0.078456432256658118 0.061053608497339221
		-0.071666798404657173 -0.076742837969092426 0.061053608497339221
		-0.073267049576027685 -0.074178250791453723 0.061053608497339221
		-0.073828940791457326 -0.071153118405992241 0.061053608497339221
		-0.073828940791457326 0.071153118405991311 0.061053608497339207
		-0.073267049576027685 0.074178250791452779 0.061053608497339207
		-0.071666798404657173 0.07674283796909151 0.061053608497339207
		-0.069271841987681451 0.078456432256657202 0.061053608497339207
		;
createNode transform -n "R_Corner_Pose" -p "Mouth__Wr_Gro";
	rename -uid "540C573E-4AEA-9BFC-EB8E-72A568185FB6";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.96226733922958385 11.797164825742671 2.3186501357823532 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -1.8583862510933521e-014 -65.525735134300874 3.1816221219854186e-014 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Corner_Mix" -p "R_Corner_Pose";
	rename -uid "718E3FA9-4F74-71EF-8099-FCAC219EB12D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Corner_Offset" -p "R_Corner_Mix";
	rename -uid "F0A56CD7-48C8-BFF8-A6B9-65BBF84C4735";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_Corner_Sel" -p "R_Corner_Offset";
	rename -uid "73686220-4273-C65A-F850-A595E93433A8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_Corner_Sel_Shape" -p "R_Corner_Sel";
	rename -uid "583F4364-4F67-B1BD-0302-EDA7B8469780";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		-0.069271841987681479 0.078456432256650138 0.061053608497339491
		-0.066446802432803473 0.079058121287859481 0.061053608497339491
		0.066446802432805166 0.079058121287859481 0.061053608497339491
		0.06927184198768313 0.078456432256650138 0.061053608497339491
		0.071666798404658866 0.076742837969084515 0.061053608497339491
		0.0732670495760296 0.074178250791445813 0.061053608497339491
		0.073828940791459088 0.071153118405984248 0.061053608497339491
		0.073828940791459088 -0.071153118405999027 0.061053608497339512
		0.0732670495760296 -0.074178250791460634 0.061053608497339512
		0.071666798404658866 -0.076742837969099503 0.061053608497339512
		0.06927184198768313 -0.078456432256665196 0.061053608497339512
		0.066446802432805166 -0.079058121287874386 0.061053608497339512
		-0.066446802432803473 -0.079058121287874386 0.061053608497339512
		-0.069271841987681479 -0.078456432256665196 0.061053608497339512
		-0.071666798404657256 -0.076742837969099503 0.061053608497339512
		-0.073267049576027699 -0.074178250791460634 0.061053608497339512
		-0.073828940791457215 -0.071153118405999027 0.061053608497339512
		-0.073828940791457215 0.071153118405984248 0.061053608497339491
		-0.073267049576027699 0.074178250791445813 0.061053608497339491
		-0.071666798404657256 0.076742837969084515 0.061053608497339491
		-0.069271841987681479 0.078456432256650138 0.061053608497339491
		;
createNode transform -n "L_UppLipInn_Pose" -p "Mouth__Wr_Gro";
	rename -uid "8C38A2EE-472D-1EE5-8782-74AABC322A14";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.5281170606613157 11.865147976224854 2.9161285255223448 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -3.2927525022109555e-015 -330 1.2288719635000849e-014 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipInn_Mix" -p "L_UppLipInn_Pose";
	rename -uid "3EA82064-4F06-BDD8-97B9-9CA6DF59D367";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipInn_Offset" -p "L_UppLipInn_Mix";
	rename -uid "7C48C009-4284-A392-66AD-7BAF18853868";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipInn_Sel" -p "L_UppLipInn_Offset";
	rename -uid "807C3D4A-4748-60CB-0745-CE9C0D545934";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppLipInn_Sel_Shape" -p "L_UppLipInn_Sel";
	rename -uid "6E4554E4-436C-EB53-C50C-3DA2689E68A7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.062665794943014663 5.2189155774762241e-015 0.13599242046699497
		-0.061713740914651309 0.010881795004480719 0.13599242046699497
		-0.058886533405369826 0.021432950334275801 0.13599242046699497
		-0.05427010695848495 0.031332987392555654 0.13599242046699497
		-0.048004888269299058 0.040280790580386437 0.13599242046699497
		-0.040280790580380803 0.048004888269304734 0.13599242046699497
		-0.031332987392550006 0.054270106958490605 0.13599242046699497
		-0.021432950334270107 0.058886533405375446 0.13599242046699497
		-0.010881795004475066 0.061713740914656971 0.13599242046699497
		4.3276050567251818e-016 0.062665794943020423 0.13599242046699497
		0.010881795004475931 0.061713740914656971 0.13599242046699497
		0.021432950334270975 0.058886533405375446 0.13599242046699497
		0.03133298739255086 0.054270106958490605 0.13599242046699497
		0.040280790580381649 0.048004888269304734 0.13599242046699497
		0.048004888269299939 0.040280790580386437 0.13599242046699497
		0.05427010695848581 0.031332987392555654 0.13599242046699497
		0.058886533405370631 0.021432950334275801 0.13599242046699497
		0.06171374091465219 0.010881795004480719 0.13599242046699497
		0.062665794943015538 5.2189155774762241e-015 0.13599242046699497
		0.062742690900174675 -0.0067364153664412965 0.13599242046699497
		0.059868345507455331 -0.0067401390101936524 0.13599242046699497
		0.055174949623046747 -0.0067436328656045362 0.13599242046699497
		0.04880527126922235 -0.0067467906649540839 0.13599242046699497
		0.040952390102145166 -0.0067495166022759042 0.13599242046699497
		0.031855400658156133 -0.0067517276816980052 0.13599242046699497
		0.021790300798029939 -0.0067533568802985063 0.13599242046699497
		0.011063226605386311 -0.006754354639619594 0.13599242046699497
		4.2886948465412749e-016 -0.0067546906322122355 0.13599242046699497
		-0.011063226605385447 -0.006754354639619594 0.13599242046699497
		-0.021790300798029079 -0.0067533568802985063 0.13599242046699497
		-0.031855400658155279 -0.0067517276816980052 0.13599242046699497
		-0.040952390102144326 -0.0067495166022759042 0.13599242046699497
		-0.048805271269221483 -0.0067467906649540839 0.13599242046699497
		-0.055174949623045907 -0.0067436328656045362 0.13599242046699497
		-0.059868345507454533 -0.0067401390101936524 0.13599242046699497
		-0.062742690900173814 -0.0067364153664412965 0.13599242046699497
		-0.062665794943014663 5.2189155774762241e-015 0.13599242046699497
		0.062665794943015538 5.2189155774762241e-015 0.13599242046699497
		;
createNode transform -n "R_UppLipInn_Pose" -p "Mouth__Wr_Gro";
	rename -uid "7021DEAE-4432-A43E-BCCC-FDAF9C085A41";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.52811706066131625 11.865147976224852 2.9161285255223444 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 3.4048674288673156e-014 -29.999999999999993 -4.1841860256838649e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipInn_Mix" -p "R_UppLipInn_Pose";
	rename -uid "2EAD6957-4DB1-3D93-A72D-C69BB001162E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipInn_Offset" -p "R_UppLipInn_Mix";
	rename -uid "27F13362-40DB-75A6-4ADF-3F88B04FCAF5";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipInn_Sel" -p "R_UppLipInn_Offset";
	rename -uid "399E5BDB-4E18-CC47-001F-B497A7233A3B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppLipInn_Sel_Shape" -p "R_UppLipInn_Sel";
	rename -uid "23A4E17B-4F79-8144-BA04-5B87CED1E7C1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.062665105110554162 1.0424374022129582e-014 0.13599242046699489
		-0.06171305108219087 0.010881795004485936 0.13599242046699489
		-0.05888584357290929 0.021432950334280949 0.13599242046699489
		-0.054269417126024483 0.031332987392560858 0.13599242046699489
		-0.04800419843683866 0.040280790580391634 0.13599242046699489
		-0.040280100747920405 0.048004888269309882 0.13599242046699489
		-0.031332315003000544 0.05427010695849574 0.13599242046699489
		-0.02143248401324279 0.058886533405380533 0.13599242046699489
		-0.010881642181229801 0.061713740914662141 0.13599242046699489
		5.8778737893577232e-016 0.062665794943025502 0.13599242046699489
		0.010881642160836829 0.061713740914662141 0.13599242046699489
		0.021432483990465007 0.058886533405380533 0.13599242046699489
		0.031332314995271691 0.05427010695849574 0.13599242046699489
		0.040280100747921509 0.048004888269309882 0.13599242046699489
		0.048004198436839771 0.040280790580391634 0.13599242046699489
		0.054269417126025697 0.031332987392560858 0.13599242046699489
		0.058885843572910511 0.021432950334280949 0.13599242046699489
		0.061713051082192105 0.010881795004485936 0.13599242046699489
		0.062665105110555341 1.0424374022129582e-014 0.13599242046699489
		0.062331066952377695 -0.006849552995694206 0.13599242046699489
		0.059475546807787938 -0.0068671691870499964 0.13599242046699489
		0.054812889867390177 -0.0068836982724246633 0.13599242046699489
		0.04848492910805538 -0.0068986375097160983 0.13599242046699489
		0.040683479629347014 -0.0069115336503457851 0.13599242046699489
		0.031646087650766264 -0.0069219940490286465 0.13599242046699489
		0.021647116309096673 -0.006929701626931347 0.13599242046699489
		0.01099061469470362 -0.0069344219278774759 0.13599242046699489
		5.8700279058902712e-016 -0.0069360114756966997 0.13599242046699489
		-0.01099061471530083 -0.0069344219278774759 0.13599242046699489
		-0.021647116332102576 -0.006929701626931347 0.13599242046699489
		-0.031646087658572512 -0.0069219940490286465 0.13599242046699489
		-0.040683479629345903 -0.0069115336503457851 0.13599242046699489
		-0.048484929108054256 -0.0068986375097160983 0.13599242046699489
		-0.054812889867388963 -0.0068836982724246633 0.13599242046699489
		-0.059475546807786703 -0.0068671691870499964 0.13599242046699489
		-0.062331066952376446 -0.006849552995694206 0.13599242046699489
		-0.062665105110554162 1.0424374022129582e-014 0.13599242046699489
		0.062665105110555341 1.0424374022129582e-014 0.13599242046699489
		;
createNode transform -n "L_UppLipMid_Pose" -p "Mouth__Wr_Gro";
	rename -uid "B6929265-4E30-D59C-27CC-6C85190A8E33";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.80481296777725275 11.8440007250957 2.6188367698460739 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -179.99999999999986 123.1277022823605 180.00000000000011 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipMid_Mix" -p "L_UppLipMid_Pose";
	rename -uid "03DE00D4-4F30-7442-BFBB-19B366CCB13A";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipMid_Offset" -p "L_UppLipMid_Mix";
	rename -uid "67B064C3-479C-F361-F90E-6C830D989E21";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipMid_Sel" -p "L_UppLipMid_Offset";
	rename -uid "88AB43BB-40D3-E094-50A4-4F8393010A74";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppLipMid_Sel_Shape" -p "L_UppLipMid_Sel";
	rename -uid "4E90FC4D-4412-57DC-9DDE-F89D477015D4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.056968904493650746 -3.1277064271861832e-015 0.088130398138339991
		-0.056103400831502274 0.0098925409131564463 0.088130398138339991
		-0.05353321218670079 0.019484500303879212 0.088130398138339991
		-0.049336460871351025 0.028484533993224568 0.088130398138339991
		-0.043640807517545642 0.036618900527616245 0.088130398138339991
		-0.03661890052761993 0.043640807517541909 0.088130398138339991
		-0.028484533993228284 0.049336460871347174 0.088130398138339991
		-0.019484500303882948 0.05353321218669712 0.088130398138339991
		-0.0098925409131601985 0.056103400831498486 0.088130398138339991
		-6.5544969686749733e-016 0.056968904493646992 0.088130398138339991
		0.0098925409131588957 0.056103400831498486 0.088130398138339991
		0.01948450030388163 0.05353321218669712 0.088130398138339991
		0.028484533993226993 0.049336460871347174 0.088130398138339991
		0.036618900527618667 0.043640807517541909 0.088130398138339991
		0.043640807517544344 0.036618900527616245 0.088130398138339991
		0.049336460871349616 0.028484533993224568 0.088130398138339991
		0.0535332121866995 0.019484500303879212 0.088130398138339991
		0.056103400831500894 0.0098925409131564463 0.088130398138339991
		0.056968904493649442 -3.1277064271861832e-015 0.088130398138339991
		0.057141067362518366 -0.0077572825440797005 0.088130398138339991
		0.05452334151505929 -0.0077624528906354781 0.088130398138339991
		0.050248968730878647 -0.0077673041719318638 0.088130398138339991
		0.044447970803127256 -0.0077716888333218071 0.088130398138339991
		0.037296189371378546 -0.0077754738464918573 0.088130398138339991
		0.029011372779081831 -0.0077785439701758032 0.088130398138339991
		0.019844877991139001 -0.0077808061418369817 0.088130398138339991
		0.01007550947585132 -0.0077821915486622276 0.088130398138339991
		-8.7187096205527319e-016 -0.0077826580804412166 0.088130398138339991
		-0.010075509475853056 -0.0077821915486622276 0.088130398138339991
		-0.019844877991140777 -0.0077808061418369817 0.088130398138339991
		-0.029011372779083559 -0.0077785439701758032 0.088130398138339991
		-0.037296189371380226 -0.0077754738464918573 0.088130398138339991
		-0.044447970803128983 -0.0077716888333218071 0.088130398138339991
		-0.050248968730880479 -0.0077673041719318638 0.088130398138339991
		-0.054523341515061031 -0.0077624528906354781 0.088130398138339991
		-0.057141067362520163 -0.0077572825440797005 0.088130398138339991
		-0.056968904493650746 -3.1277064271861832e-015 0.088130398138339991
		0.056968904493649442 -3.1277064271861832e-015 0.088130398138339991
		;
createNode transform -n "R_UppLipMid_Pose" -p "Mouth__Wr_Gro";
	rename -uid "4FDA71CC-4C1E-AEB5-18B1-4DAE04A24599";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.80481296777725231 11.8440007250957 2.6188367698460735 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -8.4980410052565123e-016 -56.87229771763942 1.4927961308776977e-014 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipMid_Mix" -p "R_UppLipMid_Pose";
	rename -uid "16233B72-4628-E108-2C1C-EC8892536E44";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipMid_Offset" -p "R_UppLipMid_Mix";
	rename -uid "C84F4005-4B3C-146D-D475-14BB0E846477";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipMid_Sel" -p "R_UppLipMid_Offset";
	rename -uid "5D04508E-457F-8155-F9DA-888DAE63BC73";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppLipMid_Sel_Shape" -p "R_UppLipMid_Sel";
	rename -uid "DD4E8A5F-4D2B-A9B9-B591-9D95FBB587B6";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.056968114866126011 -2.1902626193274505e-015 0.0881303981383392
		-0.056102611203977519 0.0098925409131573588 0.0881303981383392
		-0.053532422559175986 0.019484500303880128 0.0881303981383392
		-0.04933567124382629 0.02848453399322547 0.0881303981383392
		-0.0436400178900209 0.036618900527617126 0.0881303981383392
		-0.036618110900095306 0.043640807517542769 0.0881303981383392
		-0.028483808015348347 0.049336460871348131 0.0881303981383392
		-0.019484033101077616 0.053533212186697918 0.0881303981383392
		-0.0098923942264752089 0.056103400831499471 0.0881303981383392
		-1.0156332105446683e-015 0.056968904493647846 0.0881303981383392
		0.0098923943308643642 0.056103400831499471 0.0881303981383392
		0.019484033233235415 0.053533212186697918 0.0881303981383392
		0.028483808088439273 0.049336460871348131 0.0881303981383392
		0.03661811090009353 0.043640807517542769 0.0881303981383392
		0.043640017890019214 0.036618900527617126 0.0881303981383392
		0.049335671243824555 0.02848453399322547 0.0881303981383392
		0.05353242255917439 0.019484500303880145 0.0881303981383392
		0.056102611203975895 0.0098925409131573605 0.0881303981383392
		0.056968114866124346 -2.1902626193274505e-015 0.0881303981383392
		0.05740914499905328 -0.0079529400076268492 0.0881303981383392
		0.054779101059603395 -0.0079599369022850183 0.0881303981383392
		0.050484614588877201 -0.0079665020142792517 0.0881303981383392
		0.044656319216597226 -0.0079724356617681402 0.0881303981383392
		0.037470884030900563 -0.0079775578210169867 0.0881303981383392
		0.029147147228657525 -0.007981712539036824 0.0881303981383392
		0.019937783020229801 -0.0079847738767326766 0.0881303981383392
		0.010122771263954255 -0.0079866487115257331 0.0881303981383392
		-1.0237724533024045e-015 -0.0079872800567706119 0.0881303981383392
		-0.010122771157134027 -0.0079866487115257331 0.0881303981383392
		-0.019937782884994239 -0.0079847738767326766 0.0881303981383392
		-0.029147147153864395 -0.007981712539036824 0.0881303981383392
		-0.037470884030902298 -0.0079775578210169867 0.0881303981383392
		-0.044656319216598898 -0.0079724356617681402 0.0881303981383392
		-0.050484614588878901 -0.0079665020142792517 0.0881303981383392
		-0.054779101059604943 -0.0079599369022850183 0.0881303981383392
		-0.057409144999054848 -0.0079529400076268492 0.0881303981383392
		-0.056968114866126011 -2.1902626193274505e-015 0.0881303981383392
		0.056968114866124346 -2.1902626193274505e-015 0.0881303981383392
		;
createNode transform -n "L_UppLipOut_Pose" -p "Mouth__Wr_Gro";
	rename -uid "3F5C6A8A-4528-63E8-44C7-9691B60D1B94";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.93239623308181774 11.815491585081052 2.3946088645726356 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -179.99999999999991 114.47426486569908 180.00000000000003 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipOut_Mix" -p "L_UppLipOut_Pose";
	rename -uid "FD427482-4581-FFFA-0B03-F980855E4674";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipOut_Offset" -p "L_UppLipOut_Mix";
	rename -uid "0C8D163A-428C-2CFE-9DE5-CFAA3DEE245D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_UppLipOut_Sel" -p "L_UppLipOut_Offset";
	rename -uid "11BFF152-4E14-BC85-0D01-4C944F0644E3";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_UppLipOut_Sel_Shape" -p "L_UppLipOut_Sel";
	rename -uid "FC2C589D-40AA-156D-B52E-E693FAFE6B2A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.040110839488197568 8.7415583443199801e-015 0.065817485157356165
		-0.039501453038213299 0.0069651702841310864 0.065817485157356165
		-0.037691826802597153 0.013718706216026706 0.065817485157356165
		-0.034736965376384432 0.02005547730036351 0.065817485157356165
		-0.030726752445567541 0.025782746822204567 0.065817485157356165
		-0.025782746822195311 0.030726752445576825 0.065817485157356165
		-0.020055477300354292 0.034736965376393626 0.065817485157356165
		-0.013718706216017463 0.037691826802606306 0.065817485157356165
		-0.0069651702841218204 0.039501453038222514 0.065817485157356165
		4.9179410543942481e-016 0.040110839488206915 0.065817485157356165
		0.006965170284122856 0.039501453038222514 0.065817485157356165
		0.013718706216018492 0.037691826802606306 0.065817485157356165
		0.020055477300355305 0.034736965376393626 0.065817485157356165
		0.025782746822196355 0.030726752445576825 0.065817485157356165
		0.030726752445568647 0.025782746822204567 0.065817485157356165
		0.034736965376385459 0.02005547730036351 0.065817485157356165
		0.037691826802598145 0.013718706216026706 0.065817485157356165
		0.039501453038214354 0.0069651702841310864 0.065817485157356165
		0.040110839488198699 8.7415583443199801e-015 0.065817485157356165
		0.040176534498376847 -0.0063509262849424939 0.065817485157356165
		0.038335981675824547 -0.0063716328692799851 0.065817485157356165
		0.035330621546076683 -0.0063910616375886841 0.065817485157356165
		0.031251873911023062 -0.0064086216521608216 0.065817485157356165
		0.026223375027819303 -0.0064237801514177642 0.065817485157356165
		0.020398226233845958 -0.0064360756086568639 0.065817485157356165
		0.013953159470558012 -0.0064451353201834573 0.065817485157356165
		0.0070842053312928036 -0.0064506836993799303 0.065817485157356165
		4.8122512972689292e-016 -0.0064525521001773771 0.065817485157356165
		-0.0070842053312917897 -0.0064506836993799303 0.065817485157356165
		-0.013953159470557005 -0.0064451353201834573 0.065817485157356165
		-0.020398226233844952 -0.0064360756086568639 0.065817485157356165
		-0.026223375027818272 -0.0064237801514177642 0.065817485157356165
		-0.031251873911021945 -0.0064086216521608216 0.065817485157356165
		-0.035330621546075643 -0.0063910616375886841 0.065817485157356165
		-0.038335981675823555 -0.0063716328692799851 0.065817485157356165
		-0.040176534498375778 -0.0063509262849424939 0.065817485157356165
		-0.040110839488197568 8.7415583443199801e-015 0.065817485157356165
		0.040110839488198699 8.7415583443199801e-015 0.065817485157356165
		;
createNode transform -n "R_UppLipOut_Pose" -p "Mouth__Wr_Gro";
	rename -uid "7B26C52F-4C7D-6D14-7D01-1A80ECA21F74";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.93239623308181729 11.81549158508105 2.3946088645726369 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 7.9424973473757947e-015 -65.525735134300888 5.2898613615448611e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipOut_Mix" -p "R_UppLipOut_Pose";
	rename -uid "F507F932-48A3-737D-7983-4AA3F921F667";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipOut_Offset" -p "R_UppLipOut_Mix";
	rename -uid "C19ED98F-4DF6-377C-D7FC-BD995B3611A2";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_UppLipOut_Sel" -p "R_UppLipOut_Offset";
	rename -uid "F76886E1-4EA1-4D7D-683F-9A8B97C8A45F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_UppLipOut_Sel_Shape" -p "R_UppLipOut_Sel";
	rename -uid "7276FC40-48CD-808B-3C1B-D1BA202E9D21";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.040110839488196992 1.9643017107270204e-014 0.065817485157360314
		-0.039501453038212626 0.0069651702841420143 0.065817485157360314
		-0.037691826802596411 0.013718706216037612 0.065817485157360314
		-0.034736965376383711 0.02005547730037438 0.065817485157360314
		-0.030726752445566947 0.025782746822215458 0.065817485157360314
		-0.025782746822194617 0.030726752445587712 0.065817485157360314
		-0.020055477300353657 0.034736965376404506 0.065817485157360314
		-0.013718706216016886 0.037691826802617165 0.065817485157360314
		-0.0069651702841213156 0.039501453038233381 0.065817485157360314
		9.8189883079907276e-016 0.040110839488217774 0.065817485157360314
		0.0069651702841232828 0.039501453038233381 0.065817485157360314
		0.01371870621601887 0.037691826802617165 0.065817485157360314
		0.020055477300355683 0.034736965376404506 0.065817485157360314
		0.025782746822196667 0.030726752445587712 0.065817485157360314
		0.030726752445568949 0.025782746822215458 0.065817485157360314
		0.034736965376385792 0.02005547730037438 0.065817485157360314
		0.037691826802598381 0.013718706216037612 0.065817485157360314
		0.039501453038214521 0.0069651702841420143 0.065817485157360314
		0.040110839488198921 1.9643017107270204e-014 0.065817485157360314
		0.040025567626325032 -0.0065159679508130109 0.065817485157360314
		0.038191930843345039 -0.0065112050550803612 0.065817485157360314
		0.035197863619365312 -0.0065067360805667303 0.065817485157360314
		0.031134442238306428 -0.0065026969538277508 0.065817485157360314
		0.026124838383182896 -0.0064992102198378346 0.065817485157360314
		0.020321578099596106 -0.0064963820382381732 0.065817485157360314
		0.013900729243142711 -0.0064942981377422932 0.065817485157360314
		0.0070575858049153001 -0.0064930219083474639 0.065817485157360314
		5.4199926559709825e-016 -0.0064925921417553515 0.065817485157360314
		-0.0070575858049142185 -0.0064930219083474639 0.065817485157360314
		-0.013900729243141606 -0.0064942981377422932 0.065817485157360314
		-0.020321578099594947 -0.0064963820382381732 0.065817485157360314
		-0.026124838383181713 -0.0064992102198378346 0.065817485157360314
		-0.031134442238305297 -0.0065026969538277508 0.065817485157360314
		-0.035197863619364105 -0.0065067360805667303 0.065817485157360314
		-0.038191930843343949 -0.0065112050550803612 0.065817485157360314
		-0.040025567626324005 -0.0065159679508130109 0.065817485157360314
		-0.040110839488196992 1.9643017107270204e-014 0.065817485157360314
		0.040110839488198921 1.9643017107270204e-014 0.065817485157360314
		;
createNode transform -n "L_LowLipInn_Pose" -p "Mouth__Wr_Gro";
	rename -uid "FFC3EEFB-4B24-16DB-797C-0CA70F5E8B24";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.52624768018722534 11.806707767789792 2.9183205459386015 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 360 391 2.7012332319855887e-014 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipInn_Mix" -p "L_LowLipInn_Pose";
	rename -uid "32EC2954-4949-1BCD-314B-0BBC0089F948";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipInn_Offset" -p "L_LowLipInn_Mix";
	rename -uid "EA9A4A13-4CBF-1417-7A46-5593E809696A";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipInn_Sel" -p "L_LowLipInn_Offset";
	rename -uid "6333A356-4174-89F7-090E-4ABA05028AAD";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowLipInn_Sel_Shape" -p "L_LowLipInn_Sel";
	rename -uid "43768E66-41BB-133A-AD64-EBA260869542";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.062665794943014788 -1.2823943296158546e-015 0.13599242046699431
		-0.062323681587323251 0.0082111775666861495 0.13599242046699431
		-0.059468531697229231 0.0082042902650247482 0.13599242046699431
		-0.054806479329591241 0.0081978279829758791 0.13599242046699431
		-0.048479339070831469 0.0081919872747460085 0.13599242046699431
		-0.04067890114924648 0.0081869453443428469 0.13599242046699431
		-0.031642663375949953 0.0081828557020486511 0.13599242046699431
		-0.02164478043807657 0.0081798423143633614 0.13599242046699431
		-0.010989343976009544 0.0081779968452777227 0.13599242046699431
		2.7525561001177208e-016 0.0081773753888503969 0.13599242046699431
		0.010989343976010105 0.0081779968452777227 0.13599242046699431
		0.021644780438077119 0.0081798423143633614 0.13599242046699431
		0.031642663375950536 0.0081828557020486511 0.13599242046699431
		0.040678901149246952 0.0081869453443428469 0.13599242046699431
		0.048479339070832003 0.0081919872747460085 0.13599242046699431
		0.054806479329591831 0.0081978279829758791 0.13599242046699431
		0.059468531697229744 0.0082042902650247482 0.13599242046699431
		0.062323681587323779 0.0082111775666861495 0.13599242046699431
		0.062665794943015399 -1.2823943296158546e-015 0.13599242046699431
		0.061713740914652031 -0.010881795004476804 0.13599242046699431
		0.058886533405370381 -0.021432950334271804 0.13599242046699431
		0.054270106958485623 -0.031332987392551692 0.13599242046699431
		0.048004888269299779 -0.040280790580382517 0.13599242046699431
		0.040280790580381497 -0.048004888269300744 0.13599242046699431
		0.031332987392550693 -0.05427010695848658 0.13599242046699431
		0.021432950334270832 -0.058886533405371456 0.13599242046699431
		0.010881795004475793 -0.061713740914652995 0.13599242046699431
		2.747348520043898e-016 -0.062665794943016342 0.13599242046699431
		-0.010881795004475232 -0.061713740914652995 0.13599242046699431
		-0.021432950334270284 -0.058886533405371456 0.13599242046699431
		-0.031332987392550124 -0.05427010695848658 0.13599242046699431
		-0.040280790580381025 -0.048004888269300744 0.13599242046699431
		-0.048004888269299245 -0.040280790580382517 0.13599242046699431
		-0.05427010695848504 -0.031332987392551692 0.13599242046699431
		-0.058886533405369867 -0.021432950334271804 0.13599242046699431
		-0.061713740914651503 -0.010881795004476804 0.13599242046699431
		-0.062665794943014788 -1.2823943296158546e-015 0.13599242046699431
		0.062665794943015399 -1.2823943296158546e-015 0.13599242046699431
		;
createNode transform -n "R_LowLipInn_Pose" -p "Mouth__Wr_Gro";
	rename -uid "3ADD8E86-42C1-F494-73D6-419B784D94BC";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.52624768018722523 11.806707767789792 2.9183205459386024 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 2.1258140876777859e-014 -30.999999999999993 7.0578748763024689e-016 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipInn_Mix" -p "R_LowLipInn_Pose";
	rename -uid "97B6C862-4CB8-A4C9-9A63-2B9187DD705B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipInn_Offset" -p "R_LowLipInn_Mix";
	rename -uid "B0E3C02B-4C03-03D2-5166-3EACDE176D41";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipInn_Sel" -p "R_LowLipInn_Offset";
	rename -uid "2D91D0F3-4485-EF3E-8B41-31B1BDE96A62";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowLipInn_Sel_Shape" -p "R_LowLipInn_Sel";
	rename -uid "5B866889-4E98-710F-C655-9F80C854D3FA";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.062663587517845495 4.1929613126903951e-015 0.13599242046699375
		-0.062365188120036989 0.0085817245989652513 0.13599242046699375
		-0.059508034550829751 0.0085753895021782028 0.13599242046699375
		-0.054842710461105802 0.0085694453481022885 0.13599242046699375
		-0.0485111299595316 0.0085640729317692527 0.13599242046699375
		-0.040705217868414488 0.0085594352494565533 0.13599242046699375
		-0.031662694985220313 0.0085556735034157377 0.13599242046699375
		-0.02165846197117954 0.0085529017208538175 0.13599242046699375
		-0.010996561598441078 0.0085512042163959044 0.13599242046699375
		5.4797735765064173e-016 0.0085506325866333364 0.13599242046699375
		0.010996562018616082 0.0085512042163959044 0.13599242046699375
		0.021658462445072975 0.0085529017208538175 0.13599242046699375
		0.031662695143983358 0.0085556735034157377 0.13599242046699375
		0.040705217868415577 0.0085594352494565533 0.13599242046699375
		0.048511129959532745 0.0085640729317692527 0.13599242046699375
		0.054842710461106864 0.0085694453481022885 0.13599242046699375
		0.059508034550830834 0.0085753895021782028 0.13599242046699375
		0.062365188120038134 0.0085817245989652513 0.13599242046699375
		0.062663587517846481 4.1929613126903951e-015 0.13599242046699375
		0.061711533489483245 -0.010881795004471315 0.13599242046699375
		0.058884325980201629 -0.021432950334266336 0.13599242046699375
		0.054267899533316767 -0.031332987392546217 0.13599242046699375
		0.048002680844130965 -0.040280790580377056 0.13599242046699375
		0.040278583155212717 -0.048004888269295297 0.13599242046699375
		0.031330835850031144 -0.054270106958481161 0.13599242046699375
		0.021431458331164572 -0.058886533405366016 0.13599242046699375
		0.010881306153920913 -0.061713740914647597 0.13599242046699375
		5.4921576512855529e-016 -0.062665794943010861 0.13599242046699375
		-0.010881305738149783 -0.061713740914647597 0.13599242046699375
		-0.021431457862238015 -0.058886533405366016 0.13599242046699375
		-0.031330835692932109 -0.054270106958481161 0.13599242046699375
		-0.040278583155211635 -0.048004888269295297 0.13599242046699375
		-0.048002680844129841 -0.040280790580377056 0.13599242046699375
		-0.054267899533315705 -0.031332987392546217 0.13599242046699375
		-0.058884325980200547 -0.021432950334266336 0.13599242046699375
		-0.06171153348948212 -0.010881795004471315 0.13599242046699375
		-0.062663587517845495 4.1929613126903951e-015 0.13599242046699375
		0.062663587517846481 4.1929613126903951e-015 0.13599242046699375
		;
createNode transform -n "L_LowLipMid_Pose" -p "Mouth__Wr_Gro";
	rename -uid "5C427937-4839-F27C-15C9-25B491A2C884";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.79890537261962891 11.797455696409177 2.6151455734044227 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -179.99999999999994 123.12770228236062 180.00000000000003 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipMid_Mix" -p "L_LowLipMid_Pose";
	rename -uid "C73AF006-4050-BB08-CAA6-3A98D8226D36";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipMid_Offset" -p "L_LowLipMid_Mix";
	rename -uid "3BE16DAD-469B-F098-736A-CE9E757D1496";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipMid_Sel" -p "L_LowLipMid_Offset";
	rename -uid "40C86AB8-4D14-3579-EC88-F483EBCC840D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowLipMid_Sel_Shape" -p "L_LowLipMid_Sel";
	rename -uid "A37AA730-485F-1C79-4819-078D89F74B04";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.056968904493650607 -4.370899572855795e-015 0.08813039813834013
		-0.057144440495126299 0.008129613287975089 0.08813039813834013
		-0.054526560118939998 0.008140102381153938 0.08813039813834013
		-0.050251935011397734 0.0081499441859546919 0.08813039813834013
		-0.044450594641053533 0.0081588393579476795 0.08813039813834013
		-0.037298391027706587 0.0081665180223070826 0.08813039813834013
		-0.029013085368854597 0.0081727463888283565 0.08813039813834013
		-0.019846049467420423 0.0081773356613431703 0.08813039813834013
		-0.010076104249998804 0.0081801462391494825 0.08813039813834013
		-7.3194110744063892e-016 0.0081810926931730199 0.08813039813834013
		0.010076104249997357 0.0081801462391494825 0.08813039813834013
		0.019846049467418928 0.0081773356613431703 0.08813039813834013
		0.029013085368852817 0.0081727463888283565 0.08813039813834013
		0.03729839102770479 0.0081665180223070826 0.08813039813834013
		0.044450594641051645 0.0081588393579476795 0.08813039813834013
		0.050251935011395743 0.0081499441859546919 0.08813039813834013
		0.054526560118938097 0.008140102381153938 0.08813039813834013
		0.05714444049512437 0.008129613287975089 0.08813039813834013
		0.05696890449364965 -4.370899572855795e-015 0.08813039813834013
		0.056103400831501053 -0.0098925409131639334 0.08813039813834013
		0.053533212186699645 -0.019484500303886675 0.08813039813834013
		0.049336460871349803 -0.028484533993231996 0.08813039813834013
		0.043640807517544525 -0.036618900527623593 0.08813039813834013
		0.036618900527618854 -0.043640807517549257 0.08813039813834013
		0.028484533993227236 -0.049336460871354543 0.08813039813834013
		0.019484500303882029 -0.05353321218670444 0.08813039813834013
		0.0098925409131592704 -0.05610340083150589 0.08813039813834013
		-2.8268763040875128e-016 -0.056968904493654368 0.08813039813834013
		-0.0098925409131598238 -0.05610340083150589 0.08813039813834013
		-0.019484500303882601 -0.05353321218670444 0.08813039813834013
		-0.028484533993228079 -0.049336460871354543 0.08813039813834013
		-0.036618900527619701 -0.043640807517549257 0.08813039813834013
		-0.043640807517545475 -0.036618900527623593 0.08813039813834013
		-0.049336460871350858 -0.028484533993231996 0.08813039813834013
		-0.053533212186700617 -0.019484500303886675 0.08813039813834013
		-0.056103400831502032 -0.0098925409131639334 0.08813039813834013
		-0.056968904493650607 -4.370899572855795e-015 0.08813039813834013
		0.05696890449364965 -4.370899572855795e-015 0.08813039813834013
		;
createNode transform -n "R_LowLipMid_Pose" -p "Mouth__Wr_Gro";
	rename -uid "C8B9B6ED-4D7B-9E47-C6B5-0C8A34B71EEE";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.79890537261962946 11.797455696409177 2.6151455734044227 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -8.4980410052565123e-016 -56.87229771763942 1.4927961308776977e-014 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipMid_Mix" -p "R_LowLipMid_Pose";
	rename -uid "AF291D36-44BE-EBB4-0BFD-F5AB9AAB7627";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipMid_Offset" -p "R_LowLipMid_Mix";
	rename -uid "C6EDDED3-4F95-F7C2-9001-A3A7DBCC0477";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipMid_Sel" -p "R_LowLipMid_Offset";
	rename -uid "CD21E8F6-4B48-8762-9699-DFA6D0538C65";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowLipMid_Sel_Shape" -p "R_LowLipMid_Sel";
	rename -uid "953F71BC-4843-351D-7C83-70A446149EBD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.056965112770071574 2.9802243962223093e-015 0.088130398138339505
		-0.056904947014532047 0.0082677527143775811 0.088130398138339505
		-0.05429786202810339 0.008257533159983052 0.088130398138339505
		-0.050040864251635529 0.0082479442605627798 0.088130398138339505
		-0.044263446949352366 0.0082392776682767913 0.088130398138339505
		-0.037140736977630685 0.0082317963229631072 0.088130398138339505
		-0.028889907525480044 0.008225728007107018 0.088130398138339505
		-0.019761934270195857 0.0082212566653716915 0.088130398138339505
		-0.010033838716696225 0.0082185183111324958 0.088130398138339505
		-3.2786396904671395e-016 0.0082175961781882495 0.088130398138339505
		0.010033839372805484 0.0082185183111324958 0.088130398138339505
		0.019761935098700133 0.0082212566653716915 0.088130398138339505
		0.02888990798489385 0.008225728007107018 0.088130398138339505
		0.037140736977630047 0.0082317963229631072 0.088130398138339505
		0.044263446949351706 0.0082392776682767913 0.088130398138339505
		0.05004086425163478 0.0082479442605627798 0.088130398138339505
		0.0542978620281028 0.008257533159983052 0.088130398138339505
		0.056904947014531367 0.0082677527143775811 0.088130398138339505
		0.056965112770070887 2.9802243962223093e-015 0.088130398138339505
		0.05609960910792245 -0.0098925409131565521 0.088130398138339505
		0.053529420463121015 -0.019484500303879316 0.088130398138339505
		0.049332669147771117 -0.028484533993224679 0.088130398138339505
		0.043637015793965811 -0.036618900527616342 0.088130398138339505
		0.036615108804040175 -0.043640807517541992 0.088130398138339505
		0.028481048312065452 -0.049336460871347305 0.088130398138339505
		0.019482257561369953 -0.053533212186697224 0.088130398138339505
		0.0098918371107933212 -0.056103400831498583 0.088130398138339505
		-3.2950882765803617e-016 -0.056968904493647152 0.088130398138339505
		-0.0098918364639695566 -0.056103400831498583 0.088130398138339505
		-0.019482256744590948 -0.053533212186697224 0.088130398138339505
		-0.028481047859153421 -0.049336460871347305 0.088130398138339505
		-0.036615108804040793 -0.043640807517541992 0.088130398138339505
		-0.043637015793966477 -0.036618900527616342 0.088130398138339505
		-0.049332669147771846 -0.028484533993224679 0.088130398138339505
		-0.053529420463121591 -0.019484500303879316 0.088130398138339505
		-0.05609960910792311 -0.0098925409131565521 0.088130398138339505
		-0.056965112770071574 2.9802243962223093e-015 0.088130398138339505
		0.056965112770070887 2.9802243962223093e-015 0.088130398138339505
		;
createNode transform -n "L_LowLipOut_Pose" -p "Mouth__Wr_Gro";
	rename -uid "8EE260AD-431F-6DD5-36CD-2EB374F7DBF6";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.92712819576263428 11.790369896238278 2.3929828498631638 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 179.99999999999994 114.4742648656991 -179.99999999999994 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipOut_Mix" -p "L_LowLipOut_Pose";
	rename -uid "9EE4A5A8-4406-9D15-AC1D-0E8E9DF24C46";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipOut_Offset" -p "L_LowLipOut_Mix";
	rename -uid "C264CDBA-4700-90F9-382B-ACBD36F1BED7";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "L_LowLipOut_Sel" -p "L_LowLipOut_Offset";
	rename -uid "18CA61F8-42DD-0D63-D4FD-3EAE6F1847C7";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "L_LowLipOut_Sel_Shape" -p "L_LowLipOut_Sel";
	rename -uid "8F604FA4-4B0C-28D1-AD86-D69850905651";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.040110839488198151 -6.9140812806839727e-015 0.065817485157355651
		-0.040106300105662435 0.0060284372802203758 0.065817485157356317
		-0.03826896483562843 0.0060646808666485657 0.065817485157356317
		-0.035268858510028533 0.0060986878391126147 0.065817485157356317
		-0.031197241115717395 0.0061294238550316264 0.065817485157356317
		-0.026177532775792985 0.0061559563998968931 0.065817485157356317
		-0.020362567184356143 0.0061774776445336676 0.065817485157356317
		-0.013928767329868813 0.0061933352303323135 0.065817485157356317
		-0.0070718211158408662 0.0062030467866984471 0.065817485157356317
		5.1934110226172187e-016 0.0062063171254796226 0.065817485157356317
		0.0070718211158418282 0.0062030467866984471 0.065817485157356317
		0.013928767329869784 0.0061933352303323135 0.065817485157356317
		0.020362567184357146 0.0061774776445336676 0.065817485157356317
		0.026177532775793981 0.0061559563998968931 0.065817485157356317
		0.031197241115718283 0.0061294238550316264 0.065817485157356317
		0.035268858510029165 0.0060986878391126147 0.065817485157356317
		0.038268964835629096 0.0060646808666485657 0.065817485157356317
		0.040106300105663011 0.0060284372802203758 0.065817485157356317
		0.040110839488198297 -6.9140812806839727e-015 0.065817485157355651
		0.039501453038213799 -0.0069651702841292823 0.065817485157355651
		0.037691826802597743 -0.013718706216024888 0.065817485157355651
		0.034736965376385029 -0.020055477300361627 0.065817485157355651
		0.03072675244556829 -0.025782746822202683 0.065817485157355651
		0.025782746822196084 -0.030726752445574983 0.065817485157355651
		0.020055477300355076 -0.034736965376391829 0.065817485157355651
		0.01371870621601824 -0.037691826802604522 0.065817485157355651
		0.0069651702841226088 -0.039501453038220682 0.065817485157355651
		2.9281293953895792e-016 -0.040110839488205013 0.065817485157355651
		-0.0069651702841220988 -0.039501453038220682 0.065817485157355651
		-0.013718706216017722 -0.037691826802604522 0.065817485157355651
		-0.020055477300354521 -0.034736965376391829 0.065817485157355651
		-0.025782746822195536 -0.030726752445574983 0.065817485157355651
		-0.030726752445567843 -0.025782746822202683 0.065817485157355651
		-0.034736965376384835 -0.020055477300361627 0.065817485157355651
		-0.037691826802597514 -0.013718706216024888 0.065817485157355651
		-0.039501453038213674 -0.0069651702841292823 0.065817485157355651
		-0.040110839488198151 -6.9140812806839727e-015 0.065817485157355651
		0.040110839488198297 -6.9140812806839727e-015 0.065817485157355651
		;
createNode transform -n "R_LowLipOut_Pose" -p "Mouth__Wr_Gro";
	rename -uid "DB062135-44D5-3DEC-9C7F-AA96AE5C191A";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -0.92712819576263461 11.790369896238278 2.3929828498631647 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" -1.8583862510933521e-014 -65.525735134300874 3.1816221219854186e-014 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipOut_Mix" -p "R_LowLipOut_Pose";
	rename -uid "21C5EB2E-464F-4D7E-E02F-639CC4734A2D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipOut_Offset" -p "R_LowLipOut_Mix";
	rename -uid "D11936E9-411F-9E1F-11EA-6B8759837035";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_LowLipOut_Sel" -p "R_LowLipOut_Offset";
	rename -uid "44104E6E-4879-2ABA-61A1-34B221433D60";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "R_LowLipOut_Sel_Shape" -p "R_LowLipOut_Sel";
	rename -uid "E7C3DB01-4FB0-F848-8270-C4907B7AF4C3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37
		38
		-0.040112349278794042 -1.8195604813926312e-015 0.065817485157356734
		-0.040158088076275786 0.0060932702383430896 0.065817485157356956
		-0.038318389612593075 0.0061005743217260114 0.065817485157356956
		-0.035314407055676122 0.0061074276656402499 0.065817485157356956
		-0.031237501073097761 0.0061136218214966516 0.065817485157356956
		-0.026211245197734555 0.0061189688618741543 0.065817485157356956
		-0.020388688391596209 0.0061233059868891632 0.065817485157356956
		-0.013946527675462721 0.0061265017282696246 0.065817485157356956
		-0.0070807668007527432 0.0061284588750221032 0.065817485157356956
		-7.918421976473029e-012 0.0061291179385834851 0.065817485157356956
		0.0070807667972550168 0.0061284588750221032 0.065817485157356956
		0.013946527681915935 0.0061265017282696246 0.065817485157356956
		0.020388688403223863 0.0061233059868891632 0.065817485157356956
		0.026211245210556285 0.0061189688618741543 0.065817485157356956
		0.031237501083730256 0.0061136218214966516 0.065817485157356956
		0.035314407062626889 0.0061074276656402499 0.065817485157356956
		0.038318389615861904 0.0061005743217260114 0.065817485157356956
		0.040158088077255918 0.0060932702383430896 0.065817485157356956
		0.040112349278795777 -1.8195604813926312e-015 0.065817485157356734
		0.03950294487944124 -0.0069651702841241735 0.065817485157356734
		0.037693259448814749 -0.013718706216019786 0.065817485157356734
		0.034738284177309488 -0.020055477300356617 0.065817485157356734
		0.030727889263757881 -0.025782746822197639 0.065817485157356734
		0.025783632248186205 -0.030726752445569851 0.065817485157356734
		0.020056065234165723 -0.034736965376386701 0.065817485157356734
		0.013719002588436668 -0.037691826802599394 0.065817485157356734
		0.0069652504361838027 -0.039501453038215638 0.065817485157356734
		-7.7810232114666399e-012 -0.040110839488200017 0.065817485157356734
		-0.0069652504396080324 -0.039501453038215638 0.065817485157356734
		-0.013719002582072305 -0.037691826802599394 0.065817485157356734
		-0.020056065222711326 -0.034736965376386701 0.065817485157356734
		-0.025783632235557206 -0.030726752445569851 0.065817485157356734
		-0.030727889253282403 -0.025782746822197639 0.065817485157356734
		-0.034738284170455679 -0.020055477300356617 0.065817485157356734
		-0.037693259445582807 -0.013718706216019786 0.065817485157356734
		-0.03950294487846065 -0.0069651702841241735 0.065817485157356734
		-0.040112349278794042 -1.8195604813926312e-015 0.065817485157356734
		0.040112349278795777 -1.8195604813926312e-015 0.065817485157356734
		;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "3DF09334-4D7E-BA86-C65C-9ABA516CDC64";
	setAttr -s 23 ".lnk";
	setAttr -s 21 ".slnk";
createNode displayLayerManager -n "layerManager";
	rename -uid "1AAFD2A2-42B1-5DC4-84D3-6EBA9E66BEB4";
	setAttr ".cdl" 13;
	setAttr -s 14 ".dli[1:13]"  1 2 3 4 5 6 9 8 
		7 10 12 11 13;
createNode displayLayer -n "defaultLayer";
	rename -uid "BA350809-4520-90BA-6CB2-FAA2283CDD01";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "C76BFCDC-4CF0-267E-E1B5-C08B2496F936";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "6CD661F6-4470-5FEA-D2B6-B1ADB741C04B";
	setAttr ".g" yes;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
	rename -uid "CFB960CA-4B74-AFA1-F612-8CB8315B23F7";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
	rename -uid "1AC1D242-460F-7AE9-B961-37A456A31A1B";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
	rename -uid "387C4FCB-44F0-A04D-A400-7198FAD955A8";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
	rename -uid "C048DFBF-4978-30EA-8D70-63B055510F95";
lockNode -l 1 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "6F8B5B34-4A24-41E2-8516-539A8C1E64C7";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 1\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 0\n                -polymeshes 1\n                -subdivSurfaces 0\n                -planes 0\n                -lights 0\n                -cameras 0\n                -controlVertices 0\n"
		+ "                -hulls 0\n                -grid 1\n                -imagePlane 0\n                -joints 0\n                -ikHandles 0\n                -deformers 0\n                -dynamics 0\n                -particleInstancers 1\n                -fluids 0\n                -hairSystems 0\n                -follicles 0\n                -nCloths 0\n                -nParticles 0\n                -nRigids 0\n                -dynamicConstraints 0\n                -locators 0\n                -manipulators 1\n                -pluginShapes 0\n                -dimensions 0\n                -handles 0\n                -pivots 0\n                -textures 0\n                -strokes 0\n                -motionTrails 0\n                -clipGhosts 0\n                -greasePencils 0\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n"
		+ "            -nurbsCurves 1\n            -nurbsSurfaces 0\n            -polymeshes 1\n            -subdivSurfaces 0\n            -planes 0\n            -lights 0\n            -cameras 0\n            -controlVertices 0\n            -hulls 0\n            -grid 1\n            -imagePlane 0\n            -joints 0\n            -ikHandles 0\n            -deformers 0\n            -dynamics 0\n            -particleInstancers 1\n            -fluids 0\n            -hairSystems 0\n            -follicles 0\n            -nCloths 0\n            -nParticles 0\n            -nRigids 0\n            -dynamicConstraints 0\n            -locators 0\n            -manipulators 1\n            -pluginShapes 0\n            -dimensions 0\n            -handles 0\n            -pivots 0\n            -textures 0\n            -strokes 0\n            -motionTrails 0\n            -clipGhosts 0\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n"
		+ "        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 0 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n"
		+ "                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n"
		+ "            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n"
		+ "            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n"
		+ "            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n"
		+ "                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n"
		+ "                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n"
		+ "            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n"
		+ "            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n"
		+ "            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 1\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 0\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 794\n                -height 730\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n"
		+ "            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 794\n            -height 730\n            -sceneRenderFilter 0\n            $editorName;\n"
		+ "        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n                -showReferenceNodes 1\n                -showReferenceMembers 1\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n"
		+ "                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n"
		+ "                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n"
		+ "            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n"
		+ "            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n"
		+ "                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n"
		+ "                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n"
		+ "                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n"
		+ "                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n"
		+ "                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n"
		+ "                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n"
		+ "                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n"
		+ "                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n"
		+ "                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n"
		+ "                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n"
		+ "                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n"
		+ "                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n"
		+ "\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n"
		+ "\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"VFBPanelType\" (localizedPanelLabel(\"V-Ray Frame Buffer\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"VFBPanelType\" -l (localizedPanelLabel(\"V-Ray Frame Buffer\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"V-Ray Frame Buffer\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n"
		+ "                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n"
		+ "                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"profilerPanel\" -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n"
		+ "        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 31 100 -ps 2 69 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Outliner\")) \n\t\t\t\t\t\"outlinerPanel\"\n\t\t\t\t\t\"$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 1\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t\t\"outlinerPanel -edit -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 1\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 0\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 794\\n    -height 730\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 0\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 794\\n    -height 730\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 50 -size 100 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "48EC0EAB-4591-13C7-DA5C-B08AB83CAFF8";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 30 -ast 1 -aet 48 ";
	setAttr ".st" 6;
createNode network -n "DescriptionInformation";
	rename -uid "363F9566-4AEC-FF22-A132-F98204B517D7";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2016-07-08 19:23:30";
	setAttr -k on ".Description" -type "string" "修改眼睛大小和眼球";
lockNode -l 1 ;
createNode aiOptions -s -n "defaultArnoldRenderOptions";
	rename -uid "C270581E-491D-781E-CC96-17A4D5599719";
	setAttr ".texture_automip" no;
	setAttr ".usetx" yes;
	setAttr ".version" -type "string" "1.2.4.2";
createNode aiAOVFilter -s -n "defaultArnoldFilter";
	rename -uid "C0FA45E8-4D2C-140E-B49E-D49B269DCCDA";
	setAttr ".ai_translator" -type "string" "gaussian";
createNode aiAOVDriver -s -n "defaultArnoldDriver";
	rename -uid "B0093C64-4A53-2474-3822-C591CF5CA1AE";
	setAttr ".ai_translator" -type "string" "exr";
createNode aiAOVDriver -s -n "defaultArnoldDisplayDriver";
	rename -uid "5EDDA78A-494F-31AB-F144-A0B96A89067C";
	setAttr ".output_mode" 0;
	setAttr ".ai_translator" -type "string" "maya";
createNode network -n "DescriptionInformation4";
	rename -uid "05709C10-4503-2016-B9BB-6BA42B80DFBB";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2016-07-08 19:23:30";
	setAttr -k on ".Description" -type "string" "修改眼睛大小和眼球";
lockNode -l 1 ;
createNode script -n "xgenGlobals3";
	rename -uid "CBB89FC1-4B47-61CA-F637-ABA49F7EC6B4";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode network -n "DescriptionInformation1";
	rename -uid "9BA2496D-4EC8-8868-B7EF-BEBA903F533B";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "PIC-SH-116";
	setAttr -k on ".Time" -type "string" "2016-06-27 10:47:44";
	setAttr -k on ".Description" -type "string" "更新贴图";
lockNode -l 1 ;
createNode network -n "DescriptionInformation2";
	rename -uid "F1346C96-4D8A-7F75-6F8B-A39129A7E1A6";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "zoomer";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/zoomer";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2015-04-03 15:17:13";
	setAttr -k on ".Description" -type "string" "v004";
lockNode -l 1 ;
createNode groupId -n "groupId9";
	rename -uid "A12B55CB-4D9E-CA78-5408-2CB65AD0EDDC";
	setAttr ".ihi" 0;
createNode network -n "DescriptionInformation3";
	rename -uid "6D53BA74-4F30-BABB-664B-0E8DBD794AC3";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "zoomer";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/zoomer";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2015-04-03 15:17:13";
	setAttr -k on ".Description" -type "string" "v004";
lockNode -l 1 ;
createNode groupId -n "groupId3879";
	rename -uid "192E8714-4F43-B9FE-51DB-01B24300A813";
	setAttr ".ihi" 0;
createNode script -n "xgenGlobals2";
	rename -uid "576D56F4-4DA8-76C0-AD3C-01BFE4868848";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode script -n "xgenGlobals1";
	rename -uid "FDBAABF3-4B99-29B3-2B41-0A8DB617D7A5";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode script -n "xgenGlobals";
	rename -uid "29A171D4-4ADB-6107-02E0-F3BDC9A61A46";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode mentalrayItemsList -s -n "mentalrayItemsList";
	rename -uid "9713103A-4E22-7DB5-9C0C-27B3C8138477";
createNode mentalrayGlobals -s -n "mentalrayGlobals";
	rename -uid "4E0EAF8D-4E2A-5355-BB60-DDB44C894069";
createNode mentalrayOptions -s -n "miDefaultOptions";
	rename -uid "2065A98D-4A10-BED0-3686-66BFE6CD8D35";
	addAttr -ci true -m -sn "stringOptions" -ln "stringOptions" -at "compound" -nc 
		3;
	addAttr -ci true -sn "name" -ln "name" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "value" -ln "value" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "type" -ln "type" -dt "string" -p "stringOptions";
	setAttr -s 45 ".stringOptions";
	setAttr ".stringOptions[0].name" -type "string" "rast motion factor";
	setAttr ".stringOptions[0].value" -type "string" "1.0";
	setAttr ".stringOptions[0].type" -type "string" "scalar";
	setAttr ".stringOptions[1].name" -type "string" "rast transparency depth";
	setAttr ".stringOptions[1].value" -type "string" "8";
	setAttr ".stringOptions[1].type" -type "string" "integer";
	setAttr ".stringOptions[2].name" -type "string" "rast useopacity";
	setAttr ".stringOptions[2].value" -type "string" "true";
	setAttr ".stringOptions[2].type" -type "string" "boolean";
	setAttr ".stringOptions[3].name" -type "string" "importon";
	setAttr ".stringOptions[3].value" -type "string" "false";
	setAttr ".stringOptions[3].type" -type "string" "boolean";
	setAttr ".stringOptions[4].name" -type "string" "importon density";
	setAttr ".stringOptions[4].value" -type "string" "1.0";
	setAttr ".stringOptions[4].type" -type "string" "scalar";
	setAttr ".stringOptions[5].name" -type "string" "importon merge";
	setAttr ".stringOptions[5].value" -type "string" "0.0";
	setAttr ".stringOptions[5].type" -type "string" "scalar";
	setAttr ".stringOptions[6].name" -type "string" "importon trace depth";
	setAttr ".stringOptions[6].value" -type "string" "0";
	setAttr ".stringOptions[6].type" -type "string" "integer";
	setAttr ".stringOptions[7].name" -type "string" "importon traverse";
	setAttr ".stringOptions[7].value" -type "string" "true";
	setAttr ".stringOptions[7].type" -type "string" "boolean";
	setAttr ".stringOptions[8].name" -type "string" "shadowmap pixel samples";
	setAttr ".stringOptions[8].value" -type "string" "3";
	setAttr ".stringOptions[8].type" -type "string" "integer";
	setAttr ".stringOptions[9].name" -type "string" "ambient occlusion";
	setAttr ".stringOptions[9].value" -type "string" "false";
	setAttr ".stringOptions[9].type" -type "string" "boolean";
	setAttr ".stringOptions[10].name" -type "string" "ambient occlusion rays";
	setAttr ".stringOptions[10].value" -type "string" "256";
	setAttr ".stringOptions[10].type" -type "string" "integer";
	setAttr ".stringOptions[11].name" -type "string" "ambient occlusion cache";
	setAttr ".stringOptions[11].value" -type "string" "false";
	setAttr ".stringOptions[11].type" -type "string" "boolean";
	setAttr ".stringOptions[12].name" -type "string" "ambient occlusion cache density";
	setAttr ".stringOptions[12].value" -type "string" "1.0";
	setAttr ".stringOptions[12].type" -type "string" "scalar";
	setAttr ".stringOptions[13].name" -type "string" "ambient occlusion cache points";
	setAttr ".stringOptions[13].value" -type "string" "64";
	setAttr ".stringOptions[13].type" -type "string" "integer";
	setAttr ".stringOptions[14].name" -type "string" "irradiance particles";
	setAttr ".stringOptions[14].value" -type "string" "false";
	setAttr ".stringOptions[14].type" -type "string" "boolean";
	setAttr ".stringOptions[15].name" -type "string" "irradiance particles rays";
	setAttr ".stringOptions[15].value" -type "string" "256";
	setAttr ".stringOptions[15].type" -type "string" "integer";
	setAttr ".stringOptions[16].name" -type "string" "irradiance particles interpolate";
	setAttr ".stringOptions[16].value" -type "string" "1";
	setAttr ".stringOptions[16].type" -type "string" "integer";
	setAttr ".stringOptions[17].name" -type "string" "irradiance particles interppoints";
	setAttr ".stringOptions[17].value" -type "string" "64";
	setAttr ".stringOptions[17].type" -type "string" "integer";
	setAttr ".stringOptions[18].name" -type "string" "irradiance particles indirect passes";
	setAttr ".stringOptions[18].value" -type "string" "0";
	setAttr ".stringOptions[18].type" -type "string" "integer";
	setAttr ".stringOptions[19].name" -type "string" "irradiance particles scale";
	setAttr ".stringOptions[19].value" -type "string" "1.0";
	setAttr ".stringOptions[19].type" -type "string" "scalar";
	setAttr ".stringOptions[20].name" -type "string" "irradiance particles env";
	setAttr ".stringOptions[20].value" -type "string" "true";
	setAttr ".stringOptions[20].type" -type "string" "boolean";
	setAttr ".stringOptions[21].name" -type "string" "irradiance particles env rays";
	setAttr ".stringOptions[21].value" -type "string" "256";
	setAttr ".stringOptions[21].type" -type "string" "integer";
	setAttr ".stringOptions[22].name" -type "string" "irradiance particles env scale";
	setAttr ".stringOptions[22].value" -type "string" "1";
	setAttr ".stringOptions[22].type" -type "string" "integer";
	setAttr ".stringOptions[23].name" -type "string" "irradiance particles rebuild";
	setAttr ".stringOptions[23].value" -type "string" "true";
	setAttr ".stringOptions[23].type" -type "string" "boolean";
	setAttr ".stringOptions[24].name" -type "string" "irradiance particles file";
	setAttr ".stringOptions[24].value" -type "string" "";
	setAttr ".stringOptions[24].type" -type "string" "string";
	setAttr ".stringOptions[25].name" -type "string" "geom displace motion factor";
	setAttr ".stringOptions[25].value" -type "string" "1.0";
	setAttr ".stringOptions[25].type" -type "string" "scalar";
	setAttr ".stringOptions[26].name" -type "string" "contrast all buffers";
	setAttr ".stringOptions[26].value" -type "string" "true";
	setAttr ".stringOptions[26].type" -type "string" "boolean";
	setAttr ".stringOptions[27].name" -type "string" "finalgather normal tolerance";
	setAttr ".stringOptions[27].value" -type "string" "25.842";
	setAttr ".stringOptions[27].type" -type "string" "scalar";
	setAttr ".stringOptions[28].name" -type "string" "trace camera clip";
	setAttr ".stringOptions[28].value" -type "string" "false";
	setAttr ".stringOptions[28].type" -type "string" "boolean";
	setAttr ".stringOptions[29].name" -type "string" "unified sampling";
	setAttr ".stringOptions[29].value" -type "string" "true";
	setAttr ".stringOptions[29].type" -type "string" "boolean";
	setAttr ".stringOptions[30].name" -type "string" "samples quality";
	setAttr ".stringOptions[30].value" -type "string" "0.25 0.25 0.25 0.25";
	setAttr ".stringOptions[30].type" -type "string" "color";
	setAttr ".stringOptions[31].name" -type "string" "samples min";
	setAttr ".stringOptions[31].value" -type "string" "1.0";
	setAttr ".stringOptions[31].type" -type "string" "scalar";
	setAttr ".stringOptions[32].name" -type "string" "samples max";
	setAttr ".stringOptions[32].value" -type "string" "100.0";
	setAttr ".stringOptions[32].type" -type "string" "scalar";
	setAttr ".stringOptions[33].name" -type "string" "samples error cutoff";
	setAttr ".stringOptions[33].value" -type "string" "0.0 0.0 0.0 0.0";
	setAttr ".stringOptions[33].type" -type "string" "color";
	setAttr ".stringOptions[34].name" -type "string" "samples per object";
	setAttr ".stringOptions[34].value" -type "string" "false";
	setAttr ".stringOptions[34].type" -type "string" "boolean";
	setAttr ".stringOptions[35].name" -type "string" "progressive";
	setAttr ".stringOptions[35].value" -type "string" "false";
	setAttr ".stringOptions[35].type" -type "string" "boolean";
	setAttr ".stringOptions[36].name" -type "string" "progressive max time";
	setAttr ".stringOptions[36].value" -type "string" "0";
	setAttr ".stringOptions[36].type" -type "string" "integer";
	setAttr ".stringOptions[37].name" -type "string" "progressive subsampling size";
	setAttr ".stringOptions[37].value" -type "string" "1";
	setAttr ".stringOptions[37].type" -type "string" "integer";
	setAttr ".stringOptions[38].name" -type "string" "iray";
	setAttr ".stringOptions[38].value" -type "string" "false";
	setAttr ".stringOptions[38].type" -type "string" "boolean";
	setAttr ".stringOptions[39].name" -type "string" "light relative scale";
	setAttr ".stringOptions[39].value" -type "string" "0.31831";
	setAttr ".stringOptions[39].type" -type "string" "scalar";
	setAttr ".stringOptions[40].name" -type "string" "trace camera motion vectors";
	setAttr ".stringOptions[40].value" -type "string" "false";
	setAttr ".stringOptions[40].type" -type "string" "boolean";
	setAttr ".stringOptions[41].name" -type "string" "ray differentials";
	setAttr ".stringOptions[41].value" -type "string" "true";
	setAttr ".stringOptions[41].type" -type "string" "boolean";
	setAttr ".stringOptions[42].name" -type "string" "environment lighting mode";
	setAttr ".stringOptions[42].value" -type "string" "off";
	setAttr ".stringOptions[42].type" -type "string" "string";
	setAttr ".stringOptions[43].name" -type "string" "environment lighting quality";
	setAttr ".stringOptions[43].value" -type "string" "0.167";
	setAttr ".stringOptions[43].type" -type "string" "scalar";
	setAttr ".stringOptions[44].name" -type "string" "environment lighting shadow";
	setAttr ".stringOptions[44].value" -type "string" "transparent";
	setAttr ".stringOptions[44].type" -type "string" "string";
createNode mentalrayFramebuffer -s -n "miDefaultFramebuffer";
	rename -uid "D8CD1E50-4C92-C07E-0914-928941A891BA";
createNode network -n "DescriptionInformation5";
	rename -uid "AE6E13EF-4CA1-D288-2C1D-90BB9BD17C25";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2016-07-08 19:23:30";
	setAttr -k on ".Description" -type "string" "修改眼睛大小和眼球";
lockNode -l 1 ;
createNode network -n "DescriptionInformation9";
	rename -uid "7CB1BF42-46F4-22B7-A3AC-65AE6A9D35B5";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2016-07-08 19:23:30";
	setAttr -k on ".Description" -type "string" "修改眼睛大小和眼球";
lockNode -l 1 ;
createNode script -n "xgenGlobals7";
	rename -uid "883A856E-48EC-0867-991C-D28AC1B117BE";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode network -n "DescriptionInformation6";
	rename -uid "57553B3E-40EA-EE02-54C2-9AAACF6D781E";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "PIC-SH-116";
	setAttr -k on ".Time" -type "string" "2016-06-27 10:47:44";
	setAttr -k on ".Description" -type "string" "更新贴图";
lockNode -l 1 ;
createNode network -n "DescriptionInformation7";
	rename -uid "5E4E0CA7-4689-4AD1-F0A1-D9842E7A1F99";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "zoomer";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/zoomer";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2015-04-03 15:17:13";
	setAttr -k on ".Description" -type "string" "v004";
lockNode -l 1 ;
createNode groupId -n "groupId3905";
	rename -uid "E148412F-4C07-C2BE-20C1-1CA9AF74A901";
	setAttr ".ihi" 0;
createNode network -n "DescriptionInformation8";
	rename -uid "20FEED5C-4D7D-7C40-84EB-E8A185ACF639";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "zoomer";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/zoomer";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2015-04-03 15:17:13";
	setAttr -k on ".Description" -type "string" "v004";
lockNode -l 1 ;
createNode groupId -n "groupId3906";
	rename -uid "65ACD1D5-403E-2EE4-C557-DC9D93BE1782";
	setAttr ".ihi" 0;
createNode script -n "xgenGlobals6";
	rename -uid "5BAB1BD6-4A63-C8C0-E1B1-F88C567B219F";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode script -n "xgenGlobals5";
	rename -uid "FDB14D36-4684-6B4D-0306-4598FF99803F";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode groupId -n "groupId34";
	rename -uid "86AFBCA7-44CB-4080-F8FB-E2A1B1C8321A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId8";
	rename -uid "3A712C43-48D3-4C07-B7BE-A9AC6C1C5EA3";
	setAttr ".ihi" 0;
createNode network -n "DescriptionInformation10";
	rename -uid "C21127C6-4567-9C1E-B9F6-DA8AD970D6EF";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "BG_DOG_01";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/BG_DOG_01";
	setAttr -k on ".Author" -type "string" "PIC-SH-236";
	setAttr -k on ".Time" -type "string" "2016-05-11 10:43:45";
	setAttr -k on ".Description" -type "string" "重新上传";
lockNode -l 1 ;
createNode groupId -n "groupId83";
	rename -uid "22620F9E-4471-6B52-1850-68A156CBBA02";
	setAttr ".ihi" 0;
createNode groupId -n "groupId93";
	rename -uid "5CA099E3-4F4D-A139-AD1E-EBB5B985D64A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId124";
	rename -uid "55D2A4F8-4C7A-90CB-6142-4EB73851B719";
	setAttr ".ihi" 0;
createNode script -n "xgenGlobals8";
	rename -uid "4B7871AE-48ED-320A-ECF3-B4A78F8FADE7";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode script -n "xgenGlobals4";
	rename -uid "FD84427D-4721-500E-97A0-F1A9841BB874";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode network -n "DescriptionInformation11";
	rename -uid "25ACB41B-4D29-A554-B8DE-3AA439AFD981";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2016-07-08 19:23:30";
	setAttr -k on ".Description" -type "string" "修改眼睛大小和眼球";
lockNode -l 1 ;
createNode network -n "DescriptionInformation15";
	rename -uid "6209B10C-4A39-6356-FEB9-2FBE84EAFCF1";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2016-07-08 19:23:30";
	setAttr -k on ".Description" -type "string" "修改眼睛大小和眼球";
lockNode -l 1 ;
createNode script -n "xgenGlobals12";
	rename -uid "BABF3B64-408E-F45B-200C-69824F0946B5";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode network -n "DescriptionInformation12";
	rename -uid "086D2F6F-4DC9-5FCB-02D6-73904EAF1AEC";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "RABBIT_KIDS_02";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/RABBIT_KIDS_02";
	setAttr -k on ".Author" -type "string" "PIC-SH-116";
	setAttr -k on ".Time" -type "string" "2016-06-27 10:47:44";
	setAttr -k on ".Description" -type "string" "更新贴图";
lockNode -l 1 ;
createNode network -n "DescriptionInformation13";
	rename -uid "FCBAEBEB-4E77-8A81-6E50-44980F92BAEE";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "zoomer";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/zoomer";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2015-04-03 15:17:13";
	setAttr -k on ".Description" -type "string" "v004";
lockNode -l 1 ;
createNode groupId -n "groupId3907";
	rename -uid "DDA511BF-4B60-DA90-8FA1-7184888ACBF5";
	setAttr ".ihi" 0;
createNode network -n "DescriptionInformation14";
	rename -uid "E820D803-45AA-53BA-CA73-988305D9353D";
	addAttr -ci true -sn "Company" -ln "Company" -dt "string";
	addAttr -ci true -sn "Project" -ln "Project" -dt "string";
	addAttr -ci true -sn "ProjectPath" -ln "ProjectPath" -dt "string";
	addAttr -ci true -sn "Module" -ln "Module" -dt "string";
	addAttr -ci true -sn "SecondaryModule" -ln "SecondaryModule" -dt "string";
	addAttr -ci true -sn "Camera" -ln "Camera" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "FilePath" -ln "FilePath" -dt "string";
	addAttr -ci true -sn "Author" -ln "Author" -dt "string";
	addAttr -ci true -sn "Time" -ln "Time" -dt "string";
	addAttr -ci true -sn "Description" -ln "Description" -dt "string";
	setAttr -k on ".Company" -type "string" "MiliPictures";
	setAttr -k on ".Project" -type "string" "PPR";
	setAttr -k on ".ProjectPath" -type "string" "//hnas01/data/Projects";
	setAttr -k on ".Module" -type "string" "Model";
	setAttr -k on ".SecondaryModule" -type "string" "Characters";
	setAttr -k on ".Camera" -type "string" "None";
	setAttr -k on ".Name" -type "string" "zoomer";
	setAttr -k on ".FilePath" -type "string" "//hnas01/data/Projects/PPR/Models/Characters/zoomer";
	setAttr -k on ".Author" -type "string" "pic-p-034";
	setAttr -k on ".Time" -type "string" "2015-04-03 15:17:13";
	setAttr -k on ".Description" -type "string" "v004";
lockNode -l 1 ;
createNode groupId -n "groupId3908";
	rename -uid "76C08FAF-4B98-353A-AC93-FF8FE05689EE";
	setAttr ".ihi" 0;
createNode script -n "xgenGlobals11";
	rename -uid "1D537E77-423B-1F64-4F4C-CE8B8EF55DD8";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode script -n "xgenGlobals10";
	rename -uid "BAF791BA-44E6-E9E2-1F8A-BB94DC05F149";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode script -n "xgenGlobals9";
	rename -uid "5DC22D00-4DED-EC7D-2B93-C1980E447787";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode groupId -n "groupId3918";
	rename -uid "60C48A4B-4089-115E-5547-C28629662A01";
	setAttr ".ihi" 0;
createNode groupId -n "groupId15";
	rename -uid "38909E5D-430A-0837-8FD7-259171674161";
	setAttr ".ihi" 0;
createNode script -n "xgenGlobals13";
	rename -uid "B834C01A-4EC7-B4BF-3203-51A3D156FDB4";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode VRaySettingsNode -s -n "vraySettings";
	rename -uid "C368A215-4DCC-0064-17B0-31810011EBC5";
	setAttr ".pe" 2;
	setAttr ".se" 3;
	setAttr ".cmph" 60;
	setAttr ".cfile" -type "string" "";
	setAttr ".cfile2" -type "string" "";
	setAttr ".casf" -type "string" "";
	setAttr ".casf2" -type "string" "";
	setAttr ".st" 3;
	setAttr ".msr" 2;
	setAttr ".sd" 1000;
	setAttr ".ss" 0.01;
	setAttr ".pfts" 20;
	setAttr ".ufg" yes;
	setAttr ".fnm" -type "string" "";
	setAttr ".lcfnm" -type "string" "";
	setAttr ".asf" -type "string" "";
	setAttr ".lcasf" -type "string" "";
	setAttr ".urtrshd" yes;
	setAttr ".rtrshd" 2;
	setAttr ".ifile" -type "string" "";
	setAttr ".ifile2" -type "string" "";
	setAttr ".iasf" -type "string" "";
	setAttr ".iasf2" -type "string" "";
	setAttr ".pmfile" -type "string" "";
	setAttr ".pmfile2" -type "string" "";
	setAttr ".pmasf" -type "string" "";
	setAttr ".pmasf2" -type "string" "";
	setAttr ".dmcstd" yes;
	setAttr ".cmao" 2;
	setAttr ".cg" 2.2000000476837158;
	setAttr ".mtah" yes;
	setAttr ".srflc" 1;
	setAttr ".seu" yes;
	setAttr ".gormio" yes;
	setAttr ".wi" 960;
	setAttr ".he" 540;
	setAttr ".aspr" 1.7777780294418335;
	setAttr ".jpegq" 100;
	setAttr ".vfbOn" yes;
	setAttr ".mSceneName" -type "string" "D:/data/scripts/facial_ctrl.ma";
createNode nodeGraphEditorBookmarkInfo -n "nodeGraphEditorBookmarkInfo1";
	rename -uid "5522B128-420A-7F6B-6CF6-2C9005A6670F";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "B3CB525C-42A3-B474-0F47-9BB74501524A";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -455.95236283446195 -471.42855269568389 ;
	setAttr ".tgi[0].vh" -type "double2" 435.71426840055625 492.85712327276042 ;
select -ne :time1;
	setAttr ".o" 30;
	setAttr ".unw" 30;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 18 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surfaces" "Particles" "Fluids" "Image Planes" "UI:" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 18 0 1 1 1 1 1
		 1 0 0 0 0 0 0 0 0 0 0 0 ;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
	setAttr -s 13 ".gn";
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "facial__Ctrl.Face_C" "Eye_Aim_Grp.v";
connectAttr "facial__Ctrl.Face_C" "C_Jaw_Grp.v" -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_parentConstraint1.ctx" "Mouth_Stick_Ctrl_Gro.tx"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_parentConstraint1.cty" "Mouth_Stick_Ctrl_Gro.ty"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_parentConstraint1.ctz" "Mouth_Stick_Ctrl_Gro.tz"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_parentConstraint1.crx" "Mouth_Stick_Ctrl_Gro.rx"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_parentConstraint1.cry" "Mouth_Stick_Ctrl_Gro.ry"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_parentConstraint1.crz" "Mouth_Stick_Ctrl_Gro.rz"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_scaleConstraint1.csx" "Mouth_Stick_Ctrl_Gro.sx"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_scaleConstraint1.csy" "Mouth_Stick_Ctrl_Gro.sy"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro_scaleConstraint1.csz" "Mouth_Stick_Ctrl_Gro.sz"
		 -l on;
connectAttr "Mouth_Stick_Ctrl_Gro.ro" "Mouth_Stick_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "Mouth_Stick_Ctrl_Gro.pim" "Mouth_Stick_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "Mouth_Stick_Ctrl_Gro.rp" "Mouth_Stick_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "Mouth_Stick_Ctrl_Gro.rpt" "Mouth_Stick_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "Mouth_Stick_loc.t" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "Mouth_Stick_loc.rp" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "Mouth_Stick_loc.rpt" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "Mouth_Stick_loc.r" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "Mouth_Stick_loc.ro" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "Mouth_Stick_loc.s" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "Mouth_Stick_loc.pm" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "Mouth_Stick_Ctrl_Gro_parentConstraint1.w0" "Mouth_Stick_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "Mouth_Stick_Ctrl_Gro.pim" "Mouth_Stick_Ctrl_Gro_scaleConstraint1.cpim"
		;
connectAttr "Mouth_Stick_loc.s" "Mouth_Stick_Ctrl_Gro_scaleConstraint1.tg[0].ts"
		;
connectAttr "Mouth_Stick_loc.pm" "Mouth_Stick_Ctrl_Gro_scaleConstraint1.tg[0].tpm"
		;
connectAttr "Mouth_Stick_Ctrl_Gro_scaleConstraint1.w0" "Mouth_Stick_Ctrl_Gro_scaleConstraint1.tg[0].tw"
		;
connectAttr "Lips_out_Stick_Ctrl_Gro_parentConstraint1.ctx" "Lips_out_Stick_Ctrl_Gro.tx"
		 -l on;
connectAttr "Lips_out_Stick_Ctrl_Gro_parentConstraint1.cty" "Lips_out_Stick_Ctrl_Gro.ty"
		 -l on;
connectAttr "Lips_out_Stick_Ctrl_Gro_parentConstraint1.ctz" "Lips_out_Stick_Ctrl_Gro.tz"
		 -l on;
connectAttr "Lips_out_Stick_Ctrl_Gro_parentConstraint1.crx" "Lips_out_Stick_Ctrl_Gro.rx"
		 -l on;
connectAttr "Lips_out_Stick_Ctrl_Gro_parentConstraint1.cry" "Lips_out_Stick_Ctrl_Gro.ry"
		 -l on;
connectAttr "Lips_out_Stick_Ctrl_Gro_parentConstraint1.crz" "Lips_out_Stick_Ctrl_Gro.rz"
		 -l on;
connectAttr "Lips_out_Stick_Ctrl_Gro.ro" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "Lips_out_Stick_Ctrl_Gro.pim" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "Lips_out_Stick_Ctrl_Gro.rp" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "Lips_out_Stick_Ctrl_Gro.rpt" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "Jaw_Ctrl.t" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "Jaw_Ctrl.rp" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "Jaw_Ctrl.rpt" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "Jaw_Ctrl.r" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "Jaw_Ctrl.ro" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "Jaw_Ctrl.s" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "Jaw_Ctrl.pm" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "Lips_out_Stick_Ctrl_Gro_parentConstraint1.w0" "Lips_out_Stick_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "facial__Ctrl.Face_C" "C_Noce_Grp.v" -l on;
connectAttr "C_Noce_bridge_Ctrl.t" "C_Noce_Main_Ctrl_G.t";
connectAttr "C_Noce_bridge_Ctrl.r" "C_Noce_Main_Ctrl_G.r";
connectAttr "facial__Ctrl.Face_C" "C_Mouth_Grp.v" -l on;
connectAttr "U_Mouth_Ctrl_Gro_parentConstraint1.ctx" "U_Mouth_Ctrl_Gro.tx" -l on
		;
connectAttr "U_Mouth_Ctrl_Gro_parentConstraint1.cty" "U_Mouth_Ctrl_Gro.ty" -l on
		;
connectAttr "U_Mouth_Ctrl_Gro_parentConstraint1.ctz" "U_Mouth_Ctrl_Gro.tz" -l on
		;
connectAttr "U_Mouth_Ctrl_Gro_parentConstraint1.crx" "U_Mouth_Ctrl_Gro.rx" -l on
		;
connectAttr "U_Mouth_Ctrl_Gro_parentConstraint1.cry" "U_Mouth_Ctrl_Gro.ry" -l on
		;
connectAttr "U_Mouth_Ctrl_Gro_parentConstraint1.crz" "U_Mouth_Ctrl_Gro.rz" -l on
		;
connectAttr "U_Mouth_Ctrl_Gro.ro" "U_Mouth_Ctrl_Gro_parentConstraint1.cro";
connectAttr "U_Mouth_Ctrl_Gro.pim" "U_Mouth_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "U_Mouth_Ctrl_Gro.rp" "U_Mouth_Ctrl_Gro_parentConstraint1.crp";
connectAttr "U_Mouth_Ctrl_Gro.rpt" "U_Mouth_Ctrl_Gro_parentConstraint1.crt";
connectAttr "U_Mouth_loc.t" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "U_Mouth_loc.rp" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "U_Mouth_loc.rpt" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "U_Mouth_loc.r" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "U_Mouth_loc.ro" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "U_Mouth_loc.s" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "U_Mouth_loc.pm" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "U_Mouth_Ctrl_Gro_parentConstraint1.w0" "U_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "D_Mouth_Ctrl_Gro_parentConstraint1.ctx" "D_Mouth_Ctrl_Gro.tx" -l on
		;
connectAttr "D_Mouth_Ctrl_Gro_parentConstraint1.cty" "D_Mouth_Ctrl_Gro.ty" -l on
		;
connectAttr "D_Mouth_Ctrl_Gro_parentConstraint1.ctz" "D_Mouth_Ctrl_Gro.tz" -l on
		;
connectAttr "D_Mouth_Ctrl_Gro_parentConstraint1.crx" "D_Mouth_Ctrl_Gro.rx" -l on
		;
connectAttr "D_Mouth_Ctrl_Gro_parentConstraint1.cry" "D_Mouth_Ctrl_Gro.ry" -l on
		;
connectAttr "D_Mouth_Ctrl_Gro_parentConstraint1.crz" "D_Mouth_Ctrl_Gro.rz" -l on
		;
connectAttr "D_Mouth_Ctrl_Gro.ro" "D_Mouth_Ctrl_Gro_parentConstraint1.cro";
connectAttr "D_Mouth_Ctrl_Gro.pim" "D_Mouth_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "D_Mouth_Ctrl_Gro.rp" "D_Mouth_Ctrl_Gro_parentConstraint1.crp";
connectAttr "D_Mouth_Ctrl_Gro.rpt" "D_Mouth_Ctrl_Gro_parentConstraint1.crt";
connectAttr "D_Mouth_loc.t" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "D_Mouth_loc.rp" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "D_Mouth_loc.rpt" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "D_Mouth_loc.r" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "D_Mouth_loc.ro" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "D_Mouth_loc.s" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "D_Mouth_loc.pm" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "D_Mouth_Ctrl_Gro_parentConstraint1.w0" "D_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_Mouth_Ctrl_Gro_parentConstraint1.ctx" "L_Mouth_Ctrl_Gro.tx" -l on
		;
connectAttr "L_Mouth_Ctrl_Gro_parentConstraint1.cty" "L_Mouth_Ctrl_Gro.ty" -l on
		;
connectAttr "L_Mouth_Ctrl_Gro_parentConstraint1.ctz" "L_Mouth_Ctrl_Gro.tz" -l on
		;
connectAttr "L_Mouth_Ctrl_Gro_parentConstraint1.crx" "L_Mouth_Ctrl_Gro.rx" -l on
		;
connectAttr "L_Mouth_Ctrl_Gro_parentConstraint1.cry" "L_Mouth_Ctrl_Gro.ry" -l on
		;
connectAttr "L_Mouth_Ctrl_Gro_parentConstraint1.crz" "L_Mouth_Ctrl_Gro.rz" -l on
		;
connectAttr "L_Mouth_Ctrl_Gro.ro" "L_Mouth_Ctrl_Gro_parentConstraint1.cro";
connectAttr "L_Mouth_Ctrl_Gro.pim" "L_Mouth_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "L_Mouth_Ctrl_Gro.rp" "L_Mouth_Ctrl_Gro_parentConstraint1.crp";
connectAttr "L_Mouth_Ctrl_Gro.rpt" "L_Mouth_Ctrl_Gro_parentConstraint1.crt";
connectAttr "L_Mouth_loc.t" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_Mouth_loc.rp" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "L_Mouth_loc.rpt" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "L_Mouth_loc.r" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_Mouth_loc.ro" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "L_Mouth_loc.s" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_Mouth_loc.pm" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "L_Mouth_Ctrl_Gro_parentConstraint1.w0" "L_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_Mouth_Ctrl_Gro_parentConstraint1.ctx" "R_Mouth_Ctrl_Gro.tx" -l on
		;
connectAttr "R_Mouth_Ctrl_Gro_parentConstraint1.cty" "R_Mouth_Ctrl_Gro.ty" -l on
		;
connectAttr "R_Mouth_Ctrl_Gro_parentConstraint1.ctz" "R_Mouth_Ctrl_Gro.tz" -l on
		;
connectAttr "R_Mouth_Ctrl_Gro_parentConstraint1.crx" "R_Mouth_Ctrl_Gro.rx" -l on
		;
connectAttr "R_Mouth_Ctrl_Gro_parentConstraint1.cry" "R_Mouth_Ctrl_Gro.ry" -l on
		;
connectAttr "R_Mouth_Ctrl_Gro_parentConstraint1.crz" "R_Mouth_Ctrl_Gro.rz" -l on
		;
connectAttr "R_Mouth_Ctrl_Gro.ro" "R_Mouth_Ctrl_Gro_parentConstraint1.cro";
connectAttr "R_Mouth_Ctrl_Gro.pim" "R_Mouth_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "R_Mouth_Ctrl_Gro.rp" "R_Mouth_Ctrl_Gro_parentConstraint1.crp";
connectAttr "R_Mouth_Ctrl_Gro.rpt" "R_Mouth_Ctrl_Gro_parentConstraint1.crt";
connectAttr "R_Mouth_loc.t" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_Mouth_loc.rp" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "R_Mouth_loc.rpt" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "R_Mouth_loc.r" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_Mouth_loc.ro" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "R_Mouth_loc.s" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_Mouth_loc.pm" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "R_Mouth_Ctrl_Gro_parentConstraint1.w0" "R_Mouth_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Upperlip_Ctrl_Gro_parentConstraint1.ctx" "C_Upperlip_Ctrl_Gro.tx"
		 -l on;
connectAttr "C_Upperlip_Ctrl_Gro_parentConstraint1.cty" "C_Upperlip_Ctrl_Gro.ty"
		 -l on;
connectAttr "C_Upperlip_Ctrl_Gro_parentConstraint1.ctz" "C_Upperlip_Ctrl_Gro.tz"
		 -l on;
connectAttr "C_Upperlip_Ctrl_Gro_parentConstraint1.crx" "C_Upperlip_Ctrl_Gro.rx"
		 -l on;
connectAttr "C_Upperlip_Ctrl_Gro_parentConstraint1.cry" "C_Upperlip_Ctrl_Gro.ry"
		 -l on;
connectAttr "C_Upperlip_Ctrl_Gro_parentConstraint1.crz" "C_Upperlip_Ctrl_Gro.rz"
		 -l on;
connectAttr "C_Upperlip_Ctrl_Gro.ro" "C_Upperlip_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Upperlip_Ctrl_Gro.pim" "C_Upperlip_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Upperlip_Ctrl_Gro.rp" "C_Upperlip_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Upperlip_Ctrl_Gro.rpt" "C_Upperlip_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Upperlip_loc.t" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "C_Upperlip_loc.rp" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Upperlip_loc.rpt" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Upperlip_loc.r" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "C_Upperlip_loc.ro" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Upperlip_loc.s" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "C_Upperlip_loc.pm" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Upperlip_Ctrl_Gro_parentConstraint1.w0" "C_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Lowerlip_Ctrl_Gro_parentConstraint1.ctx" "C_Lowerlip_Ctrl_Gro.tx"
		 -l on;
connectAttr "C_Lowerlip_Ctrl_Gro_parentConstraint1.cty" "C_Lowerlip_Ctrl_Gro.ty"
		 -l on;
connectAttr "C_Lowerlip_Ctrl_Gro_parentConstraint1.ctz" "C_Lowerlip_Ctrl_Gro.tz"
		 -l on;
connectAttr "C_Lowerlip_Ctrl_Gro_parentConstraint1.crx" "C_Lowerlip_Ctrl_Gro.rx"
		 -l on;
connectAttr "C_Lowerlip_Ctrl_Gro_parentConstraint1.cry" "C_Lowerlip_Ctrl_Gro.ry"
		 -l on;
connectAttr "C_Lowerlip_Ctrl_Gro_parentConstraint1.crz" "C_Lowerlip_Ctrl_Gro.rz"
		 -l on;
connectAttr "C_Lowerlip_Ctrl_Gro.ro" "C_Lowerlip_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Lowerlip_Ctrl_Gro.pim" "C_Lowerlip_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Lowerlip_Ctrl_Gro.rp" "C_Lowerlip_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Lowerlip_Ctrl_Gro.rpt" "C_Lowerlip_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Lowerlip_loc.t" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "C_Lowerlip_loc.rp" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Lowerlip_loc.rpt" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Lowerlip_loc.r" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "C_Lowerlip_loc.ro" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Lowerlip_loc.s" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "C_Lowerlip_loc.pm" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Lowerlip_Ctrl_Gro_parentConstraint1.w0" "C_Lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_Upperlip_Ctrl_Gro_parentConstraint1.ctx" "L_Upperlip_Ctrl_Gro.tx"
		 -l on;
connectAttr "L_Upperlip_Ctrl_Gro_parentConstraint1.cty" "L_Upperlip_Ctrl_Gro.ty"
		 -l on;
connectAttr "L_Upperlip_Ctrl_Gro_parentConstraint1.ctz" "L_Upperlip_Ctrl_Gro.tz"
		 -l on;
connectAttr "L_Upperlip_Ctrl_Gro_parentConstraint1.crx" "L_Upperlip_Ctrl_Gro.rx"
		 -l on;
connectAttr "L_Upperlip_Ctrl_Gro_parentConstraint1.cry" "L_Upperlip_Ctrl_Gro.ry"
		 -l on;
connectAttr "L_Upperlip_Ctrl_Gro_parentConstraint1.crz" "L_Upperlip_Ctrl_Gro.rz"
		 -l on;
connectAttr "L_Upperlip_Ctrl_Gro.ro" "L_Upperlip_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "L_Upperlip_Ctrl_Gro.pim" "L_Upperlip_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "L_Upperlip_Ctrl_Gro.rp" "L_Upperlip_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "L_Upperlip_Ctrl_Gro.rpt" "L_Upperlip_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "L_Upperlip_loc.t" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_Upperlip_loc.rp" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "L_Upperlip_loc.rpt" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "L_Upperlip_loc.r" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_Upperlip_loc.ro" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "L_Upperlip_loc.s" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_Upperlip_loc.pm" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "L_Upperlip_Ctrl_Gro_parentConstraint1.w0" "L_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_Upperlip_Ctrl_Gro_parentConstraint1.ctx" "R_Upperlip_Ctrl_Gro.tx"
		 -l on;
connectAttr "R_Upperlip_Ctrl_Gro_parentConstraint1.cty" "R_Upperlip_Ctrl_Gro.ty"
		 -l on;
connectAttr "R_Upperlip_Ctrl_Gro_parentConstraint1.ctz" "R_Upperlip_Ctrl_Gro.tz"
		 -l on;
connectAttr "R_Upperlip_Ctrl_Gro_parentConstraint1.crx" "R_Upperlip_Ctrl_Gro.rx"
		 -l on;
connectAttr "R_Upperlip_Ctrl_Gro_parentConstraint1.cry" "R_Upperlip_Ctrl_Gro.ry"
		 -l on;
connectAttr "R_Upperlip_Ctrl_Gro_parentConstraint1.crz" "R_Upperlip_Ctrl_Gro.rz"
		 -l on;
connectAttr "R_Upperlip_Ctrl_Gro.ro" "R_Upperlip_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "R_Upperlip_Ctrl_Gro.pim" "R_Upperlip_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "R_Upperlip_Ctrl_Gro.rp" "R_Upperlip_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "R_Upperlip_Ctrl_Gro.rpt" "R_Upperlip_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "R_Upperlip_loc.t" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_Upperlip_loc.rp" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "R_Upperlip_loc.rpt" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "R_Upperlip_loc.r" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_Upperlip_loc.ro" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "R_Upperlip_loc.s" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_Upperlip_loc.pm" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "R_Upperlip_Ctrl_Gro_parentConstraint1.w0" "R_Upperlip_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_lowerlip_Ctrl_Gro_parentConstraint1.ctx" "L_lowerlip_Ctrl_Gro.tx"
		 -l on;
connectAttr "L_lowerlip_Ctrl_Gro_parentConstraint1.cty" "L_lowerlip_Ctrl_Gro.ty"
		 -l on;
connectAttr "L_lowerlip_Ctrl_Gro_parentConstraint1.ctz" "L_lowerlip_Ctrl_Gro.tz"
		 -l on;
connectAttr "L_lowerlip_Ctrl_Gro_parentConstraint1.crx" "L_lowerlip_Ctrl_Gro.rx"
		 -l on;
connectAttr "L_lowerlip_Ctrl_Gro_parentConstraint1.cry" "L_lowerlip_Ctrl_Gro.ry"
		 -l on;
connectAttr "L_lowerlip_Ctrl_Gro_parentConstraint1.crz" "L_lowerlip_Ctrl_Gro.rz"
		 -l on;
connectAttr "L_lowerlip_Ctrl_Gro.ro" "L_lowerlip_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "L_lowerlip_Ctrl_Gro.pim" "L_lowerlip_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "L_lowerlip_Ctrl_Gro.rp" "L_lowerlip_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "L_lowerlip_Ctrl_Gro.rpt" "L_lowerlip_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "L_lowerlip_loc.t" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_lowerlip_loc.rp" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "L_lowerlip_loc.rpt" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "L_lowerlip_loc.r" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_lowerlip_loc.ro" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "L_lowerlip_loc.s" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_lowerlip_loc.pm" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "L_lowerlip_Ctrl_Gro_parentConstraint1.w0" "L_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_lowerlip_Ctrl_Gro_parentConstraint1.ctx" "R_lowerlip_Ctrl_Gro.tx"
		 -l on;
connectAttr "R_lowerlip_Ctrl_Gro_parentConstraint1.cty" "R_lowerlip_Ctrl_Gro.ty"
		 -l on;
connectAttr "R_lowerlip_Ctrl_Gro_parentConstraint1.ctz" "R_lowerlip_Ctrl_Gro.tz"
		 -l on;
connectAttr "R_lowerlip_Ctrl_Gro_parentConstraint1.crx" "R_lowerlip_Ctrl_Gro.rx"
		 -l on;
connectAttr "R_lowerlip_Ctrl_Gro_parentConstraint1.cry" "R_lowerlip_Ctrl_Gro.ry"
		 -l on;
connectAttr "R_lowerlip_Ctrl_Gro_parentConstraint1.crz" "R_lowerlip_Ctrl_Gro.rz"
		 -l on;
connectAttr "R_lowerlip_Ctrl_Gro.ro" "R_lowerlip_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "R_lowerlip_Ctrl_Gro.pim" "R_lowerlip_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "R_lowerlip_Ctrl_Gro.rp" "R_lowerlip_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "R_lowerlip_Ctrl_Gro.rpt" "R_lowerlip_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "R_lowerlip_loc.t" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_lowerlip_loc.rp" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "R_lowerlip_loc.rpt" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "R_lowerlip_loc.r" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_lowerlip_loc.ro" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "R_lowerlip_loc.s" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_lowerlip_loc.pm" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "R_lowerlip_Ctrl_Gro_parentConstraint1.w0" "R_lowerlip_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "facial__Ctrl.Face_C" "C_Tongue_Grp.v" -l on;
connectAttr "C_Tongue_01_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_01_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_01_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_01_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_01_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_01_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_01_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_01_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_01_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_01_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_01_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_01_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_01_Ctrl_Gro.ro" "C_Tongue_01_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_01_Ctrl_Gro.pim" "C_Tongue_01_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_01_Ctrl_Gro.rp" "C_Tongue_01_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_01_Ctrl_Gro.rpt" "C_Tongue_01_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_01_loc.t" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_01_loc.rp" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_01_loc.rpt" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_01_loc.r" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_01_loc.ro" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_01_loc.s" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_01_loc.pm" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_01_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_01_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_02_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_02_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_02_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_02_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_02_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_02_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_02_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_02_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_02_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_02_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_02_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_02_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_02_Ctrl_Gro.ro" "C_Tongue_02_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_02_Ctrl_Gro.pim" "C_Tongue_02_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_02_Ctrl_Gro.rp" "C_Tongue_02_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_02_Ctrl_Gro.rpt" "C_Tongue_02_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_02_loc.t" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_02_loc.rp" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_02_loc.rpt" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_02_loc.r" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_02_loc.ro" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_02_loc.s" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_02_loc.pm" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_02_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_02_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_03_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_03_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_03_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_03_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_03_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_03_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_03_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_03_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_03_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_03_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_03_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_03_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_03_Ctrl_Gro.ro" "C_Tongue_03_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_03_Ctrl_Gro.pim" "C_Tongue_03_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_03_Ctrl_Gro.rp" "C_Tongue_03_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_03_Ctrl_Gro.rpt" "C_Tongue_03_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_03_loc.t" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_03_loc.rp" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_03_loc.rpt" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_03_loc.r" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_03_loc.ro" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_03_loc.s" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_03_loc.pm" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_03_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_03_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_04_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_04_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_04_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_04_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_04_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_04_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_04_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_04_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_04_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_04_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_04_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_04_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_04_Ctrl_Gro.ro" "C_Tongue_04_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_04_Ctrl_Gro.pim" "C_Tongue_04_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_04_Ctrl_Gro.rp" "C_Tongue_04_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_04_Ctrl_Gro.rpt" "C_Tongue_04_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_04_loc.t" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_04_loc.rp" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_04_loc.rpt" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_04_loc.r" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_04_loc.ro" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_04_loc.s" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_04_loc.pm" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_04_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_04_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_05_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_05_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_05_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_05_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_05_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_05_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_05_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_05_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_05_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_05_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_05_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_05_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_05_Ctrl_Gro.ro" "C_Tongue_05_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_05_Ctrl_Gro.pim" "C_Tongue_05_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_05_Ctrl_Gro.rp" "C_Tongue_05_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_05_Ctrl_Gro.rpt" "C_Tongue_05_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_05_loc.t" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_05_loc.rp" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_05_loc.rpt" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_05_loc.r" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_05_loc.ro" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_05_loc.s" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_05_loc.pm" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_05_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_05_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_06_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_06_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_06_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_06_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_06_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_06_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_06_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_06_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_06_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_06_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_06_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_06_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_06_Ctrl_Gro.ro" "C_Tongue_06_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_06_Ctrl_Gro.pim" "C_Tongue_06_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_06_Ctrl_Gro.rp" "C_Tongue_06_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_06_Ctrl_Gro.rpt" "C_Tongue_06_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_06_loc.t" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_06_loc.rp" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_06_loc.rpt" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_06_loc.r" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_06_loc.ro" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_06_loc.s" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_06_loc.pm" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_06_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_06_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_Main_02_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_Main_02_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_Main_02_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_Main_02_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_Main_02_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_Main_02_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro.ro" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro.pim" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro.rp" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro.rpt" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_01_loc.t" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_01_loc.rp" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_01_loc.rpt" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_01_loc.r" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_01_loc.ro" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_01_loc.s" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_01_loc.pm" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_Main_02_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_Main_03_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_Main_03_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_Main_03_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_Main_03_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_Main_03_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_Main_03_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro.ro" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro.pim" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro.rp" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro.rpt" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_02_loc.t" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_02_loc.rp" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_02_loc.rpt" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_02_loc.r" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_02_loc.ro" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_02_loc.s" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_02_loc.pm" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_Main_03_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_Main_04_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_Main_04_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_Main_04_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_Main_04_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_Main_04_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_Main_04_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro.ro" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro.pim" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro.rp" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro.rpt" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_03_loc.t" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_03_loc.rp" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_03_loc.rpt" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_03_loc.r" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_03_loc.ro" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_03_loc.s" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_03_loc.pm" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_Main_04_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_Main_05_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_Main_05_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_Main_05_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_Main_05_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_Main_05_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_Main_05_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro.ro" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro.pim" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro.rp" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro.rpt" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_04_loc.t" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_04_loc.rp" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_04_loc.rpt" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_04_loc.r" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_04_loc.ro" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_04_loc.s" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_04_loc.pm" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_Main_05_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.ctx" "C_Tongue_Main_06_Ctrl_Gro.tx"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.cty" "C_Tongue_Main_06_Ctrl_Gro.ty"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.ctz" "C_Tongue_Main_06_Ctrl_Gro.tz"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.crx" "C_Tongue_Main_06_Ctrl_Gro.rx"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.cry" "C_Tongue_Main_06_Ctrl_Gro.ry"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.crz" "C_Tongue_Main_06_Ctrl_Gro.rz"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro.ro" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro.pim" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro.rp" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro.rpt" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "C_Tongue_05_loc.t" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "C_Tongue_05_loc.rp" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "C_Tongue_05_loc.rpt" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "C_Tongue_05_loc.r" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "C_Tongue_05_loc.ro" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "C_Tongue_05_loc.s" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "C_Tongue_05_loc.pm" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.w0" "C_Tongue_Main_06_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "facial__Ctrl.Face_C" "L_Brow_Grp.v" -l on;
connectAttr "facial__Ctrl.Face_C" "R_Brow_Grp.v" -l on;
connectAttr "facial__Ctrl.Face_C" "L_Eye_Grp.v" -l on;
connectAttr "L_BLid_Ctrl_Gro_parentConstraint1.ctx" "L_BLid_Ctrl_Gro.tx" -l on;
connectAttr "L_BLid_Ctrl_Gro_parentConstraint1.cty" "L_BLid_Ctrl_Gro.ty" -l on;
connectAttr "L_BLid_Ctrl_Gro_parentConstraint1.ctz" "L_BLid_Ctrl_Gro.tz" -l on;
connectAttr "L_BLid_Ctrl_Gro_parentConstraint1.crx" "L_BLid_Ctrl_Gro.rx" -l on;
connectAttr "L_BLid_Ctrl_Gro_parentConstraint1.cry" "L_BLid_Ctrl_Gro.ry" -l on;
connectAttr "L_BLid_Ctrl_Gro_parentConstraint1.crz" "L_BLid_Ctrl_Gro.rz" -l on;
connectAttr "L_BLid_Ctrl_Gro.ro" "L_BLid_Ctrl_Gro_parentConstraint1.cro";
connectAttr "L_BLid_Ctrl_Gro.pim" "L_BLid_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "L_BLid_Ctrl_Gro.rp" "L_BLid_Ctrl_Gro_parentConstraint1.crp";
connectAttr "L_BLid_Ctrl_Gro.rpt" "L_BLid_Ctrl_Gro_parentConstraint1.crt";
connectAttr "L_BLid_loc.t" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_BLid_loc.rp" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "L_BLid_loc.rpt" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "L_BLid_loc.r" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_BLid_loc.ro" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "L_BLid_loc.s" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_BLid_loc.pm" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "L_BLid_Ctrl_Gro_parentConstraint1.w0" "L_BLid_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_TLid_Ctrl_Gro_parentConstraint1.ctx" "L_TLid_Ctrl_Gro.tx" -l on;
connectAttr "L_TLid_Ctrl_Gro_parentConstraint1.cty" "L_TLid_Ctrl_Gro.ty" -l on;
connectAttr "L_TLid_Ctrl_Gro_parentConstraint1.ctz" "L_TLid_Ctrl_Gro.tz" -l on;
connectAttr "L_TLid_Ctrl_Gro_parentConstraint1.crx" "L_TLid_Ctrl_Gro.rx" -l on;
connectAttr "L_TLid_Ctrl_Gro_parentConstraint1.cry" "L_TLid_Ctrl_Gro.ry" -l on;
connectAttr "L_TLid_Ctrl_Gro_parentConstraint1.crz" "L_TLid_Ctrl_Gro.rz" -l on;
connectAttr "L_TLid_Ctrl_Gro.ro" "L_TLid_Ctrl_Gro_parentConstraint1.cro";
connectAttr "L_TLid_Ctrl_Gro.pim" "L_TLid_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "L_TLid_Ctrl_Gro.rp" "L_TLid_Ctrl_Gro_parentConstraint1.crp";
connectAttr "L_TLid_Ctrl_Gro.rpt" "L_TLid_Ctrl_Gro_parentConstraint1.crt";
connectAttr "L_TLid_loc.t" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_TLid_loc.rp" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "L_TLid_loc.rpt" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "L_TLid_loc.r" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_TLid_loc.ro" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "L_TLid_loc.s" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_TLid_loc.pm" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "L_TLid_Ctrl_Gro_parentConstraint1.w0" "L_TLid_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_Eyeball_Ctrl_Gro_parentConstraint1.ctz" "L_Eyeball_Ctrl_Gro.tz" -l
		 on;
connectAttr "L_Eyeball_Ctrl_Gro_parentConstraint1.ctx" "L_Eyeball_Ctrl_Gro.tx" -l
		 on;
connectAttr "L_Eyeball_Ctrl_Gro_parentConstraint1.cty" "L_Eyeball_Ctrl_Gro.ty" -l
		 on;
connectAttr "L_Eyeball_Ctrl_Gro_parentConstraint1.crx" "L_Eyeball_Ctrl_Gro.rx" -l
		 on;
connectAttr "L_Eyeball_Ctrl_Gro_parentConstraint1.cry" "L_Eyeball_Ctrl_Gro.ry" -l
		 on;
connectAttr "L_Eyeball_Ctrl_Gro_parentConstraint1.crz" "L_Eyeball_Ctrl_Gro.rz" -l
		 on;
connectAttr "L_Eyeball_Ctrl_Gro.ro" "L_Eyeball_Ctrl_Gro_parentConstraint1.cro";
connectAttr "L_Eyeball_Ctrl_Gro.pim" "L_Eyeball_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "L_Eyeball_Ctrl_Gro.rp" "L_Eyeball_Ctrl_Gro_parentConstraint1.crp";
connectAttr "L_Eyeball_Ctrl_Gro.rpt" "L_Eyeball_Ctrl_Gro_parentConstraint1.crt";
connectAttr "L_Pupil_loc.t" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_Pupil_loc.rp" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "L_Pupil_loc.rpt" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "L_Pupil_loc.r" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_Pupil_loc.ro" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "L_Pupil_loc.s" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_Pupil_loc.pm" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "L_Eyeball_Ctrl_Gro_parentConstraint1.w0" "L_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_UppOrb_Ctrl_Gro_parentConstraint1.ctx" "L_UppOrb_Ctrl_Gro.tx" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_parentConstraint1.cty" "L_UppOrb_Ctrl_Gro.ty" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_parentConstraint1.ctz" "L_UppOrb_Ctrl_Gro.tz" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_parentConstraint1.crx" "L_UppOrb_Ctrl_Gro.rx" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_parentConstraint1.cry" "L_UppOrb_Ctrl_Gro.ry" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_parentConstraint1.crz" "L_UppOrb_Ctrl_Gro.rz" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_scaleConstraint1.csx" "L_UppOrb_Ctrl_Gro.sx" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_scaleConstraint1.csy" "L_UppOrb_Ctrl_Gro.sy" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro_scaleConstraint1.csz" "L_UppOrb_Ctrl_Gro.sz" -l on
		;
connectAttr "L_UppOrb_Ctrl_Gro.pim" "L_UppOrb_Ctrl_Gro_scaleConstraint1.cpim";
connectAttr "L_UppOrb_loc.s" "L_UppOrb_Ctrl_Gro_scaleConstraint1.tg[0].ts";
connectAttr "L_UppOrb_loc.pm" "L_UppOrb_Ctrl_Gro_scaleConstraint1.tg[0].tpm";
connectAttr "L_UppOrb_Ctrl_Gro_scaleConstraint1.w0" "L_UppOrb_Ctrl_Gro_scaleConstraint1.tg[0].tw"
		;
connectAttr "L_UppOrb_Ctrl_Gro.ro" "L_UppOrb_Ctrl_Gro_parentConstraint1.cro";
connectAttr "L_UppOrb_Ctrl_Gro.pim" "L_UppOrb_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "L_UppOrb_Ctrl_Gro.rp" "L_UppOrb_Ctrl_Gro_parentConstraint1.crp";
connectAttr "L_UppOrb_Ctrl_Gro.rpt" "L_UppOrb_Ctrl_Gro_parentConstraint1.crt";
connectAttr "L_UppOrb_loc.t" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_UppOrb_loc.rp" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "L_UppOrb_loc.rpt" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "L_UppOrb_loc.r" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_UppOrb_loc.ro" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "L_UppOrb_loc.s" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_UppOrb_loc.pm" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "L_UppOrb_Ctrl_Gro_parentConstraint1.w0" "L_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_lowOrb_Ctrl_Gro_parentConstraint1.ctx" "L_lowOrb_Ctrl_Gro.tx" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_parentConstraint1.cty" "L_lowOrb_Ctrl_Gro.ty" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_parentConstraint1.ctz" "L_lowOrb_Ctrl_Gro.tz" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_parentConstraint1.crx" "L_lowOrb_Ctrl_Gro.rx" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_parentConstraint1.cry" "L_lowOrb_Ctrl_Gro.ry" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_parentConstraint1.crz" "L_lowOrb_Ctrl_Gro.rz" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_scaleConstraint1.csx" "L_lowOrb_Ctrl_Gro.sx" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_scaleConstraint1.csy" "L_lowOrb_Ctrl_Gro.sy" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro_scaleConstraint1.csz" "L_lowOrb_Ctrl_Gro.sz" -l on
		;
connectAttr "L_lowOrb_Ctrl_Gro.pim" "L_lowOrb_Ctrl_Gro_scaleConstraint1.cpim";
connectAttr "L_lowOrb_loc.s" "L_lowOrb_Ctrl_Gro_scaleConstraint1.tg[0].ts";
connectAttr "L_lowOrb_loc.pm" "L_lowOrb_Ctrl_Gro_scaleConstraint1.tg[0].tpm";
connectAttr "L_lowOrb_Ctrl_Gro_scaleConstraint1.w0" "L_lowOrb_Ctrl_Gro_scaleConstraint1.tg[0].tw"
		;
connectAttr "L_lowOrb_Ctrl_Gro.ro" "L_lowOrb_Ctrl_Gro_parentConstraint1.cro";
connectAttr "L_lowOrb_Ctrl_Gro.pim" "L_lowOrb_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "L_lowOrb_Ctrl_Gro.rp" "L_lowOrb_Ctrl_Gro_parentConstraint1.crp";
connectAttr "L_lowOrb_Ctrl_Gro.rpt" "L_lowOrb_Ctrl_Gro_parentConstraint1.crt";
connectAttr "L_lowOrb_loc.t" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "L_lowOrb_loc.rp" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "L_lowOrb_loc.rpt" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "L_lowOrb_loc.r" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "L_lowOrb_loc.ro" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "L_lowOrb_loc.s" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "L_lowOrb_loc.pm" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "L_lowOrb_Ctrl_Gro_parentConstraint1.w0" "L_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.ctx" "L_EyeOutCorner_Ctrl_Gro.tx"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.cty" "L_EyeOutCorner_Ctrl_Gro.ty"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.ctz" "L_EyeOutCorner_Ctrl_Gro.tz"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.crx" "L_EyeOutCorner_Ctrl_Gro.rx"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.cry" "L_EyeOutCorner_Ctrl_Gro.ry"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.crz" "L_EyeOutCorner_Ctrl_Gro.rz"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.csx" "L_EyeOutCorner_Ctrl_Gro.sx"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.csy" "L_EyeOutCorner_Ctrl_Gro.sy"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.csz" "L_EyeOutCorner_Ctrl_Gro.sz"
		 -l on;
connectAttr "L_EyeOutCorner_Ctrl_Gro.pim" "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.cpim"
		;
connectAttr "L_EyeOutCorner_loc.s" "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.tg[0].ts"
		;
connectAttr "L_EyeOutCorner_loc.pm" "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.tg[0].tpm"
		;
connectAttr "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.w0" "L_EyeOutCorner_Ctrl_Gro_scaleConstraint1.tg[0].tw"
		;
connectAttr "L_EyeOutCorner_Ctrl_Gro.ro" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "L_EyeOutCorner_Ctrl_Gro.pim" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "L_EyeOutCorner_Ctrl_Gro.rp" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "L_EyeOutCorner_Ctrl_Gro.rpt" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "L_EyeOutCorner_loc.t" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "L_EyeOutCorner_loc.rp" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "L_EyeOutCorner_loc.rpt" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "L_EyeOutCorner_loc.r" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "L_EyeOutCorner_loc.ro" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "L_EyeOutCorner_loc.s" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "L_EyeOutCorner_loc.pm" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.w0" "L_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.ctx" "L_EyeInnCorner_Ctrl_Gro.tx"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.cty" "L_EyeInnCorner_Ctrl_Gro.ty"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.ctz" "L_EyeInnCorner_Ctrl_Gro.tz"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.crx" "L_EyeInnCorner_Ctrl_Gro.rx"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.cry" "L_EyeInnCorner_Ctrl_Gro.ry"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.crz" "L_EyeInnCorner_Ctrl_Gro.rz"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.csx" "L_EyeInnCorner_Ctrl_Gro.sx"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.csy" "L_EyeInnCorner_Ctrl_Gro.sy"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.csz" "L_EyeInnCorner_Ctrl_Gro.sz"
		 -l on;
connectAttr "L_EyeInnCorner_Ctrl_Gro.pim" "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.cpim"
		;
connectAttr "L_EyeInnCorner_loc.s" "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.tg[0].ts"
		;
connectAttr "L_EyeInnCorner_loc.pm" "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.tg[0].tpm"
		;
connectAttr "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.w0" "L_EyeInnCorner_Ctrl_Gro_scaleConstraint1.tg[0].tw"
		;
connectAttr "L_EyeInnCorner_Ctrl_Gro.ro" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "L_EyeInnCorner_Ctrl_Gro.pim" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "L_EyeInnCorner_Ctrl_Gro.rp" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "L_EyeInnCorner_Ctrl_Gro.rpt" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "L_EyeInnCorner_loc.t" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "L_EyeInnCorner_loc.rp" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "L_EyeInnCorner_loc.rpt" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "L_EyeInnCorner_loc.r" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "L_EyeInnCorner_loc.ro" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "L_EyeInnCorner_loc.s" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "L_EyeInnCorner_loc.pm" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.w0" "L_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "facial__Ctrl.Face_C" "R_Eye_Grp.v" -l on;
connectAttr "R_BLid_Ctrl_Gro_parentConstraint1.ctx" "R_BLid_Ctrl_Gro.tx" -l on;
connectAttr "R_BLid_Ctrl_Gro_parentConstraint1.cty" "R_BLid_Ctrl_Gro.ty" -l on;
connectAttr "R_BLid_Ctrl_Gro_parentConstraint1.ctz" "R_BLid_Ctrl_Gro.tz" -l on;
connectAttr "R_BLid_Ctrl_Gro_parentConstraint1.crx" "R_BLid_Ctrl_Gro.rx" -l on;
connectAttr "R_BLid_Ctrl_Gro_parentConstraint1.cry" "R_BLid_Ctrl_Gro.ry" -l on;
connectAttr "R_BLid_Ctrl_Gro_parentConstraint1.crz" "R_BLid_Ctrl_Gro.rz" -l on;
connectAttr "R_BLid_Ctrl_Gro.ro" "R_BLid_Ctrl_Gro_parentConstraint1.cro";
connectAttr "R_BLid_Ctrl_Gro.pim" "R_BLid_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "R_BLid_Ctrl_Gro.rp" "R_BLid_Ctrl_Gro_parentConstraint1.crp";
connectAttr "R_BLid_Ctrl_Gro.rpt" "R_BLid_Ctrl_Gro_parentConstraint1.crt";
connectAttr "R_BLid_loc.t" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_BLid_loc.rp" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "R_BLid_loc.rpt" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "R_BLid_loc.r" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_BLid_loc.ro" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "R_BLid_loc.s" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_BLid_loc.pm" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "R_BLid_Ctrl_Gro_parentConstraint1.w0" "R_BLid_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_TLid_Ctrl_Gro_parentConstraint1.ctx" "R_TLid_Ctrl_Gro.tx" -l on;
connectAttr "R_TLid_Ctrl_Gro_parentConstraint1.cty" "R_TLid_Ctrl_Gro.ty" -l on;
connectAttr "R_TLid_Ctrl_Gro_parentConstraint1.ctz" "R_TLid_Ctrl_Gro.tz" -l on;
connectAttr "R_TLid_Ctrl_Gro_parentConstraint1.crx" "R_TLid_Ctrl_Gro.rx" -l on;
connectAttr "R_TLid_Ctrl_Gro_parentConstraint1.cry" "R_TLid_Ctrl_Gro.ry" -l on;
connectAttr "R_TLid_Ctrl_Gro_parentConstraint1.crz" "R_TLid_Ctrl_Gro.rz" -l on;
connectAttr "R_TLid_Ctrl_Gro.ro" "R_TLid_Ctrl_Gro_parentConstraint1.cro";
connectAttr "R_TLid_Ctrl_Gro.pim" "R_TLid_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "R_TLid_Ctrl_Gro.rp" "R_TLid_Ctrl_Gro_parentConstraint1.crp";
connectAttr "R_TLid_Ctrl_Gro.rpt" "R_TLid_Ctrl_Gro_parentConstraint1.crt";
connectAttr "R_TLid_loc.t" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_TLid_loc.rp" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "R_TLid_loc.rpt" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "R_TLid_loc.r" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_TLid_loc.ro" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "R_TLid_loc.s" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_TLid_loc.pm" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "R_TLid_Ctrl_Gro_parentConstraint1.w0" "R_TLid_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_Eyeball_Ctrl_Gro_parentConstraint1.ctx" "R_Eyeball_Ctrl_Gro.tx" -l
		 on;
connectAttr "R_Eyeball_Ctrl_Gro_parentConstraint1.cty" "R_Eyeball_Ctrl_Gro.ty" -l
		 on;
connectAttr "R_Eyeball_Ctrl_Gro_parentConstraint1.ctz" "R_Eyeball_Ctrl_Gro.tz" -l
		 on;
connectAttr "R_Eyeball_Ctrl_Gro_parentConstraint1.crx" "R_Eyeball_Ctrl_Gro.rx" -l
		 on;
connectAttr "R_Eyeball_Ctrl_Gro_parentConstraint1.cry" "R_Eyeball_Ctrl_Gro.ry" -l
		 on;
connectAttr "R_Eyeball_Ctrl_Gro_parentConstraint1.crz" "R_Eyeball_Ctrl_Gro.rz" -l
		 on;
connectAttr "R_Eyeball_Ctrl_Gro.ro" "R_Eyeball_Ctrl_Gro_parentConstraint1.cro";
connectAttr "R_Eyeball_Ctrl_Gro.pim" "R_Eyeball_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "R_Eyeball_Ctrl_Gro.rp" "R_Eyeball_Ctrl_Gro_parentConstraint1.crp";
connectAttr "R_Eyeball_Ctrl_Gro.rpt" "R_Eyeball_Ctrl_Gro_parentConstraint1.crt";
connectAttr "R_Pupil_loc.t" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_Pupil_loc.rp" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "R_Pupil_loc.rpt" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "R_Pupil_loc.r" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_Pupil_loc.ro" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "R_Pupil_loc.s" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_Pupil_loc.pm" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "R_Eyeball_Ctrl_Gro_parentConstraint1.w0" "R_Eyeball_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_UppOrb_Ctrl_Gro_parentConstraint1.ctx" "R_UppOrb_Ctrl_Gro.tx" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_parentConstraint1.cty" "R_UppOrb_Ctrl_Gro.ty" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_parentConstraint1.ctz" "R_UppOrb_Ctrl_Gro.tz" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_parentConstraint1.crx" "R_UppOrb_Ctrl_Gro.rx" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_parentConstraint1.cry" "R_UppOrb_Ctrl_Gro.ry" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_parentConstraint1.crz" "R_UppOrb_Ctrl_Gro.rz" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_scaleConstraint1.csx" "R_UppOrb_Ctrl_Gro.sx" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_scaleConstraint1.csy" "R_UppOrb_Ctrl_Gro.sy" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro_scaleConstraint1.csz" "R_UppOrb_Ctrl_Gro.sz" -l on
		;
connectAttr "R_UppOrb_Ctrl_Gro.ro" "R_UppOrb_Ctrl_Gro_parentConstraint1.cro";
connectAttr "R_UppOrb_Ctrl_Gro.pim" "R_UppOrb_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "R_UppOrb_Ctrl_Gro.rp" "R_UppOrb_Ctrl_Gro_parentConstraint1.crp";
connectAttr "R_UppOrb_Ctrl_Gro.rpt" "R_UppOrb_Ctrl_Gro_parentConstraint1.crt";
connectAttr "R_UppOrb_loc.t" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_UppOrb_loc.rp" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "R_UppOrb_loc.rpt" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "R_UppOrb_loc.r" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_UppOrb_loc.ro" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "R_UppOrb_loc.s" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_UppOrb_loc.pm" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "R_UppOrb_Ctrl_Gro_parentConstraint1.w0" "R_UppOrb_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_UppOrb_Ctrl_Gro.pim" "R_UppOrb_Ctrl_Gro_scaleConstraint1.cpim";
connectAttr "R_UppOrb_loc.s" "R_UppOrb_Ctrl_Gro_scaleConstraint1.tg[0].ts";
connectAttr "R_UppOrb_loc.pm" "R_UppOrb_Ctrl_Gro_scaleConstraint1.tg[0].tpm";
connectAttr "R_UppOrb_Ctrl_Gro_scaleConstraint1.w0" "R_UppOrb_Ctrl_Gro_scaleConstraint1.tg[0].tw"
		;
connectAttr "R_lowOrb_Ctrl_Gro_parentConstraint1.ctx" "R_lowOrb_Ctrl_Gro.tx" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_parentConstraint1.cty" "R_lowOrb_Ctrl_Gro.ty" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_parentConstraint1.ctz" "R_lowOrb_Ctrl_Gro.tz" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_parentConstraint1.crx" "R_lowOrb_Ctrl_Gro.rx" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_parentConstraint1.cry" "R_lowOrb_Ctrl_Gro.ry" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_parentConstraint1.crz" "R_lowOrb_Ctrl_Gro.rz" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_scaleConstraint1.csx" "R_lowOrb_Ctrl_Gro.sx" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_scaleConstraint1.csy" "R_lowOrb_Ctrl_Gro.sy" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro_scaleConstraint1.csz" "R_lowOrb_Ctrl_Gro.sz" -l on
		;
connectAttr "R_lowOrb_Ctrl_Gro.ro" "R_lowOrb_Ctrl_Gro_parentConstraint1.cro";
connectAttr "R_lowOrb_Ctrl_Gro.pim" "R_lowOrb_Ctrl_Gro_parentConstraint1.cpim";
connectAttr "R_lowOrb_Ctrl_Gro.rp" "R_lowOrb_Ctrl_Gro_parentConstraint1.crp";
connectAttr "R_lowOrb_Ctrl_Gro.rpt" "R_lowOrb_Ctrl_Gro_parentConstraint1.crt";
connectAttr "R_lowOrb_loc.t" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tt";
connectAttr "R_lowOrb_loc.rp" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].trp";
connectAttr "R_lowOrb_loc.rpt" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].trt";
connectAttr "R_lowOrb_loc.r" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tr";
connectAttr "R_lowOrb_loc.ro" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tro";
connectAttr "R_lowOrb_loc.s" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].ts";
connectAttr "R_lowOrb_loc.pm" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tpm";
connectAttr "R_lowOrb_Ctrl_Gro_parentConstraint1.w0" "R_lowOrb_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_lowOrb_Ctrl_Gro.pim" "R_lowOrb_Ctrl_Gro_scaleConstraint1.cpim";
connectAttr "R_lowOrb_loc.s" "R_lowOrb_Ctrl_Gro_scaleConstraint1.tg[0].ts";
connectAttr "R_lowOrb_loc.pm" "R_lowOrb_Ctrl_Gro_scaleConstraint1.tg[0].tpm";
connectAttr "R_lowOrb_Ctrl_Gro_scaleConstraint1.w0" "R_lowOrb_Ctrl_Gro_scaleConstraint1.tg[0].tw"
		;
connectAttr "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.ctx" "R_EyeOutCorner_Ctrl_Gro.tx"
		 -l on;
connectAttr "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.cty" "R_EyeOutCorner_Ctrl_Gro.ty"
		 -l on;
connectAttr "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.ctz" "R_EyeOutCorner_Ctrl_Gro.tz"
		 -l on;
connectAttr "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.crx" "R_EyeOutCorner_Ctrl_Gro.rx"
		 -l on;
connectAttr "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.cry" "R_EyeOutCorner_Ctrl_Gro.ry"
		 -l on;
connectAttr "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.crz" "R_EyeOutCorner_Ctrl_Gro.rz"
		 -l on;
connectAttr "R_EyeOutCorner_Ctrl_Gro.ro" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "R_EyeOutCorner_Ctrl_Gro.pim" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "R_EyeOutCorner_Ctrl_Gro.rp" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "R_EyeOutCorner_Ctrl_Gro.rpt" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "R_EyeOutCorner_loc.t" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "R_EyeOutCorner_loc.rp" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "R_EyeOutCorner_loc.rpt" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "R_EyeOutCorner_loc.r" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "R_EyeOutCorner_loc.ro" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "R_EyeOutCorner_loc.s" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "R_EyeOutCorner_loc.pm" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.w0" "R_EyeOutCorner_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.ctx" "R_EyeInnCorner_Ctrl_Gro.tx"
		 -l on;
connectAttr "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.cty" "R_EyeInnCorner_Ctrl_Gro.ty"
		 -l on;
connectAttr "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.ctz" "R_EyeInnCorner_Ctrl_Gro.tz"
		 -l on;
connectAttr "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.crx" "R_EyeInnCorner_Ctrl_Gro.rx"
		 -l on;
connectAttr "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.cry" "R_EyeInnCorner_Ctrl_Gro.ry"
		 -l on;
connectAttr "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.crz" "R_EyeInnCorner_Ctrl_Gro.rz"
		 -l on;
connectAttr "R_EyeInnCorner_Ctrl_Gro.ro" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.cro"
		;
connectAttr "R_EyeInnCorner_Ctrl_Gro.pim" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.cpim"
		;
connectAttr "R_EyeInnCorner_Ctrl_Gro.rp" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.crp"
		;
connectAttr "R_EyeInnCorner_Ctrl_Gro.rpt" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.crt"
		;
connectAttr "R_EyeInnCorner_loc.t" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tt"
		;
connectAttr "R_EyeInnCorner_loc.rp" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].trp"
		;
connectAttr "R_EyeInnCorner_loc.rpt" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].trt"
		;
connectAttr "R_EyeInnCorner_loc.r" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tr"
		;
connectAttr "R_EyeInnCorner_loc.ro" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tro"
		;
connectAttr "R_EyeInnCorner_loc.s" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].ts"
		;
connectAttr "R_EyeInnCorner_loc.pm" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tpm"
		;
connectAttr "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.w0" "R_EyeInnCorner_Ctrl_Gro_parentConstraint1.tg[0].tw"
		;
connectAttr "facial__Ctrl.Face_C" "L_Face_Grp.v" -l on;
connectAttr "facial__Ctrl.Face_C" "R_Face_Grp.v" -l on;
connectAttr "facial__Ctrl.Face_C" "L_Ear_Grp.v" -l on;
connectAttr "facial__Ctrl.Face_C" "R_Ear_Grp.v" -l on;
connectAttr "facial__Ctrl.Face_C" "C_palate_Grp.v" -l on;
connectAttr "facial__Ctrl.Face_C" "C_teeth_Grp.v" -l on;
connectAttr "facial__Ctrl.Defm_C" "Deform_Ctrl_Grp.v";
connectAttr "facial__Ctrl.Sel_C" "Face_Pose__Sel.v";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":defaultObjectSet.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":hyperGraphLayout.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr ":TurtleDefaultBakeLayer.idx" ":TurtleBakeLayerManager.bli[0]";
connectAttr ":TurtleRenderOptions.msg" ":TurtleDefaultBakeLayer.rset";
connectAttr ":defaultArnoldDisplayDriver.msg" ":defaultArnoldRenderOptions.drivers"
		 -na;
connectAttr ":defaultArnoldFilter.msg" ":defaultArnoldRenderOptions.filt";
connectAttr ":defaultArnoldDriver.msg" ":defaultArnoldRenderOptions.drvr";
connectAttr ":mentalrayGlobals.msg" ":mentalrayItemsList.glb";
connectAttr ":miDefaultOptions.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayItemsList.fb" -na;
connectAttr ":miDefaultOptions.msg" ":mentalrayGlobals.opt";
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayGlobals.fb";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "groupId9.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3879.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3905.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3906.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId34.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId8.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId83.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId93.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId124.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3907.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3908.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3918.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId15.msg" ":initialShadingGroup.gn" -na;
connectAttr ":perspShape.msg" ":defaultRenderGlobals.sc";
// End of facial_ctrl.ma
