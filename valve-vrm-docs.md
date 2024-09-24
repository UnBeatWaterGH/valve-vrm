# VRM (Valve MRM) Format
## Commands
### `version`
 Always equal to 2, otherwise the file can be considered as using a "bad version".
### `name`
 Contains the name of the file/object.

 Ignored by StudioMDL.

--------------------------------------------------------------------------------

### `vertices`
 Amount of vertices.
### `faces`
 Amount of faces.
### `materials`
 Amount of materials.

 Ignored by StudioMDL.
### `texcoords`
 Amount of texture coordinates.

 Always above 0, otherwise StudioMDL complains.
### `normals`
 Amount of normals.
### `tristrips`
 Should always be 0.

 Ignored by StudioMDL.

--------------------------------------------------------------------------------

### `nodes`
 Same as in SMD.
### `skeleton`
 Same as in SMD.

--------------------------------------------------------------------------------

### `vertexlist`
 List of vertices.
 
 Each item in the list: `<int|ID> <int|Parent Bone> <float|PosX PosY PosZ> <int|links> <int|Bone ID> <float|Weight> [...]`
### `facelist`
 List of faces (triangles).

 Each item in the list: `<int|ID> <int|VertA VertB VertC>`
### `materiallist`
 List of materials.

 Each item in the list: `<int|ID>  <float|ARed AGreen ABlue AAlpha>   <float|DRed DGreen DBlue DAlpha>  <float|SRed SGreen SBlue SAlpha>  "<string|Texture Path>"`
### `texcoordlist`
 List of texture (UV) coordinates.

 Each item in the list: `<int|ID> <float|U V>`
### `normallist`
 List of normals.

 Each item in the list: `<int|ID> <int|Bone ID> <float|NormX NormY NormZ>`
### `faceattriblist`
 List of face attributes.

 Each item in the list: `<int|ID> <int|Material ID> <int|Smooth> <int|TexCoordA TexCoordB TexCoordC> <int|NormA NormB NormC>`

--------------------------------------------------------------------------------

## `MRM`
 TODO: Figure this shit out.

 Ignored by StudioMDL.
### `MRMvertices`
 TODO: Figure this shit out.

 Ignored by StudioMDL.
### `MRMfaces`
 TODO: Figure this shit out.

 Ignored by StudioMDL.
### `MRMfaceupdates`
 TODO: Figure this shit out.
 
 Basically ignored by StudioMDL.

--------------------------------------------------------------------------------

## Documentation progress
- [x] Document all lists.
- [ ] Document options for lists properly (descriptions, examples, etc.).
- [ ] MRM. (Might not need to figure it out?)
- [x] Check older versions of code to see if that might implement MRM. (2003 does not!)
