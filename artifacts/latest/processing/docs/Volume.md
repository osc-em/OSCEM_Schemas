
# Class: Volume

Class describing volume(s) obtained

URI: [processing:Volume](https://w3id.org/oscem-schemas/latest/processingVolume)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[IsosurfaceImages]<isosurface_images%200..1-++[Volume],[OrthogonalSlices]<orthogonal_slices%200..1-++[Volume],[Classes3D]++-%20volume%200..*>[Volume],[Classes3D]++-%20volume(i)%200..*>[Volume],[OrthogonalSlices],[IsosurfaceImages],[Classes3D])](https://yuml.me/diagram/nofunky;dir:TB/class/[IsosurfaceImages]<isosurface_images%200..1-++[Volume],[OrthogonalSlices]<orthogonal_slices%200..1-++[Volume],[Classes3D]++-%20volume%200..*>[Volume],[Classes3D]++-%20volume(i)%200..*>[Volume],[OrthogonalSlices],[IsosurfaceImages],[Classes3D])

## Referenced by Class

 *  **[Classes3D](Classes3D.md)** *[Classes3D➞volume](Classes3D_volume.md)*  <sub>0..\*</sub>  **[Volume](Volume.md)**
 *  **None** *[volume](volume.md)*  <sub>0..\*</sub>  **[Volume](Volume.md)**

## Attributes


### Own

 * [Volume➞orthogonal_slices](Volume_orthogonal_slices.md)  <sub>0..1</sub>
     * Description: orthogonal slices of volume
     * Range: [OrthogonalSlices](OrthogonalSlices.md)
 * [Volume➞isosurface_images](Volume_isosurface_images.md)  <sub>0..1</sub>
     * Description: isosurface images of volume
     * Range: [IsosurfaceImages](IsosurfaceImages.md)
