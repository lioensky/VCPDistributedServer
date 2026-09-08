GeometryNode(NodeInternal)
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`

subclasses --- 
:class:`GeometryNodeAccumulateField`, :class:`GeometryNodeAttributeDomainSize`, :class:`GeometryNodeAttributeStatistic`, :class:`GeometryNodeBake`, :class:`GeometryNodeBlurAttribute`, :class:`GeometryNodeBoneInfo`, :class:`GeometryNodeBoundBox`, :class:`GeometryNodeCameraInfo`, :class:`GeometryNodeCaptureAttribute`, :class:`GeometryNodeCollectionInfo`, :class:`GeometryNodeConvexHull`, :class:`GeometryNodeCornersOfEdge`, :class:`GeometryNodeCornersOfFace`, :class:`GeometryNodeCornersOfVertex`, :class:`GeometryNodeCubeGridTopology`, :class:`GeometryNodeCurveArc`, :class:`GeometryNodeCurveEndpointSelection`, :class:`GeometryNodeCurveHandleTypeSelection`, :class:`GeometryNodeCurveLength`, :class:`GeometryNodeCurveOfPoint`, :class:`GeometryNodeCurvePrimitiveBezierSegment`, :class:`GeometryNodeCurvePrimitiveCircle`, :class:`GeometryNodeCurvePrimitiveLine`, :class:`GeometryNodeCurvePrimitiveQuadrilateral`, :class:`GeometryNodeCurveQuadraticBezier`, :class:`GeometryNodeCurveSetHandles`, :class:`GeometryNodeCurveSpiral`, :class:`GeometryNodeCurveSplineType`, :class:`GeometryNodeCurveStar`, :class:`GeometryNodeCurveToMesh`, :class:`GeometryNodeCurveToPoints`, :class:`GeometryNodeCurvesToGreasePencil`, :class:`GeometryNodeCustomGroup`, :class:`GeometryNodeDeformCurvesOnSurface`, :class:`GeometryNodeDeleteGeometry`, :class:`GeometryNodeDistributePointsInGrid`, :class:`GeometryNodeDistributePointsInVolume`, :class:`GeometryNodeDistributePointsOnFaces`, :class:`GeometryNodeDualMesh`, :class:`GeometryNodeDuplicateElements`, :class:`GeometryNodeEdgePathsToCurves`, :class:`GeometryNodeEdgePathsToSelection`, :class:`GeometryNodeEdgesOfCorner`, :class:`GeometryNodeEdgesOfVertex`, :class:`GeometryNodeEdgesToFaceGroups`, :class:`GeometryNodeExtrudeMesh`, :class:`GeometryNodeFaceOfCorner`, :class:`GeometryNodeFieldAtIndex`, :class:`GeometryNodeFieldAverage`, :class:`GeometryNodeFieldMinAndMax`, :class:`GeometryNodeFieldOnDomain`, :class:`GeometryNodeFieldToGrid`, :class:`GeometryNodeFieldToList`, :class:`GeometryNodeFieldVariance`, :class:`GeometryNodeFillCurve`, :class:`GeometryNodeFilletCurve`, :class:`GeometryNodeFlipFaces`, :class:`GeometryNodeForeachGeometryElementInput`, :class:`GeometryNodeForeachGeometryElementOutput`, :class:`GeometryNodeGeometryToInstance`, :class:`GeometryNodeGetGeometryBundle`, :class:`GeometryNodeGetNamedGrid`, :class:`GeometryNodeGizmoDial`, :class:`GeometryNodeGizmoLinear`, :class:`GeometryNodeGizmoTransform`, :class:`GeometryNodeGreasePencilToCurves`, :class:`GeometryNodeGridAdvect`, :class:`GeometryNodeGridClip`, :class:`GeometryNodeGridCurl`, :class:`GeometryNodeGridDilateAndErode`, :class:`GeometryNodeGridDivergence`, :class:`GeometryNodeGridGradient`, :class:`GeometryNodeGridInfo`, :class:`GeometryNodeGridLaplacian`, :class:`GeometryNodeGridMean`, :class:`GeometryNodeGridMedian`, :class:`GeometryNodeGridPrune`, :class:`GeometryNodeGridToMesh`, :class:`GeometryNodeGridToPoints`, :class:`GeometryNodeGridVoxelize`, :class:`GeometryNodeGroup`, :class:`GeometryNodeImageInfo`, :class:`GeometryNodeImageTexture`, :class:`GeometryNodeImportCSV`, :class:`GeometryNodeImportOBJ`, :class:`GeometryNodeImportPLY`, :class:`GeometryNodeImportSTL`, :class:`GeometryNodeImportText`, :class:`GeometryNodeImportVDB`, :class:`GeometryNodeIndexOfNearest`, :class:`GeometryNodeIndexSwitch`, :class:`GeometryNodeInputActiveCamera`, :class:`GeometryNodeInputCollection`, :class:`GeometryNodeInputCurveHandlePositions`, :class:`GeometryNodeInputCurveTilt`, :class:`GeometryNodeInputEdgeSmooth`, :class:`GeometryNodeInputID`, :class:`GeometryNodeInputImage`, :class:`GeometryNodeInputIndex`, :class:`GeometryNodeInputInstanceBounds`, :class:`GeometryNodeInputInstanceRotation`, :class:`GeometryNodeInputInstanceScale`, :class:`GeometryNodeInputMaterial`, :class:`GeometryNodeInputMaterialIndex`, :class:`GeometryNodeInputMeshEdgeAngle`, :class:`GeometryNodeInputMeshEdgeNeighbors`, :class:`GeometryNodeInputMeshEdgeVertices`, :class:`GeometryNodeInputMeshFaceArea`, :class:`GeometryNodeInputMeshFaceIsPlanar`, :class:`GeometryNodeInputMeshFaceNeighbors`, :class:`GeometryNodeInputMeshIsland`, :class:`GeometryNodeInputMeshVertexNeighbors`, :class:`GeometryNodeInputNamedAttribute`, :class:`GeometryNodeInputNamedLayerSelection`, :class:`GeometryNodeInputNormal`, :class:`GeometryNodeInputObject`, :class:`GeometryNodeInputPosition`, :class:`GeometryNodeInputRadius`, :class:`GeometryNodeInputSceneTime`, :class:`GeometryNodeInputShadeSmooth`, :class:`GeometryNodeInputShortestEdgePaths`, :class:`GeometryNodeInputSplineCyclic`, :class:`GeometryNodeInputSplineResolution`, :class:`GeometryNodeInputTangent`, :class:`GeometryNodeInputVoxelIndex`, :class:`GeometryNodeInstanceOnPoints`, :class:`GeometryNodeInstanceTransform`, :class:`GeometryNodeInstancesToPoints`, :class:`GeometryNodeInterpolateCurves`, :class:`GeometryNodeIsViewport`, :class:`GeometryNodeJoinGeometry`, :class:`GeometryNodeListGetItem`, :class:`GeometryNodeListLength`, :class:`GeometryNodeMaterialSelection`, :class:`GeometryNodeMenuSwitch`, :class:`GeometryNodeMergeByDistance`, :class:`GeometryNodeMergeLayers`, :class:`GeometryNodeMeshBoolean`, :class:`GeometryNodeMeshCircle`, :class:`GeometryNodeMeshCone`, :class:`GeometryNodeMeshCube`, :class:`GeometryNodeMeshCylinder`, :class:`GeometryNodeMeshFaceSetBoundaries`, :class:`GeometryNodeMeshGrid`, :class:`GeometryNodeMeshIcoSphere`, :class:`GeometryNodeMeshLine`, :class:`GeometryNodeMeshToCurve`, :class:`GeometryNodeMeshToDensityGrid`, :class:`GeometryNodeMeshToPoints`, :class:`GeometryNodeMeshToSDFGrid`, :class:`GeometryNodeMeshToVolume`, :class:`GeometryNodeMeshUVSphere`, :class:`GeometryNodeObjectInfo`, :class:`GeometryNodeOffsetCornerInFace`, :class:`GeometryNodeOffsetPointInCurve`, :class:`GeometryNodePoints`, :class:`GeometryNodePointsOfCurve`, :class:`GeometryNodePointsToCurves`, :class:`GeometryNodePointsToSDFGrid`, :class:`GeometryNodePointsToVertices`, :class:`GeometryNodePointsToVolume`, :class:`GeometryNodeProximity`, :class:`GeometryNodeRaycast`, :class:`GeometryNodeRealizeInstances`, :class:`GeometryNodeRemoveAttribute`, :class:`GeometryNodeRepeatInput`, :class:`GeometryNodeRepeatOutput`, :class:`GeometryNodeReplaceMaterial`, :class:`GeometryNodeResampleCurve`, :class:`GeometryNodeReverseCurve`, :class:`GeometryNodeRotateInstances`, :class:`GeometryNodeSDFGridBoolean`, :class:`GeometryNodeSDFGridFillet`, :class:`GeometryNodeSDFGridLaplacian`, :class:`GeometryNodeSDFGridMean`, :class:`GeometryNodeSDFGridMeanCurvature`, :class:`GeometryNodeSDFGridMedian`, :class:`GeometryNodeSDFGridOffset`, :class:`GeometryNodeSampleCurve`, :class:`GeometryNodeSampleGrid`, :class:`GeometryNodeSampleGridIndex`, :class:`GeometryNodeSampleIndex`, :class:`GeometryNodeSampleNearest`, :class:`GeometryNodeSampleNearestSurface`, :class:`GeometryNodeSampleUVSurface`, :class:`GeometryNodeScaleElements`, :class:`GeometryNodeScaleInstances`, :class:`GeometryNodeSelfObject`, :class:`GeometryNodeSeparateComponents`, :class:`GeometryNodeSeparateGeometry`, :class:`GeometryNodeSetCurveHandlePositions`, :class:`GeometryNodeSetCurveNormal`, :class:`GeometryNodeSetCurveRadius`, :class:`GeometryNodeSetCurveTilt`, :class:`GeometryNodeSetGeometryBundle`, :class:`GeometryNodeSetGeometryName`, :class:`GeometryNodeSetGreasePencilColor`, :class:`GeometryNodeSetGreasePencilDepth`, :class:`GeometryNodeSetGreasePencilSoftness`, :class:`GeometryNodeSetGridBackground`, :class:`GeometryNodeSetGridTransform`, :class:`GeometryNodeSetID`, :class:`GeometryNodeSetInstanceTransform`, :class:`GeometryNodeSetMaterial`, :class:`GeometryNodeSetMaterialIndex`, :class:`GeometryNodeSetMeshNormal`, :class:`GeometryNodeSetPointRadius`, :class:`GeometryNodeSetPosition`, :class:`GeometryNodeSetShadeSmooth`, :class:`GeometryNodeSetSplineCyclic`, :class:`GeometryNodeSetSplineResolution`, :class:`GeometryNodeSimulationInput`, :class:`GeometryNodeSimulationOutput`, :class:`GeometryNodeSortElements`, :class:`GeometryNodeSplineLength`, :class:`GeometryNodeSplineParameter`, :class:`GeometryNodeSplitEdges`, :class:`GeometryNodeSplitToInstances`, :class:`GeometryNodeStoreNamedAttribute`, :class:`GeometryNodeStoreNamedGrid`, :class:`GeometryNodeStringJoin`, :class:`GeometryNodeStringToCurves`, :class:`GeometryNodeSubdivideCurve`, :class:`GeometryNodeSubdivideMesh`, :class:`GeometryNodeSubdivisionSurface`, :class:`GeometryNodeSwitch`, :class:`GeometryNodeTool3DCursor`, :class:`GeometryNodeToolActiveElement`, :class:`GeometryNodeToolFaceSet`, :class:`GeometryNodeToolMousePosition`, :class:`GeometryNodeToolSelection`, :class:`GeometryNodeToolSetFaceSet`, :class:`GeometryNodeToolSetSelection`, :class:`GeometryNodeTransform`, :class:`GeometryNodeTranslateInstances`, :class:`GeometryNodeTriangulate`, :class:`GeometryNodeTrimCurve`, :class:`GeometryNodeUVPackIslands`, :class:`GeometryNodeUVTangent`, :class:`GeometryNodeUVUnwrap`, :class:`GeometryNodeVertexOfCorner`, :class:`GeometryNodeViewer`, :class:`GeometryNodeViewportTransform`, :class:`GeometryNodeVolumeCube`, :class:`GeometryNodeVolumeToMesh`, :class:`GeometryNodeWarning`

.. class:: GeometryNode(NodeInternal)


   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`
   - :class:`Node.type`
   - :class:`Node.location`
   - :class:`Node.location_absolute`
   - :class:`Node.width`
   - :class:`Node.height`
   - :class:`Node.dimensions`
   - :class:`Node.name`
   - :class:`Node.label`
   - :class:`Node.inputs`
   - :class:`Node.outputs`
   - :class:`Node.internal_links`
   - :class:`Node.parent`
   - :class:`Node.warning_propagation`
   - :class:`Node.use_custom_color`
   - :class:`Node.color`
   - :class:`Node.color_tag`
   - :class:`Node.select`
   - :class:`Node.show_options`
   - :class:`Node.show_preview`
   - :class:`Node.hide`
   - :class:`Node.mute`
   - :class:`Node.show_texture`
   - :class:`Node.bl_idname`
   - :class:`Node.bl_label`
   - :class:`Node.bl_description`
   - :class:`Node.bl_icon`
   - :class:`Node.bl_static_type`
   - :class:`Node.bl_width_default`
   - :class:`Node.bl_width_min`
   - :class:`Node.bl_width_max`
   - :class:`Node.bl_height_default`
   - :class:`Node.bl_height_min`
   - :class:`Node.bl_height_max`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`
   - :class:`Node.bl_system_properties_get`
   - :class:`Node.socket_value_update`
   - :class:`Node.is_registered_node_type`
   - :class:`Node.poll`
   - :class:`Node.poll_instance`
   - :class:`Node.update`
   - :class:`Node.insert_link`
   - :class:`Node.init`
   - :class:`Node.copy`
   - :class:`Node.free`
   - :class:`Node.draw_buttons`
   - :class:`Node.draw_buttons_ext`
   - :class:`Node.draw_label`
   - :class:`Node.debug_zone_body_lazy_function_graph`
   - :class:`Node.debug_zone_lazy_function_graph`
   - :class:`Node.poll`
   - :class:`Node.bl_rna_get_subclass`
   - :class:`Node.bl_rna_get_subclass_py`
   - :class:`NodeInternal.poll`
   - :class:`NodeInternal.poll_instance`
   - :class:`NodeInternal.update`
   - :class:`NodeInternal.draw_buttons`
   - :class:`NodeInternal.draw_buttons_ext`
   - :class:`NodeInternal.bl_rna_get_subclass`
   - :class:`NodeInternal.bl_rna_get_subclass_py`

