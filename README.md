grpc検証

## grpcのpythonソースへの変換
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. grpc.proto