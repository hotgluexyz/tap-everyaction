"""Stream type classes for tap-everyaction."""

from __future__ import annotations

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_everyaction.client import EveryActionStream


class ContactsStream(EveryActionStream):
    """Define custom stream for Contacts."""

    name = "contacts"
    path = "/Party"

    @property
    def schema(self) -> dict:
        return th.PropertiesList(
            th.Property("vanId", th.IntegerType),
            th.Property("firstName", th.StringType),
            th.Property("lastName", th.StringType),
            th.Property("middleName", th.StringType),
            th.Property("suffix", th.StringType),
            th.Property("title", th.StringType),
            th.Property("sourceFileTitle", th.StringType),
            th.Property("sourceFileFirstName", th.StringType),
            th.Property("sourceFileMiddleName", th.StringType),
            th.Property("sourceFileLastName", th.StringType),
            th.Property("sourceFileSuffix", th.StringType),
            th.Property("contactSource", th.StringType),
            th.Property("contactMode", th.StringType),
            th.Property("organizationContactCommonName", th.StringType),
            th.Property("organizationContactOfficialName", th.StringType),
            th.Property("salutation", th.StringType),
            th.Property("formalSalutation", th.StringType),
            th.Property("additionalSalutation", th.StringType),
            th.Property("preferredPronoun", th.StringType),
            th.Property("pronouns", th.StringType),
            th.Property("namePronunciation", th.StringType),
            th.Property("envelopeName", th.StringType),
            th.Property("formalEnvelopeName", th.StringType),
            th.Property("additionalEnvelopeName", th.StringType),
            th.Property("contactMethodPreferenceCode", th.StringType),
            th.Property("contactMethodPreferenceId", th.StringType),
            th.Property("contactMethodPreferenceName", th.StringType),
            th.Property("assistantName", th.StringType),
            th.Property("nickname", th.StringType),
            th.Property("website", th.StringType),
            th.Property("professionalSuffix", th.StringType),
            th.Property("party", th.StringType),
            th.Property("employer", th.StringType),
            th.Property("occupation", th.StringType),
            th.Property("jobTitle", th.StringType),
            th.Property("sex", th.StringType),
            th.Property("dateOfBirth", th.StringType),
            th.Property("isDeceased", th.BooleanType),
            th.Property("dateCreated", th.DateTimeType),
            th.Property("dateAcquired", th.DateTimeType),
            th.Property("selfReportedRace", th.StringType),
            th.Property("selfReportedEthnicity", th.StringType),
            th.Property("selfReportedRaces", th.StringType),
            th.Property("selfReportedEthnicities", th.StringType),
            th.Property("selfReportedGenders", th.StringType),
            th.Property("selfReportedSexualOrientations", th.StringType),
            th.Property("selfReportedLanguagePreference", th.StringType),
            th.Property("selfReportedLanguagePreferences", th.StringType),
            th.Property("emails", th.StringType),
            th.Property("phones", th.StringType),
            th.Property("addresses", th.StringType),
            th.Property("recordedAddresses", th.StringType),
            th.Property("pollingLocation", th.StringType),
            th.Property("earlyVoteLocation", th.StringType),
            th.Property("identifiers", th.StringType),
            th.Property("codes", th.StringType),
            th.Property("customFields", th.StringType),
            th.Property("primaryCustomField", th.StringType),
            th.Property("contributionSummary", th.StringType),
            th.Property("suppressions", th.StringType),
            th.Property("caseworkCases", th.StringType),
            th.Property("caseworkIssues", th.StringType),
            th.Property("caseworkStories", th.StringType),
            th.Property("notes", th.StringType),
            th.Property("scores", th.StringType),
            th.Property("customProperties", th.StringType),
            th.Property("electionRecords", th.StringType),
            th.Property("membershipStatus", th.StringType),
            th.Property("organizationRoles", th.StringType),
            th.Property("districts", th.StringType),
            th.Property("surveyQuestionResponses", th.StringType),
            th.Property("finderNumber", th.StringType),
            th.Property("biographyImageUrl", th.StringType),
            th.Property("primaryContact", th.StringType),
        ).to_dict()

