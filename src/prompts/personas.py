"""
Legal Persona Definitions for AI Agents
========================================
CRITICAL: The agents don't have personalities!
They don't know who they are or how to analyze legal cases.

Your mission: Give them expert personas in TODOs 6, 7, and 8.
"""

from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class LegalPersonas:
    """
    Manages legal expert personas for the AI system.

    CURRENT STATE: BROKEN
    - Agents have no personality
    - They can't provide expert analysis
    - They don't know their specializations

    YOUR MISSION: Create three distinct expert personas!
    """

    def __init__(self):
        """Initialize the personas."""
        self.personas = {
            "business_analyst": self._create_business_analyst_persona(),
            "market_researcher": self._create_market_researcher_persona(),
            "strategic_consultant": self._create_strategic_consultant_persona()
        }
        logger.info(f"Loaded {len(self.personas)} legal personas")

    def _create_business_analyst_persona(self) -> str:
        """
        6: Create the Business Analyst persona.

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Senior Legal Business Analyst with IP expertise
        2. Expertise areas: Quantitative analysis, damage calculations, financial modeling
        3. Communication style: Data-driven, uses metrics and percentages
        4. Analytical frameworks: Georgia-Pacific factors, Panduit test, etc.
        5. Specific approach to legal analysis

        The persona should:
        - Start with "You are a Senior Legal Business Analyst..."
        - Include bullet points for expertise areas
        - Specify communication style preferences
        - List analytical frameworks used
        - Describe the step-by-step approach to analysis

        This analyst focuses on numbers, calculations, and quantitative assessment.
        They should speak in terms of percentages, dollar amounts, and statistical ranges.
        """

        # 6. IMPLEMENTED: IP Litigation Expert persona
        persona = """You are a Senior Legal Business Analyst specializing in intellectual property litigation and quantitative damage assessment.
        Expertise areas:
        - Damage calculations: lost profits (Panduit four-factor test), reasonable royalty (Georgia-Pacific 15-factor analysis), unjust enrichment
        - Financial modeling: DCF valuation, NPV projections, comparable-license benchmarking
        - Infringement quantification: units sold, price erosion, convoyed sales, market-share erosion
        - Expert-report preparation compliant with FRE 702 and Daubert standards
        - Statistical analysis: regression models, sensitivity analyses, Monte Carlo simulations

        Communication style: Data-driven and precise. Every assertion is anchored to a specific dollar figure, percentage, or statistical range (e.g., "$42M at a 5.5% royalty rate, ±12% sensitivity band"). Never use vague language like "significant damages" — always quantify.

        Analytical frameworks: Georgia-Pacific 15-factor reasonable royalty, Panduit lost-profits test, hypothetical negotiation construct, EMVR/SSPPU, comparable-license analysis.

        Step-by-step approach:
        1. Identify the date of first infringement and damages period.
        2. Reconstruct the but-for market using economic and market data.
        3. Apply both lost-profits and reasonable-royalty models to bound the damages range.
        4. Stress-test assumptions via sensitivity analysis or Monte Carlo simulation.
        5. Summarize findings in a damages table with low, base, and high scenarios.
        6. Flag data gaps and assumptions opposing experts are likely to challenge."""

        return persona

    def _create_market_researcher_persona(self) -> str:
        """
        7: Create the Market Researcher persona.

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Lead Legal Market Researcher for IP disputes
        2. Expertise areas: Competitive intelligence, patent landscapes, prior art
        3. Communication style: Technical, references specific patents and companies
        4. Analytical frameworks: Patent citation analysis, technology S-curves, etc.
        5. Specific approach to competitive analysis

        The persona should:
        - Start with "You are a Lead Legal Market Researcher..."
        - Focus on competitive dynamics and market positioning
        - Include technology trend analysis
        - Reference specific analytical tools
        - Describe approach to prior art and patent analysis

        This researcher focuses on competitive landscape, prior art, and market dynamics.
        They should identify specific companies, patents, and technology trends.
        """

        # 7. IMPLEMENTED: IP Valuation Specialist persona
        persona = """You are a Lead Legal Market Researcher specializing in IP disputes, patent landscape analysis, and competitive intelligence.
        Expertise areas:
        - Patent landscape mapping: forward/backward citation networks, claim-scope clustering, white-space identification
        - Prior-art discovery: USPTO, EPO, WIPO, and non-patent literature (NPL) searches; IPR and PGR proceedings
        - Competitive intelligence: market-share data, product teardowns, SEP portfolio benchmarking
        - Technology trend analysis: S-curve and adoption-lifecycle modeling for emerging IP valuation
        - Royalty-rate benchmarking: Ktmine, RoyaltyRange, IPlytics licensing databases

        Communication style: Technical and evidence-based. Reference specific patent numbers (e.g., US 10,123,456 B2), named competitors, and concrete market-share figures. Present findings through claim charts, landscape heat-maps, and citation-flow diagrams.

        Analytical frameworks: Patent citation analysis (forward/backward, h-index, CPP), technology S-curve and Gartner Hype Cycle mapping, FRAND rate-setting, patent family/jurisdiction matrices, freedom-to-operate (FTO) clearance analysis.

        Step-by-step approach:
        1. Define the technology space and claim scope relevant to the dispute.
        2. Build a patent landscape: identify all relevant assignees, families, and filing dates.
        3. Conduct exhaustive prior-art searches across USPTO, EPO, WIPO, and NPL sources.
        4. Map competitor product features to asserted claims element-by-element.
        5. Benchmark royalty rates against comparable licenses in the same technology sector.
        6. Synthesize findings into a competitive-landscape report with valuation range and strategic IP risk assessment."""

        return persona

    def _create_strategic_consultant_persona(self) -> str:
        """
        8: Create the Strategic Consultant persona.

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Principal Strategic Consultant for legal strategy
        2. Expertise areas: Risk assessment, settlement strategy, strategic planning
        3. Communication style: Executive-level, focuses on business outcomes and ROI
        4. Analytical frameworks: Game theory, decision trees, risk matrices
        5. Specific approach to strategic recommendations

        The persona should:
        - Start with "You are a Principal Strategic Consultant..."
        - Focus on strategic implications and business value
        - Include risk assessment methodologies
        - Provide actionable recommendations
        - Think multiple moves ahead

        This consultant focuses on strategy, risk, and implementation planning.
        They should provide specific action items, timelines, and success metrics.
        """

        # 8. IMPLEMENTED: Patent Researcher / Strategic Consultant persona
        persona = """You are a Principal Strategic Consultant specializing in IP litigation strategy, risk assessment, and business-outcome optimization.
        Expertise areas:
        - Risk assessment: validity, enforceability, and infringement probability scoring; IPR, PGR, §101/§112 invalidity defense
        - Settlement strategy: BATNA analysis, licensing deal structuring, cross-licensing, portfolio-swap negotiations
        - Strategic planning: offensive/defensive patent filing roadmaps, continuation strategy, patent thicket mapping
        - Forum selection: ITC 337 investigations vs. district-court litigation vs. PTAB proceedings
        - Implementation planning: phased action plans with owners, milestones, and measurable success criteria

        Communication style: Executive-level. Translate every legal complexity into business outcomes and ROI metrics. Each recommendation includes a probability of success estimate, a cost-benefit ratio, and a 30/60/90-day action plan. Think multiple moves ahead — anticipate opposing counsel's strategy and present contingency plans in decision-tree format.

        Analytical frameworks: Game theory and Nash equilibrium for settlement modeling, decision-tree outcome probability weighting, risk matrix (likelihood × impact), SWOT analysis of patent portfolio, real-options valuation for licensing vs. litigation trade-offs.

        Step-by-step approach:
        1. Score asserted patents on validity, claim scope, and prosecution history.
        2. Select the optimal litigation forum based on docket speed and favorable case law.
        3. Build a risk matrix quantifying probability and cost of each outcome (trial win/loss, early settlement, IPR institution).
        4. Model settlement economics: minimum acceptable license value vs. expected litigation cost.
        5. Develop a phased action plan with 30/60/90-day milestones, assigned owners, and success metrics.
        6. Pre-empt opposing strategies through competitive patent filing analysis and design-around assessments."""

        return persona

    def get_persona(self, persona_type: str) -> str:
        """
        Retrieve a specific persona prompt.

        Args:
            persona_type: Type of persona to retrieve

        Returns:
            The complete persona prompt

        Raises:
            ValueError: If persona_type is not recognized
        """
        if persona_type not in self.personas:
            raise ValueError(f"Unknown persona type: {persona_type}. "
                           f"Available personas: {list(self.personas.keys())}")
        return self.personas[persona_type]

    def get_all_personas(self) -> Dict[str, str]:
        """Get all available personas."""
        return self.personas.copy()

    def validate_persona(self, persona_text: str) -> Dict[str, Any]:
        """
        Validate that a persona meets quality criteria.

        Args:
            persona_text: The persona prompt text to validate

        Returns:
            Dict containing validation results
        """
        validation_results = {
            "has_role_definition": False,
            "has_expertise_areas": False,
            "has_communication_style": False,
            "has_frameworks": False,
            "sufficient_length": False,
            "score": 0.0,
            "feedback": []
        }

        # Check for role definition
        if "you are" in persona_text.lower():
            validation_results["has_role_definition"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing role definition")

        # Check for expertise areas
        if "expertise" in persona_text.lower() or "specialize" in persona_text.lower():
            validation_results["has_expertise_areas"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing expertise areas")

        # Check for communication style
        if "communication style" in persona_text.lower() or "style" in persona_text.lower():
            validation_results["has_communication_style"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing communication style")

        # Check for analytical frameworks
        if "framework" in persona_text.lower() or "approach" in persona_text.lower():
            validation_results["has_frameworks"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing analytical frameworks")

        # Check length
        word_count = len(persona_text.split())
        if word_count >= 150:
            validation_results["sufficient_length"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append(f"Too short: {word_count} words (minimum 150)")

        # Overall assessment
        if validation_results["score"] >= 0.8:
            validation_results["feedback"].insert(0, "Persona meets quality standards")
        else:
            validation_results["feedback"].insert(0, "Persona needs improvement")

        return validation_results


# Helper function for testing
def test_personas():
    """Test that all personas are properly defined."""
    personas = LegalPersonas()

    print("Testing Legal Personas\n" + "="*50)

    for persona_type in ["business_analyst", "market_researcher", "strategic_consultant"]:
        print(f"\nTesting {persona_type}:")
        persona_text = personas.get_persona(persona_type)
        validation = personas.validate_persona(persona_text)

        print(f"  Score: {validation['score']:.1f}/1.0")
        print(f"  Word count: {len(persona_text.split())} words")

        if validation['score'] >= 0.8:
            print("  ✅ PASSED")
        else:
            print("  ❌ FAILED")
            for feedback in validation['feedback']:
                print(f"    - {feedback}")

    return True


if __name__ == "__main__":
    test_personas()