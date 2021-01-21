from aws_cdk import core, aws_lambda_python as lambda_python


class AppStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Package our common dependencies as layers
        db_layer = lambda_python.PythonLayerVersion(scope, 'DB lib', entry='common/db')

        lambda_1 = lambda_python.PythonFunction(scope, 'Lambda 1', entry='lambdas/lambda_1')
        lambda_2 = lambda_python.PythonFunction(scope, 'Lambda 2', entry='lambdas/lambda_2')