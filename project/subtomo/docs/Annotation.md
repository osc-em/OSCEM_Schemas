
# Class: Annotation

A primitive annotation.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Annotation](https://w3id.org/osc-em/oscem-schemas-subtomo/Annotation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TriMesh],[SegmentationMask3D],[SegmentationMask2D],[ProbabilityMap3D],[ProbabilityMap2D],[PointVectorSet3D],[PointVectorSet2D],[PointSet3D],[PointSet2D],[PointMatrixSet3D],[PointMatrixSet2D],[Region]++-%20annotations%200..*>[Annotation&#124;path:string%20%3F],[Average]++-%20annotations%200..*>[Annotation],[Annotation]^-[TriMesh],[Annotation]^-[SegmentationMask3D],[Annotation]^-[SegmentationMask2D],[Annotation]^-[ProbabilityMap3D],[Annotation]^-[ProbabilityMap2D],[Annotation]^-[PointVectorSet3D],[Annotation]^-[PointVectorSet2D],[Annotation]^-[PointSet3D],[Annotation]^-[PointSet2D],[Annotation]^-[PointMatrixSet3D],[Annotation]^-[PointMatrixSet2D],[Region],[Average])](https://yuml.me/diagram/nofunky;dir:TB/class/[TriMesh],[SegmentationMask3D],[SegmentationMask2D],[ProbabilityMap3D],[ProbabilityMap2D],[PointVectorSet3D],[PointVectorSet2D],[PointSet3D],[PointSet2D],[PointMatrixSet3D],[PointMatrixSet2D],[Region]++-%20annotations%200..*>[Annotation&#124;path:string%20%3F],[Average]++-%20annotations%200..*>[Annotation],[Annotation]^-[TriMesh],[Annotation]^-[SegmentationMask3D],[Annotation]^-[SegmentationMask2D],[Annotation]^-[ProbabilityMap3D],[Annotation]^-[ProbabilityMap2D],[Annotation]^-[PointVectorSet3D],[Annotation]^-[PointVectorSet2D],[Annotation]^-[PointSet3D],[Annotation]^-[PointSet2D],[Annotation]^-[PointMatrixSet3D],[Annotation]^-[PointMatrixSet2D],[Region],[Average])

## Children

 * [PointMatrixSet2D](PointMatrixSet2D.md) - A set of 2D points with an associated rotation matrix.
 * [PointMatrixSet3D](PointMatrixSet3D.md) - A set of 3D points with an associated rotation matrix.
 * [PointSet2D](PointSet2D.md) - A set of 2D point annotations.
 * [PointSet3D](PointSet3D.md) - A set of 3D point annotations.
 * [PointVectorSet2D](PointVectorSet2D.md) - A set of 2D points with an associated direction vector.
 * [PointVectorSet3D](PointVectorSet3D.md) - A set of 3D points with an associated direction vector.
 * [ProbabilityMap2D](ProbabilityMap2D.md) - An annotation image with real-valued labels.
 * [ProbabilityMap3D](ProbabilityMap3D.md) - An annotation volume with real-valued labels.
 * [SegmentationMask2D](SegmentationMask2D.md) - An annotation image with categorical labels.
 * [SegmentationMask3D](SegmentationMask3D.md) - An annotation volume with categorical labels.
 * [TriMesh](TriMesh.md) - A mesh annotation.

## Referenced by Class

 *  **None** *[annotations](annotations.md)*  <sub>0..\*</sub>  **[Annotation](Annotation.md)**

## Attributes


### Own

 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)
