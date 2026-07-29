import copy
import unittest

from RUNTIME import Framework
from RUNTIME.adapter import prepare_model_adapter
from RUNTIME.compiler import compile_prompt
from RUNTIME.contracts import Status
from RUNTIME.qa import run_quality_assurance


class PhotographicRealismTest(unittest.TestCase):
    def request(self, location, place, atmosphere, **context):
        user_request = {"location": location, "place": place, "atmosphere": atmosphere,
                        **context}
        return {"user_request": user_request,
                "identity": {"canonical_asset": "USER_SUPPLIED_MASTER_PHOTO"},
                "adapter_id": "ahif.openai-images.v1",
                "execution_timestamp": "2026-07-29T00:00:00Z"}

    def test_bali_sunset_is_identity_safe_and_environmentally_integrated(self):
        result = Framework.execute(self.request("Bali, Indonesia", "beach",
                                   "natural tropical sunset", activity="walking by the shore"))
        prompt = result["final_prompt"].lower()
        for expected in ("natural skin texture", "under-eye", "lip texture", "flyaways",
                         "sunset", "environmental color bounce", "restrained sharpening"):
            self.assertIn(expected, prompt)
        for copied in ("sweater", "glasses", "hand on cheek", "selfie"):
            self.assertNotIn(copied, prompt)
        self.assertEqual(result["reasoning_output"]["identity"]["lock_status"], "locked")
        self.assertIn("waxy or plastic skin", result["final_prompt_package"]["negative_constraints"])

    def test_tokyo_night_has_coherent_low_light_capture(self):
        result = Framework.execute(self.request("Tokyo, Japan", "urban street",
                                   "neon night", activity="walking", weather="light rain",
                                   time="night"))
        prompt = result["final_prompt"].lower()
        self.assertIn("low-light exposure", prompt)
        self.assertIn("neon reflections", prompt)
        self.assertNotIn("sunset key light", prompt)
        self.assertNotIn("daylight", prompt)

    def test_swiss_cafe_uses_contextual_wardrobe_and_depth(self):
        result = Framework.execute(self.request("Swiss Alps", "mountain café terrace",
                                   "natural afternoon", activity="having coffee",
                                   weather="cool", time="afternoon"))
        prompt = result["final_prompt"].lower()
        self.assertIn("cool-weather layers", prompt)
        self.assertIn("moderate depth of field", prompt)
        self.assertNotIn("beachwear", prompt)

    def test_compiler_rejects_unready_and_contradictory_optics(self):
        unready = compile_prompt({"context": {"location": "x", "place": "y", "atmosphere": "z",
                                   "constraints": []}, "identity": {"lock_status": "locked"},
                                   "directives": [], "realism": {"compiler_ready": False}})
        self.assertEqual(unready.status, Status.BLOCKED)
        contradictory = compile_prompt({"context": {"location": "x", "place": "y",
                "atmosphere": "z", "constraints": []}, "identity": {"lock_status": "locked"},
                "directives": [], "realism": {"compiler_ready": True,
                "compiler_directives": {"camera": ["deep depth of field", "shallow depth of field"]},
                "negative_constraints": [], "artifact_risks": []}})
        self.assertIn("AHIF-COMPILER-REALISM-OPTICS-CONTRADICTION", contradictory.errors)

    def test_qa_blocks_synthetic_and_unsupported_claims(self):
        base = {"positive_prompt": "IDENTITY: preserve\nREALISM: waxy plastic skin; perfect symmetry",
                "negative_constraints": ["different person"],
                "identity_binding": {"lock_status": "locked"}, "sections": {"identity": "preserve"}}
        report = run_quality_assurance(base)
        self.assertEqual(report.status, Status.BLOCKED)
        self.assertIn("AHIF-QA-REALISM-SKIN-SYNTHETIC", report.errors)
        claim = copy.deepcopy(base)
        claim["positive_prompt"] = "empirically validated generated image"
        report = run_quality_assurance(claim)
        self.assertIn("AHIF-QA-REALISM-EMPIRICAL-CLAIM", report.errors)
        integration = copy.deepcopy(base)
        integration["positive_prompt"] = "incoherent lighting and pasted subject"
        report = run_quality_assurance(integration)
        self.assertIn("AHIF-QA-REALISM-LIGHTING-INCOHERENT", report.errors)
        self.assertIn("AHIF-QA-REALISM-ENVIRONMENT-INTEGRATION", report.errors)

    def test_adapter_discloses_experimental_semantic_mapping(self):
        package = {"release_eligible": True, "final_prompt": "x", "negative_constraints": ["y"],
                   "identity_binding": {"canonical_asset": "MASTER"},
                   "realism_contract": {"required_semantics": ["skin", "lighting"]}}
        result = prepare_model_adapter({"adapter_id": "ahif.openai-images.v1",
                                        "final_prompt": package})
        self.assertEqual(result.output["registry_status"], "experimental")
        self.assertEqual(result.output["realism_mapping"]["semantic_preservation"], "verbatim-prompt")
        self.assertEqual(result.output["realism_mapping"]["empirical_quality"], "NOT_EVALUATED")

    def test_runtime_is_deterministic_and_does_not_fabricate_evidence(self):
        request = self.request("Bali, Indonesia", "beach", "natural tropical sunset")
        self.assertEqual(Framework.execute(request), Framework.execute(copy.deepcopy(request)))
        result = Framework.execute(request)
        self.assertFalse(result["metadata"]["external_model_invoked"])
        self.assertEqual(result["empirical_validation"]["status"], "NOT_EVALUATED")
        self.assertFalse(result["empirical_validation"]["persisted"])


if __name__ == "__main__":
    unittest.main()
