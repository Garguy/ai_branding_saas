import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";

export class BrandforgeInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

//     const layer = new lambda.LayerVersion(this, "BaseLayer", {
//       code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
//       compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
//     });

        const dockerFunc = new lambda.DockerImageFunction(this, "DockerFunc", {
            code: lambda.DockerImageFunction.fromImageAsset("/")
        })

    const apiLambda = new lambda.Function(this, "ApiFunction", {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset("../app"),
      handler: "brandforge_api.handler",
      layers: [layer],
    });
  }
}
