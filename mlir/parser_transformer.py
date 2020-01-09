from lark import v_args, Transformer
from mlir import astnodes


class TreeToMlir(Transformer):
    ###############################################################
    # Low-level literal syntax
    digit = lambda self, val: int(val[0])
    hex_digit = lambda self, val: str(val[0])
    letter = lambda self, val: str(val[0])
    id_punct = lambda self, val: str(val[0])
    underscore = lambda self, val: str(val[0])
    true = lambda self, _: True
    false = lambda self, _: False
    id_chars = lambda self, val: str(val[0])
    dimension = astnodes.Dimension

    # Literals
    @v_args(inline=True)
    def decimal_literal(self, *digits):
        return int(''.join(str(d) for d in digits))

    @v_args(inline=True)
    def hexadecimal_literal(self, *digits):
        return '0x' + ''.join(digits)

    float_literal = lambda self, value: float(value[0])

    @v_args(inline=True)
    def string_literal(self, s):
        return astnodes.StringLiteral(s[1:-1].replace('\\"', '"'))

    @v_args(inline=True)
    def bare_id(self, *s):
        return ''.join(s)

    @v_args(inline=True)
    def suffix_id(self, *suffix):
        return ''.join(str(s) for s in suffix)

    ###############################################################
    # MLIR Identifiers

    ssa_id = astnodes.SsaId
    symbol_ref_id = astnodes.SymbolRefId
    block_id = astnodes.BlockId
    type_alias = astnodes.TypeAlias
    map_or_set_id = astnodes.MapOrSetId

    ###############################################################
    # MLIR Types

    none_type = astnodes.NoneType
    f16 = lambda self, _: "f16"
    bf16 = lambda self, _: "bf16"
    f32 = lambda self, _: "f32"
    f64 = lambda self, _: "f64"
    float_type = astnodes.FloatType
    index_type = astnodes.IndexType
    integer_type = astnodes.IntegerType
    complex_type = astnodes.ComplexType
    tuple_type = astnodes.TupleType
    vector_type = astnodes.VectorType
    ranked_tensor_type = astnodes.RankedTensorType
    unranked_tensor_type = astnodes.UnrankedTensorType
    ranked_memref_type = astnodes.RankedMemRefType
    unranked_memref_type = astnodes.UnrankedMemRefType
    opaque_dialect_item = astnodes.OpaqueDialectType
    pretty_dialect_item = astnodes.PrettyDialectType
    function_type = astnodes.FunctionType
    strided_layout = astnodes.StridedLayout

    ###############################################################
    # MLIR Attributes

    array_attribute = astnodes.ArrayAttr
    bool_attribute = astnodes.BoolAttr
    dictionary_attribute = astnodes.DictionaryAttr
    dense_elements_attribute = astnodes.DenseElementsAttr
    opaque_elements_attribute = astnodes.OpaqueElementsAttr
    sparse_elements_attribute = astnodes.SparseElementsAttr
    float_attribute = astnodes.FloatAttr
    integer_attribute = astnodes.IntegerAttr
    integer_set_attribute = astnodes.IntSetAttr
    string_attribute = astnodes.StringAttr
    symbol_ref_attribute = astnodes.SymbolRefAttr
    type_attribute = astnodes.TypeAttr
    unit_attribute = astnodes.UnitAttr

    dependent_attribute_entry = astnodes.AttributeEntry
    dialect_attribute_entry = astnodes.DialectAttributeEntry
    attribute_dict = astnodes.AttributeDict

    ###############################################################
    # Operations

    op_result = astnodes.OpResult
    location = astnodes.FileLineColLoc

    operation = astnodes.Operation
    generic_operation = astnodes.GenericOperation
    custom_operation = astnodes.CustomOperation

    ###############################################################
    # Blocks, regions, modules, functions

    block_label = astnodes.BlockLabel
    block = astnodes.Block
    region = list
    module = astnodes.Module
    function = astnodes.Function
    named_argument = astnodes.NamedArgument

    ###############################################################
    # TODO: (semi-)Affine expressions, maps, and integer sets

    ###############################################################
    # TODO: Top-level definitions

    ###############################################################
    # List types
    bare_id_list = list
    ssa_id_list = list
    ssa_use_list = list
    op_result_list = list
    successor_list = list
    function_body = list
    ssa_id_and_type_list = list
    block_arg_list = list
    ssa_use_and_type_list = list
    stride_list = list
    dimension_list_ranked = list
    static_dimension_list = list
    pretty_dialect_item_body = list
    type_list_no_parens = list
    affine_constraint_conjunction = list
    function_result_list_no_parens = list
    dim_id_list = list
    symbol_id_list = list

    ###############################################################
    # Composite types that should be reduced to sub-types
    bool_literal = lambda self, value: value[0]
    integer_literal = lambda self, value: value[0]
    constant_literal = lambda self, value: value[0]
    dimension_list = lambda self, value: value[0]
    ssa_use = lambda self, value: value[0]
    vector_element_type = lambda self, value: value[0]
    tensor_memref_element_type = lambda self, value: value[0]
    tensor_type = lambda self, value: value[0]
    memref_type = lambda self, value: value[0]
    standard_type = lambda self, value: value[0]
    dialect_type = lambda self, value: value[0]
    non_function_type = lambda self, value: value[0]
    type = lambda self, value: value[0]
    type_list_parens = lambda self, value: (value[0] if value else [])
    function_result_type = lambda self, value: value[0]
    standard_attribute = lambda self, value: value[0]
    attribute_value = lambda self, value: value[0]
    dialect_attribute = lambda self, value: value[0]
    attribute_entry = lambda self, value: value[0]
    trailing_type = lambda self, value: value[0]
    trailing_location = lambda self, value: value[0]
    function_result_list_parens = lambda self, value: value[0]
    symbol_or_const = lambda self, value: value[0]
    affine_map = lambda self, value: value[0]
    semi_affine_map = lambda self, value: value[0]
    integer_set = lambda self, value: value[0]

    # Dialect ops and types
    pymlir_dialect_ops = lambda self, value: value[0].children[0]
    pymlir_dialect_types = lambda self, value: value[0].children[0]
