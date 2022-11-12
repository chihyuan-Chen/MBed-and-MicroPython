#ifndef __MODEL_JSON_H__
#define __MODEL_JSON_H__

const char recognition_model_string_json[] = {"{\"NumModels\":1,\"ModelIndexes\":{\"0\":\"PT_RANK_1\"},\"ModelDescriptions\":[{\"Name\":\"PT_RANK_1\",\"ClassMaps\":{\"1\":\"Left\",\"2\":\"OK\",\"3\":\"Right\",\"0\":\"Unknown\"},\"ModelType\":\"DecisionTreeEnsemble\",\"FeatureFunctions\":[\"GlobalMinMaxSum\",\"AbsoluteMean\"]}]}"};

int recognition_model_string_json_len = sizeof(recognition_model_string_json);

#endif /* __MODEL_JSON_H__ */
