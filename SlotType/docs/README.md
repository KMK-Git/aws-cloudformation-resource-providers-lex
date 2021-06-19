# CustomResource::Lex::SlotType

Resource schema for CustomResource::Lex::SlotType

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "CustomResource::Lex::SlotType",
    "Properties" : {
        "<a href="#createversion" title="CreateVersion">CreateVersion</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enumerationvalues" title="EnumerationValues">EnumerationValues</a>" : <i>[ <a href="enumerationvalue.md">EnumerationValue</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentslottypesignature" title="ParentSlotTypeSignature">ParentSlotTypeSignature</a>" : <i>String</i>,
        "<a href="#slottypeconfigurations" title="SlotTypeConfigurations">SlotTypeConfigurations</a>" : <i>[ <a href="slottypeconfiguration.md">SlotTypeConfiguration</a>, ... ]</i>,
        "<a href="#valueselectionstrategy" title="ValueSelectionStrategy">ValueSelectionStrategy</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: CustomResource::Lex::SlotType
Properties:
    <a href="#createversion" title="CreateVersion">CreateVersion</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enumerationvalues" title="EnumerationValues">EnumerationValues</a>: <i>
      - <a href="enumerationvalue.md">EnumerationValue</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentslottypesignature" title="ParentSlotTypeSignature">ParentSlotTypeSignature</a>: <i>String</i>
    <a href="#slottypeconfigurations" title="SlotTypeConfigurations">SlotTypeConfigurations</a>: <i>
      - <a href="slottypeconfiguration.md">SlotTypeConfiguration</a></i>
    <a href="#valueselectionstrategy" title="ValueSelectionStrategy">ValueSelectionStrategy</a>: <i>String</i>
</pre>

## Properties

#### CreateVersion

When set to true a new numbered version of the slot type is created for each update.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the slot type.

_Required_: No

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>200</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnumerationValues

A list of EnumerationValue objects that defines the values that the slot type can take. Each value can have a list of synonyms, which are additional values that help train the machine learning model about the values that it resolves for a slot.
When Amazon Lex resolves a slot value, it generates a resolution list that contains up to five possible values for the slot. If you are using a Lambda function, this resolution list is passed to the function. If you are not using a Lambda function you can choose to return the value that the user entered or the first value in the resolution list as the slot value. The valueSelectionStrategy field indicates the option to use.

_Required_: No

_Type_: List of <a href="enumerationvalue.md">EnumerationValue</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the slot type. The name is not case sensitive. The name can't match a built-in slot type name, or a built-in slot type name with "AMAZON." removed. For example, because there is a built-in slot type called AMAZON.DATE, you can't create a custom slot type called DATE.

_Required_: Yes

_Type_: String

_Pattern_: <code>^([A-Za-z]_?){1,101}$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ParentSlotTypeSignature

The built-in slot type used as the parent of the slot type. When you define a parent slot type, the new slot type has all of the same configuration as the parent.
Only AMAZON.AlphaNumeric is supported.

_Required_: No

_Type_: String

_Pattern_: <code>^((AMAZON\.)_?|[A-Za-z]_?)+</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotTypeConfigurations

Configuration information that extends the parent built-in slot type. The configuration is added to the settings for the parent slot type.

_Required_: No

_Type_: List of <a href="slottypeconfiguration.md">SlotTypeConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSelectionStrategy

Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:
ORIGINAL_VALUE - Returns the value entered by the user, if the user value is similar to the slot value.
TOP_RESOLUTION - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.
If you don't specify the valueSelectionStrategy, the default is ORIGINAL_VALUE.

_Required_: No

_Type_: String

_Allowed Values_: <code>ORIGINAL_VALUE</code> | <code>TOP_RESOLUTION</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### Version

The version of the slot type.

#### Checksum

Checksum of the $LATEST version of the slot type.

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### LastUpdatedDate

Returns the <code>LastUpdatedDate</code> value.

