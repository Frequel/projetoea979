import sys;
import os.path;
import json;

import IdentifyRunway;
import Display;
import Correct;
import Calculate;

def ReadJSON(JSONPath, Path):
	File = open(JSONPath, "r");
	Data = json.loads(File.read());
	Data["Image"] = Path;
	File.close();
	return Data;

def Main():
	if (len(sys.argv) < 2):
		sys.exit("No input file path provided.");	
	Path = sys.argv[1];
	ExportPath = None;
	if (len(sys.argv) > 2):
		ExportPath = sys.argv[2];
		os.makedirs(ExportPath, exist_ok = True);
		if (not os.path.exists(ExportPath)):
			ExportPath = None;

	JSONPath = os.path.splitext(Path)[0]+".txt";
	if (not os.path.exists(Path)):
		sys.exit("File does not exist.");
	if (not os.path.exists(JSONPath)):
		sys.exit("JSON file does not exist.");

	JSON = ReadJSON(JSONPath, Path);
	JSON = IdentifyRunway.IdentifyRunway(JSON, ExportPath);
	Display.Display(JSON, ExportPath);
	Correct.Correct(JSON, ExportPath);
	JSON = Calculate.find_position(JSON);

	#Export JSON:
	if (ExportPath is not None):
		File = open(ExportPath + "/11 JSON.txt", "w");
		json.dump(JSON, File, indent = 4);
		File.close();
	
	print(json.dumps(JSON, indent = 4));

if (__name__ == "__main__"):
	Main();
